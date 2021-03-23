from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

import json

class OrderForm(FlaskForm):
    item = SelectField('Item')
    quantity = StringField('Quantity')
    buyer_id = StringField('Buyer Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])

    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        #TODO: Use the database instead of re-reading the fixture
        self.item.choices = self._get_sorted_item_names()

    def _get_sorted_item_names(self):
        return sorted([x['name'] for x in json.load(open("./data/products.json"))['products']])

