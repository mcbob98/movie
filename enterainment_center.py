import media
import fresh_tomatoes

#An instance of the movie class containing one of my favorit movies Raw Deal
raw_deal = media.Movie("Raw Deal",
                       "A disgraced agent who leaps at a chance for "
                       "reinstatement.",
                       "http://people.cis.ksu.edu/~mcdevitt/Movie/raw.jpg",
                       "https://youtu.be/Sr1PSyCxb7g")
                       
                       

#An instance of the movie class containing one of my favorit movies Avatar
avatar = media.Movie("Avatar",
                     "A marine on an alien lpanet",
                     "http://people.cis.ksu.edu/~mcdevitt/Movie/avatar.jpeg",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

"""An instance of the movie class containing one of my favorit movies
   Star Wars Force Awakens"""
force_awakens = media.Movie("Star Wars: The Force Awakens",
                            "The First Order has risen from the fallen Galactic"
                            " Empire and seeks to eliminate the New Republic.",
                            "http://people.cis.ksu.edu/~mcdevitt/Movie/force.jpg",
                            "www.youtube.com/watch?v=Hyc84zvhbQU")


#A list of the tree instances of the movie class created above
movies = [raw_deal, avatar, force_awakens]

"""Calling the fresh_tomatoes open_movies method to create the webpage
    with three of my favorit movies"""
fresh_tomatoes.open_movies_page(movies)
