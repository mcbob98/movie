import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "a story of a boy and his toys that come to life",
                        "/home/m/mcdevitt/Downloads/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
raw_deal = media.Movie("Raw Deal",
                       "A disgraced agent who leaps at a chance for reinstatement.",
                       "/home/m/mcdevitt/Downloads/raw.jpg",
                       "https://www.youtube.com/watch?v=4UUlyAn5Yq")
                       
                       

#print(toy_story.storyline)
avatar = media.Movie("Avatar",
                     "A marine on an alien lpanet",
                     "/home/m/mcdevitt/Downloads/avatar.jpeg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")
#print(avatar.storyline)
#avatar.show_trailer()

force_awakens = media.Movie("Star Wars: The Force Awakens",
                            "The First Order has risen from the fallen Galactic Empire and seeks to eliminate the New Republic.",
                            "/home/m/mcdevitt/Downloads/force.jpg",
                            "www.youtube.com/watch?v=Hyc84zvhbQU")

#force_awakens.show_trailer()

movies = [raw_deal, avatar, force_awakens]

#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
print(media.Movie.__module__)
print(media.Movie.__name__)
