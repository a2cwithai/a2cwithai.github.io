from flask import Flask,request,render_template
import databaseusers as db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/login',methods=['POST','GET'])
def login():
    name1 = request.form['username']
    pwd = request.form['password']
    
    if(db.check_user(name1,pwd)):
        return render_template('home.html' , name=name1)
    else:
        return render_template('login.html' , info = 'Invalid user or Password!')

@app.route('/signup',methods=['POST' , 'GET'])
def signup():
    name1 = request.form['username']
    pwd = request.form['password']
    
    if(db.create_user(name1,pwd)):
        return render_template('home.html',name=name1)
    else:
        return render_template('signup.html' , info='Username exists!')
      
@app.route('/')
def home():
    return render_template('personal.html')

if __name__ == '__main__':
    app.run(debug=True)