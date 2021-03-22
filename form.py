from wtforms import Form, StringField

class OrderForm(Form):
    item = StringField('Item')
    quantity = StringField('quantity')
    buyer_id = StringField('Buyer Name')
    city = StringField('City')

