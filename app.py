"""
Aplicación Streamlit para asistente de investigación digital.
"""
import os
import streamlit as st
from dotenv import load_dotenv
import time

# Cargar variables de entorno
load_dotenv()

# Importar módulos personalizados
from modulos.buscador import realizar_busqueda, obtener_texto_completo
from modulos.procesador import generar_resumen, preprocesar_texto_para_wordcloud
from modulos.visualizador import generar_nube_palabras, contar_palabras_frecuentes

# Configuración de la página
st.set_page_config(
    page_title="Asistente de Investigación Digital",
    page_icon="🔍",
    layout="wide"
)

# Título y descripción
st.title("🔍 Asistente de Investigación Digital")
st.markdown("""
Esta herramienta te ayuda a buscar información actualizada en la web sobre cualquier tema,
analiza el contenido utilizando modelos de lenguaje y presenta un resumen junto con visualizaciones interactivas.
""")

# Verificar las claves API
if not os.getenv("OPENAI_API_KEY") or not os.getenv("TAVILY_API_KEY"):
    st.error("""
    ⚠️ Se requieren claves API para el funcionamiento correcto.
    
    1. Copia el archivo `.env.example` a `.env`
    2. Agrega tus claves API:
       - OPENAI_API_KEY: Obtén una clave en [OpenAI](https://platform.openai.com)
       - TAVILY_API_KEY: Obtén una clave en [Tavily](https://tavily.com)
    """)
    st.stop()

# Formulario de búsqueda
with st.form("formulario_busqueda"):
    tema = st.text_input("Ingresa un tema de interés:", placeholder="Ejemplo: Inteligencia artificial aplicada a la medicina")
    boton_buscar = st.form_submit_button("Buscar información")

# Procesar la búsqueda cuando se envía el formulario
if boton_buscar and tema:
    # Crear contenedor para mostrar estado
    estado = st.empty()
    
    # Iniciar búsqueda
    estado.info("🔍 Buscando información en la web...")
    try:
        resultados = realizar_busqueda(tema)
        
        if not resultados:
            st.warning("No se encontraron resultados para el tema especificado. Intenta con otro tema o reformula tu consulta.")
            st.stop()
        
        # Mostrar resultados en tabs
        st.subheader("Resultados de la búsqueda")
        
        # Crear pestañas para los diferentes resultados
        tabs = st.tabs([f"Resultado {i+1}" for i in range(len(resultados))])
        
        # Mostrar cada resultado en su pestaña correspondiente
        for i, (tab, resultado) in enumerate(zip(tabs, resultados)):
            with tab:
                st.markdown(f"### {resultado['titulo']}")
                st.markdown(f"**Fuente:** [{resultado['url']}]({resultado['url']})")
                st.markdown("**Extracto:**")
                st.markdown(resultado['contenido'][:500] + "...")
        
        # Obtener texto completo para análisis
        texto_completo = obtener_texto_completo(resultados)
        
        # Generar resumen
        estado.info("📝 Generando resumen...")
        resumen = generar_resumen(texto_completo, tema)
        
        # Mostrar resumen
        st.subheader("Resumen")
        st.markdown(resumen)
        
        # Preparar texto para nube de palabras
        estado.info("🔄 Procesando texto para visualización...")
        texto_procesado = preprocesar_texto_para_wordcloud(texto_completo)
        
        # Generar nube de palabras
        estado.info("📊 Generando visualización...")
        nube_palabras_img = generar_nube_palabras(texto_procesado)
        
        # Crear columnas para visualizaciones
        col1, col2 = st.columns(2)
        
        # Mostrar nube de palabras
        with col1:
            st.subheader("Nube de Palabras")
            st.markdown(f'<img src="data:image/png;base64,{nube_palabras_img}" alt="Nube de palabras" width="100%">', unsafe_allow_html=True)
        
        # Contar palabras frecuentes
        palabras_frecuentes = contar_palabras_frecuentes(texto_procesado, n=15)
        
        # Mostrar palabras frecuentes
        with col2:
            st.subheader("Palabras más frecuentes")
            for palabra, frecuencia in palabras_frecuentes.items():
                st.write(f"- **{palabra}**: {frecuencia}")
        
        # Limpiar estado
        estado.success("✅ Análisis completo")
        
    except Exception as e:
        estado.error(f"❌ Error durante la búsqueda: {str(e)}")
        st.exception(e)

# Información adicional
with st.expander("ℹ️ Acerca de esta aplicación"):
    st.markdown("""
    **Asistente de Investigación Digital** es una herramienta que integra:
    - Búsqueda web con la API de Tavily
    - Análisis de texto con OpenAI a través de LangChain
    - Visualización de datos con WordCloud y Matplotlib
    - Interfaz interactiva con Streamlit
    
    El código fuente está disponible en el repositorio del proyecto.
    """)

# Footer
st.markdown("---")
st.markdown("Desarrollado como proyecto educativo • 2025")