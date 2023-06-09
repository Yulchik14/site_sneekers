import datetime
from flask import render_template,  url_for, request, flash, redirect
from app import app, db
from models import User, Item, Order
from flask_login import current_user, login_user, login_required, logout_user

@app.route("/")
def index():
    items = Item.query.all()
    return render_template("index.html", items = items)

@app.route("/item/<id>")
def item(id):
    item = Item.query.get(id)
    items = Item.query.filter_by(category = item.category).all()
    return render_template("item.html", item = item, items = items)
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/purchase/<item_id>")
def purchase(item_id):
    item = Item.query.get(item_id)
    return render_template("purchase.html", item = item)