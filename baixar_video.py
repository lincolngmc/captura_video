import yt_dlp

#url = 'https://www.youtube.com/watch?v=-FRdGi-ARw0'
url = 'https://www.youtube.com/watch?v=iyjny2WAKcg&t=2s&pp=2AECkAIB0gcJCRsBo7VqN5tD'

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'ffmpeg_location': r'C:\Users\GMCORREIA\OneDrive\developer\python\video\ffmpeg\bin\ffmpeg.exe',
    'merge_output_format': 'mp4',  # força saída em .mp4
    'postprocessor_args': [
        '-c:v', 'copy',  # copia o vídeo sem reencodar
        '-c:a', 'aac',   # reencoda o áudio para AAC
        '-b:a', '192k'   # define bitrate do áudio
    ]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
