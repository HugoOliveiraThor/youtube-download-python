import youtube_dl

def baixar_video(url):
    """
    Function  to  download a video from Youtube using a URL as reference.

    Args:
        url (str): A URL from youtube video.
    """
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo[ext=mp4]/best[ext=mp4]',
        'outtmpl': '%(title)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    while True:
        url = input('Type the URL from Youtube video you want to download:')

        if url.strip() == '':
            print('URL invalid. Try again.')
            continue

        try:
            baixar_video(url)
            print(f'Vídeo donwloaded with success: {url}')
        except Exception as e:
            print(f'Failed to download the video: {e}')

        continuar = input('Do you want to download another one ? (s/n): ')
        if continuar.lower() != 's':
            break
