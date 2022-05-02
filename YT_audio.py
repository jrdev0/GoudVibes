import youtube_dl
import os
import glob
import shutil

def yt_pobieracz(link_yt, nowa_nazwa):
  
    nowa_nazwa = nowa_nazwa + '.mp3'
    options = {
        'format':'bestaudio/best',
        'extractaudio':True,
         'audioformat':'mp3',
        'outtmpl':u'%(id)s.%(ext)s', #ID of the video
        'noplaylist':True,
        'nocheckcertificate':True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '360',
        }]
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([link_yt])

    for filepath in glob.glob(os.path.join('', '*.mp3')):

        mp3_file = str(filepath)
        os.rename(mp3_file, nowa_nazwa)
        
        # To work this localy must be create new directory for saving audio or comment lines below.
        shutil.copy(f'{nowa_nazwa}', f'GuodVibs/', follow_symlinks=True)
        os.remove(nowa_nazwa)
        
        

