''' test to script '''

import unittest
import sys, os
sys.path.append(os.path.abspath('../'))


from backend.process import make_sale


class TestMakeSalesMethod(unittest.TestCase):

    def setUp(self):
        """ """
        
        self.credi_card = '43567890-987654367'
        
    def test_product_book(self):
        """ test of the book product """
        
        make_sale('Awesome book', 'book', self.credi_card)
        self.assertIn(
            "Item isento de impostos conforme disposto na Constituição Art. 150, VI, d",
            sys.stdout.getvalue().strip())

    def test_product_digital(self):
        """ test of the digital product """
        
        make_sale('Awesome music', 'digital', self.credi_card)
        self.assertIn(
            "Descrição da compra: Awesome music",
            sys.stdout.getvalue().strip())

    def test_product_membership(self):
        """ test of the membership product """
        
        make_sale('Awesome subscription', 'membership', self.credi_card)
        self.assertIn(
            "Awesome subscription = Fulano bem vindo a assinatura",
            sys.stdout.getvalue().strip())

    def test_product_physical(self):
        """ test of the physical product """
        
        make_sale('Awesome product', 'physical', self.credi_card)
        self.assertIn(
            "Awesome product = shipping label of Product",
            sys.stdout.getvalue().strip())

    def test_error_product(self):
        """ test of the product wich type not exist """
        
        make_sale('New type product', 'newType', self.credi_card)
        self.assertIn(
            "Type Not implementad, contact the support",
            sys.stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main(module=__name__, buffer=True)
