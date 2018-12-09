import time
from collections import OrderedDict
from backend.utils import import_class


class Payment:
    authorization_number = None
    amount = None
    invoice = None
    order = None
    payment_method = None
    paid_at = None

    def __init__(self, attributes={}):
        self.authorization_number = attributes.get('attributes', None)
        self.amount = attributes.get('amount', None)
        self.invoice = attributes.get('invoice', None)
        self.order = attributes.get('order', None)
        self.payment_method = attributes.get('payment_method', None)

    def pay(self, paid_at=time.time()):
        self.amount = self.order.total_amount()
        self.authorization_number = int(time.time())
        attributes = dict(
            billing_address=self.order.address,
            shipping_address=self.order.address,
            order=self.order
        )
        self.invoice = Invoice(attributes=attributes)
        self.paid_at = paid_at
        self.order.payment = self
        self.order.close(self.paid_at)

    def is_paid(self):
        return self.paid_at != None


class Invoice:
    billing_address = None
    shipping_address = None
    order = None

    def __init__(self, attributes={}):
        self.billing_address = attributes.get('billing_address', None)
        self.shipping_address = attributes.get('shipping_address', None)
        self.order = attributes.get('order', None)


class Order:
    customer = None
    items = None
    payment = None
    address = None
    closed_at = None
    
    methods_shipping = {
        "physical": 'backend.shipping.PhysicalShipping',
        "book": 'backend.shipping.BookShipping', 
        "digital": 'backend.shipping.DigitalShipping',
        "membership": 'backend.shipping.MembershipShipping'
    }

    def __init__(self, customer, attributes={}):
        self.customer = customer
        self.items = []
        self.order_item_class = attributes.get('order_item_class', OrderItem)
        self.address = attributes.get('address', Address(zipcode='45678-979'))

    def add_product(self, product):
        self.items.append(self.order_item_class(order=self, product=product))

    def total_amount(self):
        total = 0
        for item in self.items:
            total += item.total()

        return total

    def close(self, closed_at=time.time()):
        self.closed_at = closed_at

    def send_product(self):
        result = OrderedDict()
        for item in self.items:
            product_name = item.product.name
            product_type = item.product.type
        
            factory_class = import_class(
                self.methods_shipping.get(product_type, 'shipping.BaseShipping')
            )    
            obj_class = factory_class(attributes=dict(
                shipping_address=self.address,
                order=self
            ))
            result[product_name] = obj_class.run()
        
        return result
        

class OrderItem:
    order = None
    product = None

    def __init__(self, order, product):
        self.order = order
        self.product = product

    def total(self):
        return 10


class Product:
    # use type to distinguish each kind of product: physical, book, digital, membership, etc.
    name = None
    type = None

    def __init__(self, name, type):
        self.name = name
        self.type = type


class Address:
    zipcode = None

    def __init__(self, zipcode):
        self.zipcode = zipcode


class CreditCard:

    @staticmethod
    def fetch_by_hashed(code):
        return CreditCard()


class Customer:
    name = "Fulano"
    email = "fulano@gmail.com"
    

class Membership:
    customer = None
    
    def __init__(self, customer):
        self.customer = customer

    def send_email_welcome(self):
        return "%s bem vindo a assinatura, qualquer duvida estamos a disposição" % (
            self.customer.name)
            
class Voucher:
    payment = None
    customer = None
    
    def __init__(self, attributes):
        self.payment = attributes.get('payment', None)
        self.customer = attributes.get('customer', None)

    def total(self):
        return 10
        