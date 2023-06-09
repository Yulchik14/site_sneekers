import datetime
from flask import render_template,  url_for, request, flash, redirect
from app import app, db
from models import Item, Order

@app.route("/")
def index():
    items = Item.query.all()
    category_map = set()
    for item in items:
        category_map.add(item.category)
    return render_template("index.html", items = items, categories = category_map)

@app.route("/item/<id>")
def item(id):
    item = Item.query.get(id)
    items = Item.query.filter_by(category = item.category).all()
    return render_template("item.html", item = item, items = items)
    
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/purchase/<item_id>", methods = ["POST", "GET"])
def purchase(item_id):
    item = Item.query.get(item_id)
    if request.method == "POST":
        new_order = Order(item_id=item.id,
                            name=request.form['name'], 
                            email=request.form['email'],
                            phone=request.form['phone'],
                            size=request.form['size'],
                            city=request.form['city'],
                            address=request.form['address'],
                            nova_posta=request.form['nova_posta'])
        db.session.add(new_order)
        db.session.commit()
        flash("Замовлення прийнято, очікуйте на дзвінок", "alert-success")
        return redirect(url_for('index'))
    return render_template("purchase.html", item = item)

@app.route("/<category>")
def category(category):
    items = Item.query.filter_by(category=category).all()
    return render_template("category.html", items = items, category = category)