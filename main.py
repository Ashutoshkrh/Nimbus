from flask import *  
from flask_session import Session
from connector import initialize
import hashlib
from feed.feed import feeder
app = Flask(__name__) 
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) 

app.register_blueprint(feeder,url_prefix='/feed')
db=initialize()

def verify_password(stored_password, provided_password):
   # Hash the provided password
   provided_password_hash = hashlib.sha256(provided_password.encode()).hexdigest()

   return provided_password_hash == stored_password  


def hash_password(password):
   # Create a new sha256 hash object
   sha_signature = hashlib.sha256(password.encode()).hexdigest()
   return sha_signature
   
@app.route('/')
def index():
    if 'username' not in session:
        return redirect('/login')
    return '<h1> "Home page" </h1>' 

@app.route('/signup',methods=["GET","POST"])
def signup():
    if request.method == "POST":
        data = request.form
        firstname = data['firstname']
        lastname = data['lastname']
        username = data['username']
        password = data['password']
        users_col = db['users']
       
        if(firstname=='' or lastname=='' or username=='' or password=='') :
            return render_template('signup.html',Message = "Fields cannot be empty")
        elif(len(username)<3):
            return render_template('signup.html',Message="username must be atleast 3 characters long")
        elif(len(password)<6):
            return render_template('signup.html',Message="Password must be atleast 6 characters long")
        elif(users_col.find_one({'username':username})):
            return render_template('signup.html',Message="Username already exists")
        else:
            encrypted_password = hash_password(password)
           
            data = {'firstname' : firstname,'lastname' : lastname,'username':username,'password': encrypted_password}
            users_col.insert_one(data)
            return redirect('/login')
    else:
        return render_template('signup.html')   
         
             
          


                

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        data = request.form
        username = data['username']
        password = data['password']
        
        user_col = db["users"]
        user_data = user_col.find_one({'username': username})
        ver_pass=verify_password(user_data['password'],password)
        if ver_pass == True:
            session["username"] = username
            return redirect('/')
    return render_template('login.html')
        
@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")
        
if __name__ == '__main__':  
   app.run(debug=True)