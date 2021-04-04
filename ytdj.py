import os
import re
import json
from pytube import YouTube
from moviepy.editor import *

class Downloader:
    def __init__(self):
        pass
    def download(self, url):
        url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        id = re.findall('https:\/\/w*?.?youtube.com\/watch\?v=([A-z 0-9]*)', url)[0]
        path = './ytdl/temp/mp4/'

        video = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ').streams.get_lowest_resolution()
        video.download(path)
        os.rename(f'{path}{video.title}.mp4', f'{path}{id}.mp4')

        return id

    def convert(self, id: str):
        path = './ytdl/temp/'

        video = VideoFileClip(f'mp4/{id}.mp4')
        video.audio.write_audiofile(f'mp3/{id}.mp3')

        os.remove(f'{path}mp4/{id}.mp4')

    def check_cache(self, id: str):
        path = './ytdl/temp/'

        if os.path.exists(f'{path}mp4/{id}.mp4') or os.path.exists(f'{path}mp3/{id}.mp3')

dl = Downloader()
id = dl.download('d')
dl.convert(id)




""" def inp():
    res = input('What song do you want?')

class Translator:
    def __init__(self, lang: str):
        self.contents = None
        self.lang = lang

    def translate(self, label: str):
        if self.contents == None:
            self.contents = self.read_langfile()

        if label in self.contents:
            return self.contents[label]
        raise Exception(f'Key \'{label}\' was not found in the language file \'{self.lang}.json\'')

    def read_langfile(self):
        lang = self.lang

        for file in os.listdir('./ytdl/lang'):
            if file[:-5] == lang:
                with open(f'./ytdl/lang/{file}', 'r') as f:
                    contents = json.load(f)
                return contents
        raise Exception('Language file not found.')

tstr = Translator('en_US')
out = tstr.translate('nextsong')
print(out) """