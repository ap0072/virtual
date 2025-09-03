# importing all necessary packages



from flask import Flask,flash
from flask import Blueprint, render_template, url_for,request,redirect


from flask_sqlalchemy import SQLAlchemy



from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer,ListTrainer
import os


from googletrans import Translator
translator = Translator()


#training the chatterbot algo

try:
	os.remove("db.sqlite3")
	print("Old database removed. Training new database")
except:
	print('No database found. Creating new database.')

english_bot = ChatBot('Bot')
english_bot.set_trainer(ListTrainer)
for file in os.listdir('data'):
        print('Training using '+file)
        convData = open('data/' + file).readlines()
        english_bot.train(convData)
        print("Training completed for "+file)



app = Flask(__name__)


english_bot = ChatBot('Bot',
             storage_adapter='chatterbot.storage.SQLStorageAdapter',
             logic_adapters=[
   {
       'import_path': 'chatterbot.logic.BestMatch'
   },
   
],
trainer='chatterbot.trainers.ListTrainer')
english_bot.set_trainer(ListTrainer)




app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasesqlite.sqlite3'
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class databasesqlite(db.Model):
   id = db.Column('student_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   pwd = db.Column(db.String(50))
   email=db.Column(db.String(50))
   no=db.Column(db.String(50))
   
   def __init__(self, name, pwd,email,no):
        self.name = name
        self.pwd = pwd
        self.email = email
        self.no = no

    



#different ways of flow of html pages using render template  
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/new-account',methods=["POST"])
def account1():
        account = databasesqlite(request.form['name'], request.form['pwd'],request.form['email'],request.form['no'])
        user= databasesqlite.query.filter_by(name=request.form['name']).first()
        if user:
            flash("User name already exists")
            return render_template('account.html')

        else:
            # flash("Account created successfully")
            db.session.add(account)
            db.session.commit()
            flash("Account created Successfully")
            return render_template('login.html')
 

@app.route('/forget_password')
def forgot():
    return render_template('forget_password.html')

@app.route('/update-password',methods=["POST"])
def update():
    name=request.form['name']
    password=request.form['pwd']

    cursor=databasesqlite.query.filter_by(name=name).first()
    if not cursor:
        flash("Account doesn't exists")
    else:
        #update database record for password column to particular user
        rows_updated = databasesqlite.query.filter_by(name=name).update(dict(pwd=password))
        db.session.commit()
        flash("Password changed Successfully")
        return render_template('login.html')
    return render_template('forget_password.html')


@app.route('/chatbot',methods=["POST"])
def chatbot():
    name=request.form['name']
    password=request.form['pwd']

    cursor=databasesqlite.query.filter_by(name=name,pwd=password).all()
    cursor12=databasesqlite.query.filter_by(name=name).first()
    
    if cursor:
        return render_template('chat4.html',name=name)
    elif (cursor12):
        flash("Incorrect Password")
    else:
        flash("User name doesn't exists")
    
    return render_template('login.html')



@app.route('/get')
def get_bot_response():
    # userText = request.form['textInput']
    userText = request.args.get('msg')
    print(userText) 
    result=translator.translate(str(userText), dest='en')
    userText1=result.text
    # print(userText1)
    response = str(english_bot.get_response(userText1))


    response=translator.translate(response, dest=result.src)
    # print(response)
    return str(response.text)
    # flash (response)


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=5000)
