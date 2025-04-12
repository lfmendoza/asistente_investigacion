# 🔍 Asistente de Investigación Digital

Esta aplicación web interactiva funciona como un asistente de investigación digital, capaz de buscar información actualizada en la web, analizarla utilizando modelos de lenguaje y presentar un resumen junto con una visualización interactiva de las palabras más frecuentes.

## 📋 Características

- Búsqueda web con la API de Tavily directamente con requests
- Presentación amigable de resultados (título, contenido, enlaces)
- Generación automática de resúmenes con OpenAI
- Visualización interactiva de las palabras más frecuentes
- Interfaz de usuario intuitiva desarrollada con Streamlit

## 🚀 Instalación

### Requisitos previos

- Python 3.8 o superior
- Claves API para OpenAI y Tavily (opcional, la aplicación funciona en modo simulado sin ellas)

### Pasos de instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/lfmendoza/asistente_investigacion.git
   cd asistente_investigacion
   ```

2. Crear y activar un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv

   # En Windows
   venv\Scripts\activate

   # En macOS/Linux
   source venv/bin/activate
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

4. Configurar las claves API (opcional):

   ```bash
   cp .env.example .env
   ```

   Edita el archivo `.env` y agrega tus claves API:

   ```
   OPENAI_API_KEY=tu_clave_de_openai
   TAVILY_API_KEY=tu_clave_de_tavily
   ```

## 📋 Resultados de pruebas

En la raíz del proyecto se encuentran varios archivos PDF que contienen los resultados de diferentes pruebas realizadas con la aplicación:

- `Asistente de Investigación Digital.pdf` - Prueba principal del funcionamiento completo
- `Asistente de Investigación Digital-2.pdf` - Prueba de búsquedas sobre temas tecnológicos
- `Asistente de Investigación Digital-3.pdf` - Prueba de búsquedas sobre temas científicos
- `Asistente de Investigación Digital-4.pdf` - Prueba de búsquedas sobre temas educativos
- `Asistente de Investigación Digital-5.pdf` - Prueba de funcionamiento con API simulada

Estos archivos demuestran el correcto funcionamiento de la aplicación en diferentes escenarios y con distintos tipos de consultas.

## 💻 Uso

1. Iniciar la aplicación:

   ```bash
   streamlit run app_simple.py
   ```

2. Abrir el navegador en la dirección mostrada (generalmente http://localhost:8501)

3. Ingresar un tema de interés en el campo de texto y hacer clic en "Buscar información"

4. Explorar los resultados, el resumen y las visualizaciones generadas

## 🏗️ Estructura del proyecto

```
asistente_investigacion/
├── Asistente de Investigación Digital.pdf     # Prueba principal
├── Asistente de Investigación Digital-2.pdf   # Prueba con temas tecnológicos
├── Asistente de Investigación Digital-3.pdf   # Prueba con temas científicos
├── Asistente de Investigación Digital-4.pdf   # Prueba con temas educativos
├── Asistente de Investigación Digital-5.pdf   # Prueba con API simulada
├── .env.example                               # Plantilla para las claves de API
├── .env                                       # Archivo para tus claves API (debes crearlo)
├── README.md                                  # Documentación del proyecto
├── app_simple.py                              # Aplicación principal (versión simplificada)
├── requirements.txt                           # Dependencias del proyecto
└── modulos/
    ├── __init__.py                            # Hace que el directorio sea un paquete
    ├── buscador_alternative.py                # Módulo para la búsqueda (versión alternativa)
    ├── procesador.py                          # Módulo para procesamiento con OpenAI
    └── visualizador_simple.py                 # Módulo para visualización simplificada
```

## 📚 Descripción de los módulos

### `buscador_alternative.py`

Este módulo se encarga de realizar búsquedas web simuladas. Cuando no se dispone de una clave API de Tavily válida, genera resultados simulados basados en el tema proporcionado.

Funciones principales:

- `realizar_busqueda(tema)`: Simula una búsqueda web sobre el tema especificado.
- `obtener_texto_completo(resultados)`: Extrae todo el texto de los resultados para análisis posterior.

### `procesador.py`

Este módulo utiliza la API de OpenAI para analizar y procesar el texto obtenido de las búsquedas. Incluye mecanismos de respaldo para funcionar sin una clave API de OpenAI.

Funciones principales:

- `generar_resumen(texto, tema)`: Genera un resumen del contenido utilizando OpenAI o un generador simulado.
- `preprocesar_texto_para_wordcloud(texto)`: Preprocesa el texto para la visualización de palabras frecuentes.

### `visualizador_simple.py`

Este módulo se encarga de generar visualizaciones a partir del texto procesado, utilizando HTML/CSS en lugar de bibliotecas externas como matplotlib.

Funciones principales:

- `contar_palabras_frecuentes(texto, n)`: Cuenta las palabras más frecuentes en el texto.
- `generar_tabla_html(palabras_frecuentes)`: Genera una tabla HTML con barras de progreso para representar la frecuencia de palabras.

## 🛠️ Tecnologías utilizadas

- **Streamlit**: Para la interfaz de usuario web
- **OpenAI API**: Para el procesamiento de lenguaje natural
- **Tavily API**: Para la búsqueda de información en la web
- **Python-dotenv**: Para la gestión de variables de entorno

## 📦 Requisitos

```
streamlit==1.32.0
requests==2.31.0
openai==1.12.0
python-dotenv==1.0.0
```

## 🤔 Reflexión crítica sobre el uso de IA para buscar y procesar información

El uso de inteligencia artificial para buscar y procesar información representa un avance significativo en la manera en que accedemos al conocimiento, pero también plantea importantes consideraciones:

### Ventajas

- **Eficiencia**: La IA puede analizar grandes volúmenes de información en segundos, algo imposible para un humano.
- **Acceso a información diversa**: Permite obtener una visión más amplia y variada sobre un tema específico.
- **Reducción de sesgos humanos**: Potencialmente puede reducir algunos sesgos cognitivos presentes en la investigación humana.
- **Personalización**: Adapta los resultados a necesidades específicas del usuario.

### Desafíos y limitaciones

- **Calidad y veracidad**: La IA no siempre distingue información veraz de la falsa, pudiendo propagar desinformación.
- **Sesgos algorítmicos**: Los sistemas pueden reflejar y amplificar sesgos presentes en sus datos de entrenamiento.
- **Falta de pensamiento crítico**: La IA carece de la capacidad humana para evaluar críticamente el contexto y la fiabilidad de las fuentes.
- **Dependencia tecnológica**: Puede reducir las habilidades de investigación independiente de los usuarios.
- **Burbujas informativas**: Los algoritmos pueden reforzar creencias existentes al mostrar información que coincide con preferencias previas.

### Consideraciones éticas

- Es crucial mantener la transparencia sobre cuándo la información ha sido procesada por IA.
- Los usuarios deben desarrollar alfabetización digital para evaluar críticamente los resultados.
- El papel humano en la verificación y contextualización de la información sigue siendo insustituible.

Esta aplicación busca ser una herramienta complementaria que potencie las capacidades de investigación humanas, no reemplazarlas. El objetivo es proporcionar un punto de partida eficiente para explorar temas, pero siempre fomentando el análisis crítico y la verificación de fuentes por parte del usuario.

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
s
