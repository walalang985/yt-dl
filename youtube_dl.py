import pytube as pyt,os, time
from moviepy.editor import VideoFileClip
from urllib.request import urlopen as op
from pathlib import Path
class Internet(object):
    def __init__(self):
        return
    def check(self) -> str:
        self.conn = ""
        url = "https://www.youtube.com"
        timeout = 5
        try:
            response = op(url,timeout=timeout)
            self.conn = str(response)
        except:
           self.conn = str(response)
        return self.conn

class NotEnoughStorageError(Exception):
    def __init__(self,message="The drive is empty"):
        self.message = message
        super().__init__(self.message)
class NoConversionError(Exception):
    def __init__(self,message = "Conversion of videos to audio is not allowed at this time"):
        self.message = message
        super().__init__(self.message)
        '''
        this error is raised when conv2audio is false and the user tries to
        download the audio of a video
        '''
class NotAYoutubeURLError(Exception):
    def __init__(self, message="The given input by the user is not a valid youtube link"):
        self.message = message
        super().__init__(self.message)
class WeakOrNoInternetError(Exception):
    def __init__(self,message="Your connectivity is either weak or you are not connected to one"):
        self.message = message
        super().__init__(self.message)
class youtubeDL(object):
    internet = Internet()
    conv2audio = False
    def __init__(self):
        if not self.conv2audio:
            if os.path.exists("Downloaded Videos"):
                os.chdir("Downloaded Videos")
                return
            else:
                os.mkdir("Downloaded Videos")
                os.chdir("Downloaded Videos")
        else:
            if os.path.exists("Downloaded Audio"):
                os.chdir("Downloaded Audio")
                return
            else:
                os.mkdir("Downloaded Audio")
                os.chdir("Downloaded Audio")

                
    def convert_to_audio(self,conv:bool):
        self.conv2audio = conv
    def download_video(self, url=""):
        self.url = url
        if not "youtube.com" in self.url:
            raise NotAYoutubeURLError
        if self.internet.check:
            filename = str(input("Enter the file name you want to save it as or blank for default"))
            if filename == "":
                vid = pyt.YouTube(self.url)
                stream = vid.streams.get_by_itag(22)
                stream.download()
            else:
                vid = pyt.YouTube(url)
                stream = vid.streams.get_by_itag(22)
                stream.download(filename=filename)
        else:
            raise WeakOrNoInternetError
    def download_playlist(self):
        self.url = str(input("Enter the url to download"))
        if not "youtube.com" in self.url:
            raise NotAYoutubeURLError
        if self.internet.check():
                pl = pyt.Playlist(self.url)
                if os.path.exists(pl.title):
                    os.chdir(pl.title)
                    for url in pl.video_urls:
                        vid = pyt.YouTube(url)                    
                        stream = vid.streams.get_by_itag(22)
                        stream.download()
                else:
                    os.mkdir(pl.title)
                    time.sleep(2)
                    os.chdir(pl.title)
                    for url in pl.video_urls:
                        vid = pyt.YouTube(url)                    
                        stream = vid.streams.get_by_itag(22)
                        stream.download()
        else:
            raise WeakOrNoInternetError
               
    def download_audio_only(self):
        if not self.conv2audio:
            raise NoConversionError
        else:
            print("A")
