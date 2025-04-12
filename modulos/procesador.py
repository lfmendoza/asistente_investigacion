"""
Módulo para procesar texto utilizando OpenAI y generar resúmenes.
"""
import os
from typing import List, Dict, Any
from openai import OpenAI

def generar_resumen(texto: str, tema: str) -> str:
    """
    Genera un resumen del contenido encontrado utilizando OpenAI.
    
    Args:
        texto (str): El texto completo de los resultados de búsqueda.
        tema (str): El tema de búsqueda original.
        
    Returns:
        str: Resumen generado por el modelo de lenguaje.
    """
    # Inicializar el cliente de OpenAI
    cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Crear prompt para el resumen
    prompt = f"""
    Por favor, genera un resumen conciso pero informativo sobre el tema: "{tema}" 
    basado en la siguiente información recopilada de diversas fuentes web:
    
    {texto[:8000]}  # Limitamos el texto a 8000 caracteres para no exceder los tokens de la API
    
    El resumen debe:
    1. Proporcionar una visión general del tema
    2. Destacar los puntos clave y hallazgos importantes
    3. Ser objetivo y basado en hechos
    4. Tener aproximadamente 300-500 palabras
    """
    
    # Realizar la solicitud a la API
    respuesta = cliente.chat.completions.create(
        model="gpt-4-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente de investigación experto en sintetizar información de múltiples fuentes."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=700
    )
    
    # Obtener y devolver el resumen
    return respuesta.choices[0].message.content

def preprocesar_texto_para_wordcloud(texto: str) -> str:
    """
    Preprocesa el texto para generar una nube de palabras más relevante.
    
    Args:
        texto (str): El texto completo de los resultados de búsqueda.
        
    Returns:
        str: Texto preprocesado para la nube de palabras.
    """
    # Inicializar el cliente de OpenAI
    cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    # Crear prompt para la extracción de palabras clave
    prompt = f"""
    A partir del siguiente texto, extrae las palabras y frases clave que mejor representan 
    el contenido. Elimina palabras comunes, conectores y términos irrelevantes. 
    Proporciona solo una lista de las palabras y frases más significativas, separadas por espacios.
    
    Texto:
    {texto[:5000]}  # Limitamos el texto para no exceder los tokens
    """
    
    # Realizar la solicitud a la API
    respuesta = cliente.chat.completions.create(
        model="gpt-4-mini",
        messages=[
            {"role": "system", "content": "Eres un asistente especializado en análisis de texto y extracción de palabras clave."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500
    )
    
    # Obtener y devolver las palabras clave
    return respuesta.choices[0].message.content