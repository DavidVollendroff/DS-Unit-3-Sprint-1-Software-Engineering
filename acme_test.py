import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealsplosion(self):
        """Tests stealability and explosiveness"""
        prod = Product('Highly desirable explosive', price=1000, flammability=1000)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...BABOOM!!")


class AcmeReportTests(unittest.TestCase):
    """Testing our reports for ACMEness"""
    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        products = generate_products()
        for product in products:
            split_name = product.name.split(' ', 1)
            self.assertIn(split_name[0], ADJECTIVES)
            self.assertIn(split_name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
