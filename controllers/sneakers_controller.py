from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sneaker import Sneaker
import repositories.sneaker_repository as sneaker_repository
import repositories.brand_repository as brand_repository

sneakers_blueprint = Blueprint("sneakers", __name__)

# NEW
@sneakers_blueprint.route("/sneakers")
def sneakers():
    sneakers = sneaker_repository.select_all() 
    return render_template("sneakers/index.html", all_sneakers = sneakers)

# NEW
@sneakers_blueprint.route("/sneakers/new", methods=['GET'])
def new_sneaker():
    brands = brand_repository.select_all()
    return render_template("sneakers/new.html", all_brands = brands)

# CREATE
@sneakers_blueprint.route("/sneakers", methods=['POST'])
def create_sneaker():
    model       = request.form['model']
    brand_id    = request.form['brand_id']
    price       = request.form['price']
    listed      = request.form['listed']
    brand       = brand_repository.select(brand_id)
    sneaker     = Sneaker(model, brand, price, listed)
    sneaker_repository.save(sneaker)
    return redirect('/sneakers')

# SHOW
@sneakers_blueprint.route("/sneakers/<id>", methods=['GET'])
def show_sneaker(id):
    sneaker = sneaker_repository.select(id)
    return render_template('sneakers/show.html', sneaker = sneaker)

# EDIT
@sneakers_blueprint.route("/sneakers/<id>/edit", methods=['GET'])
def edit_sneaker(id):
    sneaker = sneaker_repository.select(id)
    brands = brand_repository.select_all()
    return render_template('sneakers/edit.html', sneaker = sneaker, all_brands = brands)

# UPDATE
@sneakers_blueprint.route("/sneakers/<id>", methods=['POST'])
def update_sneaker(id):
    model       = request.form['model']
    brand_id    = request.form['brand_id']
    price       = request.form['price']
    listed      = request.form['listed']
    brand       = brand_repository.select(brand_id)
    sneaker     = Sneaker(model, brand, price, listed, id)
    sneaker_repository.update(sneaker)
    return redirect('/sneakers')

# DELETE
@sneakers_blueprint.route("/sneakers/<id>/delete", methods=['POST'])
def delete_sneaker(id):
    sneaker_repository.delete(id)
    return redirect('/sneakers')
