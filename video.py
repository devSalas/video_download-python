from pytube import YouTube
import os

"""def downloadVideo():
  # URL del video que deseas descargar
  video_url =link

  # Crea una instancia de YouTube
  yt = YouTube(video_url)

  
  # Obtén la mejor resolución disponible
  stream = yt.streams.get_highest_resolution() """
 
  # Descarga el video
  #stream.download()

def downloadVideo():
  ruta_archivo = os.path.abspath(__file__)
  ruta_directorio = os.path.dirname(ruta_archivo)

  ruta_video = os.path.join(ruta_directorio,"Vuela.mp4")
  print(ruta_video)
  return ruta_video


def getVideo():
  return ""
