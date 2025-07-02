from yt_dlp import YoutubeDL

def SalvarVideo(link, local, qualidade):

    ydl_opts = {
        'outtmpl' : local + '/%(title)s.mp4'
    }
    if qualidade == 1:
        ydl_opts['format'] = '298+bestaudio[ext=m4a]/136+bestaudio[ext=m4a]/bestvideo+bestaudio'

    elif qualidade == 2:
        ydl_opts['format'] = '135+bestaudio[ext=m4a]/bestvideo+bestaudio'
    elif qualidade == 4:
        ydl_opts['format'] = '299+bestaudio[ext=m4a]/137+bestaudio[ext=m4a]/bestvideo+bestaudio'

    with YoutubeDL(ydl_opts) as ydl:
            errorCode = ydl.download([link])
    return errorCode
    #localsalvo = YoutubeDL.get_output_path()
    #return localsalvo