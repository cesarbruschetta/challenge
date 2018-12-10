""" process to make sales of customer """

import sys
import os
sys.path.append(os.path.abspath('../'))

from backend.bootstrap import Customer, Order, Product, Payment, CreditCard


def make_sale(product_name, product_type, credi_card):
    """ method to create new sale """

    foolano = Customer()
    product = Product(name=product_name, type=product_type)
    product_order = Order(foolano)
    product_order.add_product(product)
    
    attributes = dict(
        order=product_order,
        payment_method=CreditCard.fetch_by_hashed(credi_card)
    )
    
    payment_order = Payment(attributes=attributes)
    payment_order.pay()
    print(payment_order.is_paid())  # < true
    
    send_product = product_order.send_product()
    for name, mensagem in send_product.items():
        print("%s = %s" % (name, mensagem))
        print(30 * "--")
    