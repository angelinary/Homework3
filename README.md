# Homework3

**First time:**

Run the following:

* `python3 -m venv venv`

* `source venv/bin/activate`

* `pip install flask`

* `pip install flask-sqlalchemy`

* `pip install flask-login`

* `pip install flask-wtf`


**To Start:**

Run `python run.py`

Go to the browser and open [127.0.0.1:5000/](127.0.0.1:5000/)

**What is implemented:**

* `/` homepage with links to recipes and add

* `/recipes` to view all recipes

* `/recipe/new` to add a new recipe

* `/recipe/<id>` to view a recipe

* `/recipe/<id>/delete` to delete a recipe

* `User` and `Recipe` models

* `RecipeForm` form