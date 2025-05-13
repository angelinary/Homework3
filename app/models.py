from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable = False)
    password = db.Column(db.String(32), nullable = False)
    email = db.Column(db.String(32))
    recipes = db.relationship('Recipe', backref = 'author')

class Recipe(db.Model): # class that inherits from Model class of the defined database
    id = db.Column(db.Integer, primary_key = True) # Prim key must be unique and easily indexable
    title = db.Column(db.String(80), nullable = False)
    description = db.Column(db.String, nullable = False)
    ingredients = db.Column(db.String, nullable = False)
    instructions = db.Column(db.String, nullable = False)
    created = db.Column(db.DateTime, nullable = False)
    author_id = db.Column(db.Integer, db.ForeignKey(User.id))
    