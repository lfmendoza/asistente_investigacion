# 🔍 Asistente de Investigación Digital

Esta aplicación web interactiva funciona como un asistente de investigación digital, capaz de buscar información actualizada en la web, analizarla utilizando modelos de lenguaje y presentar un resumen junto con una visualización interactiva de las palabras más frecuentes.

## 📋 Características

- Búsqueda web con la API de Tavily a través de un agente ReAct de LangChain
- Presentación amigable de resultados (título, contenido, enlaces)
- Generación automática de resúmenes con OpenAI (GPT-4-mini)
- Visualización interactiva con nubes de palabras
- Interfaz de usuario intuitiva desarrollada con Streamlit

## 🚀 Instalación

### Requisitos previos

- Python 3.9 o superior
- Claves API para OpenAI y Tavily

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

4. Configurar las claves API:
   ```bash
   cp .env.example .env
   ```
   
   Edita el archivo `.env` y agrega tus claves API:
   ```
   OPENAI_API_KEY=tu_clave_de_openai
   TAVILY_API_KEY=tu_clave_de_tavily
   ```

## 💻 Uso

1. Iniciar la aplicación:
   ```bash
   streamlit run app.py
   ```

2. Abrir el navegador en la dirección mostrada (generalmente http://localhost:8501)

3. Ingresar un tema de interés en el campo de texto y hacer clic en "Buscar información"

4. Explorar los resultados, el resumen y las visualizaciones generadas

## 🏗️ Estructura del proyecto

```
asistente_investigacion/
├── .env.example                # Plantilla para las claves de API
├── README.md                   # Documentación del proyecto
├── app.py                      # Punto de entrada principal de Streamlit
└── modulos/
    ├── __init__.py             # Hace que el directorio sea un paquete
    ├── buscador.py             # Módulo para la búsqueda con Tavily
    ├── procesador.py           # Módulo para procesamiento con OpenAI
    └── visualizador.py         # Módulo para visualización (WordCloud)
```

## 📚 Descripción de los módulos

### `modulos/buscador.py`

Este módulo se encarga de realizar búsquedas web utilizando la API de Tavily a través de LangChain. Implementa un agente ReAct que busca información relevante sobre el tema proporcionado por el usuario.

Funciones principales:
- `inicializar_agente_busqueda()`: Configura el agente ReAct con la herramienta de búsqueda.
- `realizar_busqueda(tema)`: Ejecuta la búsqueda y procesa los resultados.
- `obtener_texto_completo(resultados)`: Extrae todo el texto de los resultados para análisis posterior.

### `modulos/procesador.py`

Este módulo utiliza la API de OpenAI para analizar y procesar el texto obtenido de las búsquedas.

Funciones principales:
- `generar_resumen(texto, tema)`: Genera un resumen del contenido utilizando GPT-4-mini.
- `preprocesar_texto_para_wordcloud(texto)`: Preprocesa el texto para generar una nube de palabras más relevante.

### `modulos/visualizador.py`

Este módulo se encarga de generar visualizaciones a partir del texto procesado.

Funciones principales:
- `generar_nube_palabras(texto)`: Genera una nube de palabras a partir del texto.
- `contar_palabras_frecuentes(texto, n)`: Cuenta las palabras más frecuentes en el texto.

## 🛠️ Tecnologías utilizadas

- **Streamlit**: Para la interfaz de usuario web
- **LangChain**: Para la integración de modelos de lenguaje y herramientas
- **OpenAI API**: Para el procesamiento de lenguaje natural
- **Tavily API**: Para la búsqueda de información en la web
- **WordCloud y Matplotlib**: Para la visualización de datos
- **Python-dotenv**: Para la gestión de variables de entorno

## 📦 Requisitos

```
streamlit==1.32.0
requests==2.31.0
openai==1.12.0
python-dotenv==1.0.0
langchain==0.1.4
langchain-openai==0.0.5
matplotlib==3.8.2
wordcloud==1.9.2
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

## 🙏 Agradecimientos

- Equipo de OpenAI por proporcionar la API para el procesamiento de lenguaje natural
- Equipo de Tavily por su API de búsqueda web
- Comunidad de Streamlit por crear una herramienta tan versátil para aplicaciones web en Python
- Desarrolladores de LangChain por facilitar la integración de modelos de lenguaje con herramientas