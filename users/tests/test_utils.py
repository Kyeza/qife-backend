from django.test import TestCase

from users import utils


class TestUtils(TestCase):

    def test_none_phone_number_input(self):

        # empty string input
        empty_str = utils.get_international_phone_number_format('')

        # invalid phone number string
        invalid_str = utils.get_international_phone_number_format('xyz')

        expected = None

        self.assertIsNone(empty_str, msg=f'Expected: {expected}\nGot: {empty_str}')
        self.assertIsNone(invalid_str, msg=f'Expected: {expected}\nGot: {invalid_str}')

    def test_valid_phone_number_input(self):

        valid_str_1 = utils.get_international_phone_number_format('0784668858')
        valid_str_2 = utils.get_international_phone_number_format('256784668858')
        valid_str_3 = utils.get_international_phone_number_format('+256784668858')

        expected = '+256784668858'

        self.assertEqual(valid_str_1, expected, msg=f'Expected: {expected}\nGot: {valid_str_1}')
        self.assertEqual(valid_str_2, expected, msg=f'Expected: {expected}\nGot: {valid_str_2}')
        self.assertEqual(valid_str_3, expected, msg=f'Expected: {expected}\nGot: {valid_str_3}')
