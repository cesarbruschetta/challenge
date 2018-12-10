
from backend.bootstrap import Membership, Voucher


class BaseShipping:
    shipping_address = None
    order = None

    def __init__(self, attributes={}):
        self.shipping_address = attributes.get('shipping_address', None)
        self.order = attributes.get('order', None)

    def run(self):
        return "Type Not implementad, contact the support"


class PhysicalShipping(BaseShipping):

    def print_shipping_label(self):
        return "shipping label of Product"

    def run(self):
        return self.print_shipping_label()


class BookShipping(BaseShipping):
    
    def print_shipping_label_book(self):
        return "shipping label of Product \n '** Item isento de impostos conforme disposto na Constituição Art. 150, VI, d **'"

    def run(self):
        return self.print_shipping_label_book()
    
    
class DigitalShipping(BaseShipping):
    voucher = None

    def send_desciption_order(self):
        return "Descrição da compra: %s \n\
    Obrigado pela Compra, e como agradecimento vc ganhou um voucher de R$%s \n\
    Basta fazer uma nova compra com seu e-mail e seu cartão de credito" % (
        self.order.items[0].product.name, self.voucher.total())

    def run(self):
        attributes = dict(
            customer=self.order.customer,
            payment=self.order.payment
        )
        
        self.voucher = Voucher(attributes=attributes)
        return self.send_desciption_order()
        
    
class MembershipShipping(BaseShipping):

    def run(self):
        sub = Membership(customer=self.order.customer)
        return sub.send_email_welcome()
        