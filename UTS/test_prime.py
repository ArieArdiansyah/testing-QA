import unittest
from prime import is_prime  

class TestIsPrime(unittest.TestCase):

    def test_negative_numbers(self):
        for i in range(-5, 0):
            with self.subTest(i=i):
                self.assertFalse(is_prime(i))

    def test_less_than_two(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_first_few_primes(self):
        for prime in [2, 3, 5, 7, 11, 13]:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime))

    def test_first_few_non_primes(self):
        for non_prime in [4, 6, 8, 9, 10]:
            with self.subTest(non_prime=non_prime):
                self.assertFalse(is_prime(non_prime))

if __name__ == '__main__':
    unittest.main()
