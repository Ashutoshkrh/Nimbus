from flask import *
from connector import initialize
feeder = Blueprint('feeder',__name__,static_folder='static',template_folder='templates')

db = initialize()
@feeder.route('/')
def home():
    print(session)
    if 'username' not in session:
        return redirect('/login')
    if session['username'] == None:
        return redirect('/login')
    users_list = fetch_users() 
    posts_list = fetch_posts()
    session['people'] = 'people'
    return render_template("feed.html",firstname = "Kush",lastname = "Raj",username = "Kushwaha",users_list = users_list,posts = posts_list)


def fetch_users():
    users_col = db['users']
    users_list = users_col.find({},{'_id':1,'firstname':1,'lastname':1,'username':1})
    return users_list

def fetch_posts():
    posts_col = db['Post']
    post_list = posts_col.find({},{'_id' : 1, 'username' : 1, 'title':1,'description' : 1, 'img_url' : 1})
    return post_list
@feeder.route('/people')
def people():
    if 'people' not in session:
        return redirect('/login')
    if(session['people']=='people'):
        users_list = fetch_users()
        return render_template("people.html",users_list = users_list)
    else:
        return redirect('/login')

@feeder.route('/post',methods=["GET","POST"])
def post():
    if 'username' not in session:
        return redirect('/login')
    if session['username'] != None:
        if request.method == "POST":
            data = request.form
            title = data['title']
            description = data['description']
            url = data['url']
            post_col = db["Post"]
            print('eengie')
            data1 = {'username' : str(session['username']),'title' : title,'description':description,'img_url': url}
            print(data1)
            post_col.insert_one(data1)
            print('fddychfyytfufy5ytf')
            return redirect('/feed')
        return render_template('post.html')
    else:
        return redirect('/login')