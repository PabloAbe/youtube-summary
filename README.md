# youtube-summary
Este proyecto es una herramienta de automatización en Python diseñada para procesar y resumir el contenido de vídeos de YouTube. La aplicación automatiza un flujo de trabajo completo, desde la extracción del audio hasta la generación de un resumen detallado y conciso.


Cómo Usar el Proyecto
Sigue estas instrucciones para configurar y ejecutar la herramienta de resumen de vídeos.

1. Requisitos
Asegúrate de que tienes los siguientes programas instalados en tu sistema:

Python 3.10+: El script está desarrollado en Python y necesita esta versión o una superior.

FFmpeg: Es una herramienta necesaria para procesar el audio de los vídeos. Puedes instalarla con tu gestor de paquetes (brew install ffmpeg en macOS, sudo apt install ffmpeg en Linux o descargando desde su sitio oficial).

2. Instalación de Bibliotecas
Navega a la carpeta de tu proyecto en el terminal e instala las bibliotecas de Python necesarias usando pip:

Bash

pip install yt-dlp openai ffmpeg-python

3. Configuración de la Clave de API
Este proyecto requiere una clave de la API de OpenAI para funcionar.

Obtén tu clave de API desde: https://platform.openai.com/api-keys.

Configúrala como una variable de entorno en tu terminal. Reemplaza tu_clave_aqui por tu clave real:

Bash

export OPENAI_API_KEY='tu_clave_aqui'


4. Ejecución del Script
Con todo configurado, puedes ejecutar el script. Simplemente proporciona la URL del vídeo de YouTube como un argumento en la línea de comandos:

Bash

python youtube.summary.py 'https://www.youtube.com/watch?v=TKnnmhX-59k'

El script creará un archivo resumo.md en la misma carpeta, que contendrá el resumen del vídeo.
