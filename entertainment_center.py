import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story" , "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=cRdxXPV9GNQ")
point_break = media.Movie("Point Break", "A young hot shot FBI agent infiltrates a gang of surfing back robbers","https://upload.wikimedia.org/wikipedia/en/7/7a/Point_Break_poster.jpg", "https://www.youtube.com/watch?v=ncvFAm4kYCo")
movies = [toy_story, avatar, point_break]
fresh_tomatoes.open_movies_page(movies)
