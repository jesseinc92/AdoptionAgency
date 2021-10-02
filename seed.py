from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

photo_url = 'https://i.guim.co.uk/img/media/03734ee186eba543fb3d0e35db2a90a14a5d79e3/0_173_5200_3120/master/5200.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=9c30ed97ea8731f3e2a155467201afe3'

# add pets
sparky = Pet(name='Sparky', species='cat', photo_url=photo_url, age=3, available=True)
daisy = Pet(name='Daisy', species='dog', photo_url=photo_url, age=1, available=True)
boo = Pet(name='Boo', species='Ghost', photo_url=photo_url, age=100, available=True)
ronny = Pet(name='Ronny', species='cat', photo_url=photo_url, age=28, available=True)
jesse = Pet(name='Jesse', species='dog', photo_url=photo_url, age=30, available=True)
pixie = Pet(name='Pixie', species='cat', photo_url=photo_url, age=10, available=True)

# add all seeds to session
db.session.add(sparky)
db.session.add(daisy)
db.session.add(boo)
db.session.add(ronny)
db.session.add(jesse)
db.session.add(pixie)

# commit above session adds
db.session.commit()

