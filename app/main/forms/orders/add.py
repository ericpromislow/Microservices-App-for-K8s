from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from app.models import Product, Customer

class OrderForm(FlaskForm):
    item = SelectField('Item')
    quantity = StringField('Quantity')
    buyer = SelectField('Buyer Name')

    submit = SubmitField('Submit')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.item.choices = self._get_sorted_item_names()
        self.buyer.choices = self._get_sorted_customer_names()

    def _get_sorted_item_names(self):
        return sorted([x.name for x in Product.query.all()])

    def _get_sorted_customer_names(self):
        # We need to do something with that ID
        names = sorted([[x.last_name, x.first_name, x.id] for x in Customer.query.all()])
        return ["%s %s" % (fname, lname) for (lname, fname, id) in names]
