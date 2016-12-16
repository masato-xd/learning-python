# coding: utf-8
import webbrowser


class Movie(object):

    """docstring for Move

        可以使用这个创建一个电影实例"""

    def __init__(self, movie_title, movie_storyline, movie_image, movie_video):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_image
        self.trailer_youtube_url = movie_video

# 打开指定网址播放视频
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
