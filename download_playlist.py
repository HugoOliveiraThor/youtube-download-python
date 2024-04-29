import youtube_dl

ydl_opts = {
    'playlist': True,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/playlist?list=PL4454867602F707D3'])
