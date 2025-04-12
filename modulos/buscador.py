"""
Módulo para realizar búsquedas web utilizando Tavily a través de LangChain.
"""
import os
from typing import List, Dict, Any
from langchain.tools import TavilySearchResults
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import Document

def inicializar_agente_busqueda() -> AgentExecutor:
    """
    Inicializa el agente ReAct de LangChain con la herramienta de búsqueda de Tavily.
    
    Returns:
        AgentExecutor: Agente configurado para realizar búsquedas.
    """
    # Herramienta de búsqueda Tavily
    search_tool = TavilySearchResults(
        tavily_api_key=os.getenv("TAVILY_API_KEY"),
        max_results=5,
        include_raw_content=True,
        include_domains=[],
        exclude_domains=[]
    )
    
    # Modelo de lenguaje para el agente
    llm = ChatOpenAI(
        model="gpt-4-mini",
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    # Plantilla de prompt para el agente
    template = """
    Eres un asistente de investigación que ayuda a buscar información relevante en la web.
    
    Objetivo: Encontrar información actualizada y relevante sobre: {tema}
    
    Debes buscar contenido de fuentes confiables y diversas para proporcionar una visión completa del tema.
    """
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["tema"]
    )
    
    # Crear el agente ReAct
    agent = create_react_agent(llm, [search_tool], prompt)
    agent_executor = AgentExecutor.from_agent_and_tools(
        agent=agent, 
        tools=[search_tool], 
        verbose=True,
        return_intermediate_steps=True
    )
    
    return agent_executor

def realizar_busqueda(tema: str) -> List[Dict[str, Any]]:
    """
    Realiza una búsqueda sobre el tema especificado usando el agente ReAct.
    
    Args:
        tema (str): El tema sobre el cual buscar información.
        
    Returns:
        List[Dict[str, Any]]: Lista de resultados de la búsqueda.
    """
    # Inicializar el agente
    agente = inicializar_agente_busqueda()
    
    # Ejecutar la búsqueda
    resultado = agente.invoke({"tema": tema})
    
    # Procesar y formatear los resultados
    resultados_formateados = []
    
    # Extraer los resultados de los pasos intermedios
    for paso in resultado["intermediate_steps"]:
        # Verificar si es un resultado de búsqueda de Tavily
        if isinstance(paso[1], list) and len(paso[1]) > 0 and isinstance(paso[1][0], dict):
            for item in paso[1]:
                if "title" in item and "content" in item and "url" in item:
                    resultados_formateados.append({
                        "titulo": item.get("title", "Sin título"),
                        "contenido": item.get("content", "Sin contenido"),
                        "url": item.get("url", "Sin URL"),
                        "contenido_raw": item.get("raw_content", item.get("content", ""))
                    })
    
    return resultados_formateados

def obtener_texto_completo(resultados: List[Dict[str, Any]]) -> str:
    """
    Obtiene todo el texto de los resultados para análisis posterior.
    
    Args:
        resultados (List[Dict[str, Any]]): Lista de resultados de búsqueda.
        
    Returns:
        str: Todo el texto concatenado de los resultados.
    """
    texto_completo = ""
    
    for resultado in resultados:
        # Usar el contenido raw si está disponible, de lo contrario usar el contenido normal
        contenido = resultado.get("contenido_raw", resultado.get("contenido", ""))
        texto_completo += contenido + "\n\n"
    
    return texto_completo