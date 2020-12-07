from flask import render_template, redirect, url_for, request

from product import app


@app.route('/')
def product():
    return render_template("product.html")


@app.route('/login')
def login():
    return render_template("login.html")