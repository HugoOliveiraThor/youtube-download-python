import youtube_dl

def my_hook(d):
    if d['status'] == 'downloading':
        percentage = int(d['_percent'] * 100)
        print(f'Progress: {percentage}%')

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo[ext=mp4]/best[ext=mp4]',
    'progress_hooks': [my_hook],
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=jNQXAC9IVRw'])
