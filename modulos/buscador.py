"""
Módulo para realizar búsquedas web utilizando la API de Tavily directamente.
"""
import os
import requests
from typing import List, Dict, Any
import json

def realizar_busqueda(tema: str) -> List[Dict[str, Any]]:
    """
    Realiza una búsqueda sobre el tema especificado usando la API de Tavily directamente.
    
    Args:
        tema (str): El tema sobre el cual buscar información.
        
    Returns:
        List[Dict[str, Any]]: Lista de resultados de la búsqueda.
    """
    # Obtener la API key de Tavily
    api_key = os.getenv("TAVILY_API_KEY")
    
    if not api_key:
        raise ValueError("No se encontró la clave API para Tavily. Verifica tu archivo .env")
    
    # Configurar la petición a la API de Tavily
    endpoint = "https://api.tavily.com/search"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "api_key": api_key,
        "query": tema,
        "search_depth": "advanced",
        "max_results": 5,
        "include_raw_content": True,
        "include_domains": [],
        "exclude_domains": []
    }
    
    try:
        # Realizar la petición
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Verificar si hubo errores en la petición
        
        # Obtener los resultados
        results = response.json().get("results", [])
        
        # Formatear los resultados
        resultados_formateados = []
        for item in results:
            resultados_formateados.append({
                "titulo": item.get("title", "Sin título"),
                "contenido": item.get("content", "Sin contenido"),
                "url": item.get("url", "Sin URL"),
                "contenido_raw": item.get("raw_content", item.get("content", ""))
            })
        
        return resultados_formateados
    
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la búsqueda: {str(e)}")
        return []

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