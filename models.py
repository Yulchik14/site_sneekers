from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "user" # ім'я таблиці

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String)
    
    orders = db.relationship('Order', backref='order', lazy=True)

    #Метод repr використовується для відображення об'єкта у зручному для читача форматі.
    def __repr__(self):
        return f"User: {self.username}"

    def set_password(self, original_password):
        self.password = generate_password_hash(original_password)

    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)
   
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class Item(db.Model):
    __tablename__ = "item"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Float)
    sale = db.Column(db.Float)

class Order(db.Model):
    __tablename__ = "order"
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    city = db.Column(db.String)
    address = db.Column(db.String)
    nova_posta = db.Column(db.String)
    status = db.Column(db.String, default = "Очікування")
