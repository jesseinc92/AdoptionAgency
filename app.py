from models import connect_db
from flask import Flask, render_template, redirect
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()


@app.route('/')
def show_pet_list():
    '''Displays a list of the pets in the database.'''
    return render_template('pet-list.html')