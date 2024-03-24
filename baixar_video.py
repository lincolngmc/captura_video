#método que baixa vídeos do youtube
#pip install pytube moviepy
#https://pytube.io/en/latest/user/captions.html


from pytube import YouTube

yt = YouTube(
    'https://www.youtube.com/watch?v=mKUfbaLe-Lc',
    # on_progress_callback=progress_func,
    # on_complete_callback=complete_func,
    # proxies=my_proxies,
    use_oauth=False,
    allow_oauth_cache=True
)

yt.streams.filter(only_audio=False)
yt.streams
stream = yt.streams.get_by_itag(18)
print(stream)
stream.download()