from flask import render_template, redirect, url_for, request

from product import app


@app.route('/')
def product():
    return render_template("product.html")


@app.route('/')
def prod():
    return render_template("product.html")