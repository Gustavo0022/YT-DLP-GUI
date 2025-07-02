from yt_dlp import YoutubeDL

def SalvarAudio(link, local):
    ydl_opts = {
        'outtmpl' : local + '/%(title)s',
        'format': 'mp3/bestaudio/best', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }
    print( local + '/%(title)s')
    with YoutubeDL(ydl_opts) as ydl:
        errorCode = ydl.download(link)
    return errorCode

    