from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# add pets
sparky = Pet(name='Sparky', species='cat', age=3, available=True)
daisy = Pet(name='Daisy', species='dog', age=1, available=True)
boo = Pet(name='Boo', species='Ghost', age=100, available=True)
ronny = Pet(name='Ronny', species='cat', age=28, available=True)
jesse = Pet(name='Jesse', species='dog', age=30, available=True)

# add all seeds to session
db.session.add(sparky)
db.session.add(daisy)
db.session.add(boo)
db.session.add(ronny)
db.session.add(jesse)

# commit above session adds
db.session.commit()

