import webbrowser

class Movie():
    """The Movie class allows user to view movie trailers"""

    #A class vairable which all instances of the movie class can use
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    """Contructor for the movie class which takes four perameters
       the title of the movie, the story line of the movie, a link to the poster
       image of the movie and a link to the frailer of the movie"""
    def __init__(self,movie_title,movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
    """A method that opens a web browser and plays a tailer of the move"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
