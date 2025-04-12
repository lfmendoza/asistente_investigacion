"""
Paquete de módulos para el asistente de investigación digital.
"""
# Este archivo hace que el directorio 'modulos' sea reconocido como un paquete Python
# Importamos los módulos para facilitar su acceso
from . import buscador_alternative
from . import procesador
from . import visualizador_simple

# Definir explícitamente qué módulos se pueden importar
__all__ = ['buscador_alternative', 'procesador', 'visualizador_simple']