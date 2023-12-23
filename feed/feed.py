from flask import *
from connector import initialize
feeder = Blueprint('feeder',__name__,static_folder='static',template_folder='templates')

db = initialize()
@feeder.route('/')
def home():
    print(session)
    if session['username'] == None:
        return redirect('/login')
    users_list = fetch_users() 
    return render_template("feed.html",firstname = "Kush",lastname = "Raj",username = "Kushwaha",users_list = users_list)


def fetch_users():
    users_col = db['users']
    users_list = users_col.find({},{'_id':1,'firstname':1,'lastname':1,'username':1})
    return users_list
