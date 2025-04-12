"""
Módulo simplificado para visualización de datos sin dependencia en matplotlib.
"""
from collections import Counter
import re

def contar_palabras_frecuentes(texto: str, n: int = 20) -> dict:
    """
    Cuenta las palabras más frecuentes en el texto.
    
    Args:
        texto (str): El texto para analizar.
        n (int): Número de palabras más frecuentes a devolver.
        
    Returns:
        dict: Diccionario con las palabras más frecuentes y sus conteos.
    """
    # Verificar que texto no sea None
    if texto is None:
        texto = ""
    
    # Asegurarse de que sea string
    texto = str(texto)
    
    # Preprocesar el texto
    palabras = re.findall(r'\b\w+\b', texto.lower())
    
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
    
    # Filtrar palabras vacías y stopwords
    palabras_filtradas = [palabra for palabra in palabras if palabra and palabra not in stopwords and len(palabra) > 2]
    
    # Contar frecuencias
    contador = Counter(palabras_filtradas)
    
    # Obtener las n palabras más frecuentes
    palabras_comunes = dict(contador.most_common(n))
    
    return palabras_comunes

def generar_tabla_html(palabras_frecuentes: dict) -> str:
    """
    Genera una tabla HTML con las palabras más frecuentes.
    
    Args:
        palabras_frecuentes (dict): Diccionario con palabras y frecuencias.
        
    Returns:
        str: Código HTML de la tabla.
    """
    # Verificar que palabras_frecuentes no sea None
    if not palabras_frecuentes:
        palabras_frecuentes = {"No hay suficientes datos": 1}
    
    # Crear estilos CSS para la tabla
    css = """
    <style>
        .palabra-tabla {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            font-family: Arial, sans-serif;
        }
        .palabra-tabla th {
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            text-align: left;
        }
        .palabra-tabla td {
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }
        .palabra-tabla tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        .palabra-tabla tr:hover {
            background-color: #ddd;
        }
        .barra {
            background-color: #4CAF50;
            height: 20px;
            border-radius: 3px;
        }
    </style>
    """
    
    # Obtener el valor máximo para calcular porcentajes para las barras
    max_freq = max(palabras_frecuentes.values()) if palabras_frecuentes else 1
    
    # Construir la tabla HTML
    tabla_html = f"""
    {css}
    <table class="palabra-tabla">
        <tr>
            <th>Palabra</th>
            <th>Frecuencia</th>
            <th>Distribución</th>
        </tr>
    """
    
    # Añadir filas para cada palabra
    for palabra, frecuencia in palabras_frecuentes.items():
        # Calcular ancho de barra en porcentaje
        porcentaje = (frecuencia / max_freq) * 100
        
        tabla_html += f"""
        <tr>
            <td><strong>{palabra}</strong></td>
            <td>{frecuencia}</td>
            <td>
                <div class="barra" style="width: {porcentaje}%;"></div>
            </td>
        </tr>
        """
    
    tabla_html += "</table>"
    
    return tabla_html