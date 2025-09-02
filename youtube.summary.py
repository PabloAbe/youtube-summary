import sys
import os
import ffmpeg
from yt_dlp import YoutubeDL
from openai import OpenAI

# Pega a URL do argumento
try:
    url = sys.argv[1]
except IndexError:
    print("Por favor, forneça uma URL do YouTube como argumento.")
    sys.exit(1)

# Nome do arquivo de saída
output_filename = "audio.wav"

try:
    # Obtém a URL do stream de áudio usando yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        stream_url = info_dict['url']

    # Converte o stream para um arquivo WAV usando ffmpeg
    print("Baixando e convertendo o áudio...")
    (
        ffmpeg
        .input(stream_url)
        .output(output_filename, format='wav', acodec='pcm_s16le', ac=2, ar='44100', loglevel="error")
        .run(cmd='./ffmpeg')
    )
    print("Conversão de áudio concluída.")

    # Cria o cliente OpenAI
    client = OpenAI()

    # Abre o arquivo de áudio para transcrição
    with open(output_filename, "rb") as audio_file:
        print("Iniciando a transcrição...")
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    print("Transcrição concluída.")
    
    # Remove o arquivo de áudio após a transcrição
    os.remove(output_filename)

    # Pede pela revisão e resumo
    print("Gerando o resumo...")
    completion = client.chat.completions.create(
          model="gpt-4o-mini",
          messages=[
              {"role": "system",
                "content": "Você é um assistente que resume vídeos e transcrições do YouTube."},
              {"role": "user",
                "content": f"Descreva e resuma o seguinte vídeo: \n\n{transcript.text}"}
          ])
    
    # Salva o resumo em um arquivo
    with open("resumo.md", "w+") as md:
        md.write(completion.choices[0].message.content)

    print("Resumo do vídeo criado com sucesso no arquivo 'resumo.md'.")

except ffmpeg.Error as e:
    print("Erro do FFmpeg. Verifique o output abaixo para mais detalhes:")
    print(e.stderr.decode('utf8'))
    sys.exit(1)
except Exception as e:
    print(f"Ocorreu um erro: {e}")
    sys.exit(1)