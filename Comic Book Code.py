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
        self.stock = stock
    
        
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
def product_page():
    data = dict (comic_list = comics)
    return data

@route('/purchase_page/<comic_id>')
@view('purchase_page')
def purchase_page(comic_id):
    comic_id = int(comic_id)
    found_comic = None
    for comic in comics:
        if comic.id == comic_id:
            found_comic  = comic
    data = dict (comic = found_comic)
    found_comic.stock = found_comic.stock - 1
    return data







@route("/picture/<filename>")
def serve_picture(filename):
    return static_file(filename, root ="./images")




run(host ='0.0.0.0', port = 8080, reloader = True, debug = True)