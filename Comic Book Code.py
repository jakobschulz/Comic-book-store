#Comic book store website.
#Cosmo's Comics

from bottle import run, route, view, get, post, request
from itertools import count


class Comic:
    _ids = count(0)
    
    def __init__(self, name, image, stock):
        self.id = next(self._ids)
        self.name = name
        self.image = image
        self. stock = stock
    
        
#test data
comics = [Comic("Super Dude", "image", int(8)),
          Comic("Lizard Man", "image", int(12)),
          Comic("Water Woman", "image", int(3))]


#pages
#index page
@route("/")
@view("index")
def index():
    #need this function to attach the decorators above
    pass






run(host ='0.0.0.0', port = 8080, reloader = True, debug = True)