from flask_wtf import FlaskForm
from wtforms import StringField, FloatField,  SubmitField, SelectField
from wtforms.validators import DataRequired, InputRequired
from proyecto_inventario.routes import Product, Store


class StoreForm(FlaskForm):
    store_name = StringField('Store', validators=[InputRequired()])
    address = StringField('Address', validators=[DataRequired()])
    description = StringField('Category', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')


class ProductForm(FlaskForm):
    store = SelectField('Store', validators=[DataRequired()])
    product_name = StringField('Product', validators=[DataRequired()])
    description = StringField('Category', validators=[DataRequired()])
    sku = StringField('SKU', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    submit = SubmitField('Submit')

