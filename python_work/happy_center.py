# coding: utf-8

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come tolife",
                        "https://upload.wikimedia.org/wikipedia/zh/d/dc/Movie_poster_toy_story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")


moana = media.Movie("Moana",
                    "海洋的故事",
                    "https://upload.wikimedia.org/wikipedia/zh/thumb/d/d5/Moana-poster1.jpg/220px-Moana-poster1.jpg",
                    "https://www.youtube.com/watch?v=uaBzCo4mtNE")


pere = media.Movie("Miss Pere",
                    "佩小姐的神奇故事",
                    "https://upload.wikimedia.org/wikipedia/zh/thumb/5/50/Miss_Peregrine%27s_Home_for_Peculiar_Children_Poster.jpg/220px-Miss_Peregrine%27s_Home_for_Peculiar_Children_Poster.jpg",
                    "https://www.youtube.com/watch?v=WEwqRcaazKY")

movies = [toy_story, moana, pere]
# fresh_tomatoes.open_movies_page(movies)

print dir(media.Movie)
print dir(media.Movie.show_trailer)