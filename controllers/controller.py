from flask import render_template
from app import app
from models.orders import orders


@app.route("/order")
def index():
    return render_template("index.html", title="Home", orders=orders)


@app.route("/orders/<id>")
def order(id):
    return render_template("order.html", title="Customer", orders=orders[int(id)])
