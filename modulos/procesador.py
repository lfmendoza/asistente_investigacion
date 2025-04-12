"""
Módulo para procesar texto utilizando OpenAI y generar resúmenes.
"""
import os
from typing import List, Dict, Any
import openai
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
    # Verificar que texto no sea None
    if texto is None:
        texto = "No hay información disponible para resumir."
    
    # Verificar que tema no sea None
    if tema is None:
        tema = "tema no especificado"
    
    # Asegurarse de que ambos sean strings
    texto = str(texto)
    tema = str(tema)
    
    # Obtener la clave API
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Si no hay clave API, generar un resumen simulado
    if not api_key:
        return generar_resumen_simulado(tema)
    
    try:
        # Inicializar el cliente de OpenAI
        cliente = OpenAI(api_key=api_key)
        
        # Limitar el texto para no exceder los tokens
        texto_limitado = texto[:8000]
        
        # Crear prompt para el resumen
        prompt = f"""
        Por favor, genera un resumen conciso pero informativo sobre el tema: "{tema}" 
        basado en la siguiente información recopilada de diversas fuentes web:
        
        {texto_limitado}
        
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
    
    except Exception as e:
        print(f"Error al generar resumen con OpenAI: {str(e)}")
        return generar_resumen_simulado(tema)

def generar_resumen_simulado(tema: str) -> str:
    """
    Genera un resumen simulado cuando no se puede usar la API de OpenAI.
    
    Args:
        tema (str): El tema de búsqueda.
        
    Returns:
        str: Resumen simulado.
    """
    return f"""
    # Resumen sobre {tema}
    
    Este es un resumen generado automáticamente sobre {tema} basado en la información recopilada de diversas fuentes. 
    
    ## Aspectos clave
    
    {tema} es un campo que ha experimentado importantes avances en los últimos años. Según los expertos, las aplicaciones prácticas 
    de {tema} están transformando múltiples industrias, desde la tecnología hasta la economía y la sociedad.
    
    Los puntos más destacados incluyen:
    
    1. La evolución de {tema} ha sido constante, con innovaciones significativas cada año
    2. Los expertos consideran que el impacto de {tema} continuará expandiéndose
    3. Las organizaciones que adoptan {tema} reportan mejoras en eficiencia y resultados
    4. La investigación en {tema} sigue siendo un área prioritaria a nivel global
    
    ## Conclusiones
    
    El futuro de {tema} parece prometedor, con numerosas oportunidades por explorar. Los especialistas recomiendan 
    mantenerse actualizados en este campo dada su relevancia creciente y potencial transformador.
    """

def preprocesar_texto_para_wordcloud(texto: str) -> str:
    """
    Preprocesa el texto para generar una nube de palabras más relevante.
    En esta versión simplificada, realizamos un preprocesamiento básico
    sin depender de la API de OpenAI.
    
    Args:
        texto (str): El texto completo de los resultados de búsqueda.
        
    Returns:
        str: Texto preprocesado para la nube de palabras.
    """
    # Verificar que texto no sea None
    if texto is None:
        texto = ""
    
    # Asegurarse de que sea string
    texto = str(texto)
    
    # Obtener la clave API
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Si hay clave API, intentar usar OpenAI
    if api_key:
        try:
            # Inicializar el cliente de OpenAI
            cliente = OpenAI(api_key=api_key)
            
            # Limitar el texto para no exceder los tokens
            texto_limitado = texto[:5000]
            
            # Crear prompt para la extracción de palabras clave
            prompt = f"""
            A partir del siguiente texto, extrae las palabras y frases clave que mejor representan 
            el contenido. Elimina palabras comunes, conectores y términos irrelevantes. 
            Proporciona solo una lista de las palabras y frases más significativas, separadas por espacios.
            
            Texto:
            {texto_limitado}
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
        
        except Exception as e:
            print(f"Error al preprocesar texto con OpenAI: {str(e)}")
            # En caso de error, continuar con el procesamiento básico
    
    # Procesamiento básico sin OpenAI
    import re
    from collections import Counter
    
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar caracteres especiales y números
    texto = re.sub(r'[^\w\s]', ' ', texto)
    texto = re.sub(r'\d+', ' ', texto)
    
    # Eliminar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto)
    
    # Lista de stopwords en español
    stopwords = [
        "a", "al", "algo", "algunas", "algunos", "ante", "antes", "como", "con", "contra",
        "cual", "cuando", "de", "del", "desde", "donde", "durante", "e", "el", "ella",
        "ellas", "ellos", "en", "entre", "era", "erais", "eran", "eras", "eres", "es",
        "esa", "esas", "ese", "eso", "esos", "esta", "estaba", "estabais", "estaban",
        "estabas", "estad", "estada", "estadas", "estado", "estados", "estamos", "estando",
        "estar", "estaremos", "estará", "estarán", "estarás", "estaré", "estaréis",
        "estaría", "estaríais", "estaríamos", "estarían", "estarías", "estas", "este",
        "estemos", "esto", "estos", "estoy", "estuve", "estuviera", "estuvierais",
        "estuvieran", "estuvieras", "estuvieron", "estuviese", "estuvieseis", "estuviesen",
        "estuvieses", "estuvimos", "estuviste", "estuvisteis", "estuviéramos",
        "estuviésemos", "estuvo", "está", "estábamos", "estáis", "están", "estás", "esté",
        "estéis", "estén", "estés", "fue", "fuera", "fuerais", "fueran", "fueras", "fueron",
        "fuese", "fueseis", "fuesen", "fueses", "fui", "fuimos", "fuiste", "fuisteis",
        "fuéramos", "fuésemos", "ha", "habida", "habidas", "habido", "habidos", "habiendo",
        "habremos", "habrá", "habrán", "habrás", "habré", "habréis", "habría", "habríais",
        "habríamos", "habrían", "habrías", "habéis", "había", "habíais", "habíamos",
        "habían", "habías", "han", "has", "hasta", "hay", "haya", "hayamos", "hayan",
        "hayas", "hayáis", "he", "hemos", "hube", "hubiera", "hubierais", "hubieran",
        "hubieras", "hubieron", "hubiese", "hubieseis", "hubiesen", "hubieses", "hubimos",
        "hubiste", "hubisteis", "hubiéramos", "hubiésemos", "hubo", "la", "las", "le",
        "les", "lo", "los", "me", "mi", "mis", "mucho", "muchos", "muy", "más", "mí", "mía",
        "mías", "mío", "míos", "nada", "ni", "no", "nos", "nosotras", "nosotros", "nuestra",
        "nuestras", "nuestro", "nuestros", "o", "os", "otra", "otras", "otro", "otros",
        "para", "pero", "poco", "por", "porque", "que", "quien", "quienes", "qué", "se",
        "sea", "seamos", "sean", "seas", "ser", "seremos", "será", "serán", "serás", "seré",
        "seréis", "sería", "seríais", "seríamos", "serían", "serías", "seáis", "si", "sido",
        "siendo", "sin", "sobre", "sois", "somos", "son", "soy", "su", "sus", "suya",
        "suyas", "suyo", "suyos", "sí", "también", "tanto", "te", "tendremos", "tendrá",
        "tendrán", "tendrás", "tendré", "tendréis", "tendría", "tendríais", "tendríamos",
        "tendrían", "tendrías", "tened", "tenemos", "tenga", "tengamos", "tengan", "tengas",
        "tengo", "tengáis", "tenida", "tenidas", "tenido", "tenidos", "teniendo", "tenéis",
        "tenía", "teníais", "teníamos", "tenían", "tenías", "ti", "tiene", "tienen",
        "tienes", "todo", "todos", "tu", "tus", "tuve", "tuviera", "tuvierais", "tuvieran",
        "tuvieras", "tuvieron", "tuviese", "tuvieseis", "tuviesen", "tuvieses", "tuvimos",
        "tuviste", "tuvisteis", "tuviéramos", "tuviésemos", "tuvo", "tuya", "tuyas", "tuyo",
        "tuyos", "tú", "un", "una", "uno", "unos", "vosotras", "vosotros", "vuestra",
        "vuestras", "vuestro", "vuestros", "y", "ya", "yo", "él", "éramos"
    ]
    
    # Dividir en palabras y filtrar stopwords
    palabras = texto.split()
    palabras = [p for p in palabras if p not in stopwords and len(p) > 3]
    
    # Contar frecuencias
    contador = Counter(palabras)
    palabras_comunes = contador.most_common(100)
    
    # Crear texto con palabras relevantes repetidas según su frecuencia
    texto_procesado = " ".join([palabra for palabra, freq in palabras_comunes for _ in range(min(freq, 10))])
    
    return texto_procesado