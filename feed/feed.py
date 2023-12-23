from flask import *

feeder = Blueprint('feeder',__name__,static_folder='static',template_folder='templates')

@feeder.route('/test')
def test():
    return render_template("feed.html",firstname = "Kush",lastname = "Raj",username = "Kushwaha")

