
from flask import Flask, request, jsonify
from flask import render_template, flash,redirect,url_for
from proyecto_inventario import app, db
from proyecto_inventario.models import Store, Product
from proyecto_inventario.forms import StoreForm, ProductForm




@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html')


@app.route('/storeform', methods=['GET', 'POST'])
def storeform():
    form = StoreForm()
    if request.method == 'POST':
        store = Store(name=form.store_name.data,
                      description=form.description.data,
                      email=form.email.data, address=form.address.data)
        db.session.add(store)
        db.session.commit()
        flash('Your store has been added!', 'success')
        stores = Store.query.all()
        return render_template('list_stores.html', stores_list=stores)
    else:
        return render_template('storeform.html', title='Form', form=form)


@app.route('/productform', methods=['GET', 'POST'])
def productform():
    form = ProductForm()
    store_choices = (Store.query.distinct(Store.name).all())
    stores_names = []
    for s in store_choices:
        stores_names.append((s.id, s.name))
    print(stores_names)
    form.store.choices = stores_names

    if request.method == 'POST':
        print(form.store.data, form.product_name.data, form.description.data, form.quantity.data, form.price.data, form.sku.data)
        product = Product(store_id=form.store.data, name=form.product_name.data,
        description=form.description.data, quantity=form.quantity.data,
        price=form.price.data, sku=form.sku.data)
        db.session.add(product)
        db.session.commit()
        flash('Your product has been added!', 'success')
        return render_template('home.html')
    else:
        return render_template('productform.html', title='Form', form=form)


@app.route('/list_stores')
def getstorestable():
    stores_list = Store.query.all()
    return render_template('list_stores.html', stores_list=stores_list)


@app.route('/store/<string:store_id>/', methods=["PUT", "GET", "POST"])
def edit_store(store_id):
    store = Store.query.filter_by(id=store_id).first()
    # product_found = [product for product in products if product['name'] == name]
    form = StoreForm()
    if request.method == 'POST':
        store.name = form.store_name.data,
        store.address = form.address.data,
        store.description = form.description.data,
        store.email = form.email.data,

        db.session.add(store)
        db.session.commit()
        flash('Your store has been updated!', 'success')
        stores = Store.query.all()
        return render_template('list_stores.html', stores_list=stores)

    return render_template('update_store.html', title='Form',
                           form=form, legend='Update Store', store=store)



# a list of all products
@app.route('/product_list')
def getproducts():
    products = Product.query.all()
    return render_template('product_list.html', products=products)


@app.route('/product/<string:name>')
def product(name):
    store = Store.query.filter_by(name=name).first_or_404()
    products = Product.query.filter_by(storesname=store)
    return render_template('product_list.html', products=products, store=store)


@app.route('/products/<string:store>/<string:name>', methods=["PUT", "GET", "POST"])
def edit_product(store, name):
    product = Product.query.filter_by(id=name, store_id=store).first()
    # product_found = [product for product in products if product['name'] == name]
    form = ProductForm()
    if request.method == 'POST':
        print(form.store.data, form.product_name.data, form.description.data, form.quantity.data, form.price.data,
              form.sku.data)
        product.name = form.product_name.data,
        product.description = form.description.data,
        product.quantity = form.quantity.data,
        product.price = form.price.data,
        product.sku = form.sku.data
        db.session.add(product)
        db.session.commit()
        flash('Your product has been updated!', 'success')
        products = Product.query.filter_by(store_id=store)
        return render_template('product_list.html', products=products, store=store)

    return render_template('update_product.html', title='Form',
                           form=form, legend='Update Product', product=product)


@app.route('/delete/product/<string:store_id>/<string:name>', methods=["GET"])
def delete_product(store_id, name):
    Product.query.filter_by(id=name, store_id=store_id).delete()
    db.session.commit()
    flash('Your product has been deleted!', 'success')
    store = Product.query.filter_by(store_id=store_id)
    products = Product.query.filter_by(store_id=store_id)
    return render_template('product_list.html', products=products, store=store)






