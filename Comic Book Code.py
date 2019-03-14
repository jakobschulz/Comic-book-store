#Comic book store website.
#Cosmo's Comics

from bottle import run, route, view, get, post, request, static_file
from itertools import count


class Comic:
    _ids = count(0)
    
    def __init__(self, name, image, stock):
        self.id = next(self._ids)
        self.name = name
        self.image = image
        self. stock = stock
    
        
#test data
comics = [Comic("Super Dude", "superdude.png", int(8)),
          Comic("Lizard Man", "lizardman.jpg", int(12)),
          Comic("Water Woman", "waterwoman.jpg", int(3))]


#pages
#index page
@route("/")
@view("index")
def index():
    #need this function to attach the decorators above
    pass


@route('/product_page')
@view('product_page')
def check_in():
    data = dict (comic_list = comics)
    return data









@route("/picture/<filename>")
def serve_picture(filename):
    return static_file(filename, root ="./images")




run(host ='0.0.0.0', port = 8080, reloader = True, debug = True)