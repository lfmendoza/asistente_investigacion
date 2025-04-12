"""
Módulo para visualización de datos y generación de nubes de palabras.
"""
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import io
import base64

def generar_nube_palabras(texto: str) -> str:
    """
    Genera una nube de palabras a partir del texto proporcionado.
    
    Args:
        texto (str): El texto para generar la nube de palabras.
        
    Returns:
        str: Imagen de la nube de palabras en formato base64 para mostrar en Streamlit.
    """
    # Configuración de la nube de palabras
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=150,
        colormap='viridis',
        contour_width=1,
        contour_color='steelblue',
        collocations=True
    ).generate(texto)
    
    # Crear figura
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    
    # Convertir la figura a imagen base64 para Streamlit
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    
    # Convertir a base64
    img_str = base64.b64encode(buf.read()).decode()
    
    return img_str

def contar_palabras_frecuentes(texto: str, n: int = 10) -> dict:
    """
    Cuenta las palabras más frecuentes en el texto.
    
    Args:
        texto (str): El texto para analizar.
        n (int): Número de palabras más frecuentes a devolver.
        
    Returns:
        dict: Diccionario con las palabras más frecuentes y sus conteos.
    """
    # Lista de palabras comunes (stopwords) en español
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
        "sea", "seamos", "sean", "seas", "seremos", "será", "serán", "serás", "seré",
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
    
    # Convertir a minúsculas y dividir en palabras
    palabras = texto.lower().split()
    
    # Eliminar signos de puntuación
    palabras = [palabra.strip('.,;:()[]{}"""\'\'') for palabra in palabras]
    
    # Filtrar palabras vacías y stopwords
    palabras = [palabra for palabra in palabras if palabra and palabra not in stopwords and len(palabra) > 2]
    
    # Contar frecuencias
    conteo = {}
    for palabra in palabras:
        conteo[palabra] = conteo.get(palabra, 0) + 1
    
    # Ordenar por frecuencia y tomar las n más frecuentes
    palabras_frecuentes = dict(sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:n])
    
    return palabras_frecuentes