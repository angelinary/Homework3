from app import myapp_obj
from flask import render_template, url_for, redirect, request
from app.forms import LoginForm, RecipeForm
from app.models import User, Recipe
from app import db
from datetime import datetime
# from <X> import <Y>

@myapp_obj.route("/")
def index():
    return render_template('index.html')

@myapp_obj.route("/recipes")
def recipes():
    rows = db.session.query(Recipe) # request every row in recipe table
    return render_template('recipes.html', recipes = rows)

@myapp_obj.route("/recipe/<id>")
def recipe(id = 0):
    result = db.session.query(Recipe).filter_by(id = id).first()
    return render_template('recipe.html', recipe = result)

@myapp_obj.route('/recipe/new', methods=['GET', 'POST'])
def add():
    form = RecipeForm()
    # check if the form is being submitted
    if request.method == 'POST':
        # get the default user
        user = User.query.filter_by(id = 1).first()
        if user is None:
            # create the user if needed
            default_user = User(
                username = 'default',
                password = '',
            )
            db.session.add(default_user)
            db.session.commit()
        
        # now create the new recipe
        recipe = Recipe(
            title = form.title.data,
            description = form.description.data, 
            ingredients = form.ingredients.data,
            instructions = form.instructions.data, 
            created = datetime.now(),
            author_id = 1,
        )
        db.session.add(recipe)
        db.session.commit()
        return redirect(url_for('recipes'))
    
    return render_template('add.html', form=form)

@myapp_obj.route('/recipe/<id>/delete')
def delete(id = 0):
    result = Recipe.query.filter_by(id = id).first()
    if result:
        db.session.delete(result)
        db.session.commit()
        
    # don't need to do anything if the result doesn't exist
    
    return redirect(url_for('recipes'))


@myapp_obj.route("/accounts")
def users():
    return "My USER ACCOUNTS"

@myapp_obj.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(f"Here is the input from the user {form.username.data} and {form.password.data}")
        return redirect("/")
    else:
        print("MOOOO MOOO")
    return render_template("login.html", form=form)
    # What is render template returning?
    #return str(type(render_template("login.html", form=form)))
