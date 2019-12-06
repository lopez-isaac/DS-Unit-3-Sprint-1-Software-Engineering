import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    """
    test default for Subclass
    """
    def test_subclass_default(self):
        prod = BoxingGlove("Mike_Tyson")
        self.assertEqual(prod.price,10)

    """
    test stealability and explode method
    """
    def Test_it_all(self):
        prod = Product("Some_toy")
        self.assertEqual(prod.explode,"...it's a glove.")
        self.assertEqual(prod.stealability,"kinda stealable")

class AcmeReportsTest(unittest.TestCase):

    def test_default_num_products(self):
        pass

    def test_legal_names(self):
        pass



if __name__ == '__main__':
    unittest.main()
