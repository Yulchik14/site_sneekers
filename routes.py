import datetime
from flask import render_template,  url_for, request, flash, redirect
from app import app, db
from models import User, Item, Order
from flask_login import current_user, login_user, login_required, logout_user

@app.route("/")
def index():
    items = Item.query.all()
    return render_template("index.html", items = items)

@app.route("/faqs")
def faqs():
    return render_template("faqs.html")
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/productdetail")
def productdetail():
    return render_template("productdetail.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/shoppingcart")
def shoppingcart():
    return render_template("shoppingcart.html")