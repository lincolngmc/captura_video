#método que baixa vídeos do youtube
#pip install pytube moviepy pytubefix
#https://pytube.io/en/latest/user/captions.html

import pytube
from pytubefix import YouTube


#links = ['https://www.youtube.com/watch?v=hMQNmIdxOOI', 'https://www.youtube.com/watch?v=HNJV5RjJwq8', 'https://www.youtube.com/watch?v=wDkecsu-yu8']



yt = YouTube(url='https://www.youtube.com/watch?v=HNJV5RjJwq8'
    , use_oauth=True  # se True, o comando envia informação de 'usuario maior de idade' para youtube.
    ,allow_oauth_cache=True
)

yt.streams.filter(only_audio=False)
#yt.streams
stream = yt.streams.get_by_itag(18)
#print(stream)
stream.download()