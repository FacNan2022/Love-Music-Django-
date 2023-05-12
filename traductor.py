import moviepy.editor as mp
import time

def karaoke(video_path, lyrics):
    # Extraer audio del video
    video = mp.VideoFileClip(video_path)
    audio = video.audio

    # Dividir las letras en líneas individuales
    lines = lyrics.split('\n')

    # Reproducir el audio y mostrar las letras en tiempo real
    start_time = time.time()
    current_line = 0
    while time.time() - start_time <= audio.duration:
        elapsed_time = time.time() - start_time
        if current_line < len(lines) and elapsed_time >= current_line * 2:
            line = lines[current_line]
            print(line)
            current_line += 1

    audio.close()

# Ejemplo de uso
video_path = 'Angel.mp4'  # Ruta al archivo de video
lyrics = """
    Angel
    Así es la ley
Hay un ángel
Hecho para mí
Te conocí
El tiempo se me fue
Tal como llego

Y te fallé
Te hice daño
Tantos años yo
Pasé por todo sin pesar
Te ame sin casi amar
Y al final quien me salvó
El ángel que quiero yo

De nuevo tú te cuelas en mis huesos
Dejándome tu beso
Junto al corazón
Y otra vez tú, abriéndome tus alas me sacas de las malas rachas de dolor
Por que tú eres el ángel que quiero yo

Cuando eso es fallar ya no sé que hacer
Ni a dónde ir
Confio en ti
Y te siento cerca pensando en mi

El cuerpo se me va
Hacia donde tú estás
Mi vida cambió
El ángel que quiero yo

De nuevo tú te cuelas en mis huesos
Dejándome tu beso
Junto el corazón
Y otra vez tu abriéndome tus alas me sacas de las malas rachas de dolor
Por que tú eres el ángel que quiero yo

De nuevo tú te cuelas en mis huesos
Dejándome tu beso
Junto el corazón
Y otra vez tú, abriéndome tus alas me sacas de las malas rachas de dolor
Por que tú eres el ángel que quiero yo
"""  # Letra de la canción

karaoke(video_path, lyrics)



