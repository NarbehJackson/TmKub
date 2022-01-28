from flask import Flask, request, render_template_string, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from utils import Crypt

app = Flask(__name__)

username = os.environ.get('USERNAME','root')
password = os.environ.get('MYSQL_ROOT_PASSWORD')
database = os.environ.get('MYSQL_DATABASE')
host = os.environ.get('MYSQL_HOST')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{0}:{1}@{2}/{3}'.format(username,password,host,database)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class CreditCard(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(250))
    name = db.Column(db.String(250)) 
    expiry = db.Column(db.String(50)) 

db.create_all()

@app.route('/not-found')
def not_found():
    page = request.args.get('page','')
    template = '<h2>{0} Page you are looking for cannot be found! </h2>'.format(page)
    return render_template_string(template), 404


@app.route('/payment',methods=['GET', 'POST'])
def upload():	
    if request.method == 'GET':
        return render_template("payment.html")
    elif request.method == 'POST':        
        u = request.form		
        card = CreditCard()	        
        card.number = Crypt().encrypt(u.get('number'))
        card.name = u.get('name')
        card.expiry = u.get('expiry')
        db.session.add(card)
        db.session.commit()	
        return redirect('/payment')    
    

app.run(debug=True,host='0.0.0.0')    