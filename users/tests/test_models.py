from django.test import TestCase

from users.models import User, Farmer, EquipmentOwner
from users import utils


class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.admin_user_data = {
            'username': 'admin',
            'email': 'admin@example.com',
            'password': 'pass@12345'
        }

        cls.normal_user = {
            'phone_number': '0700000000'
        }

    def test_superuser_creation(self):
        user = User.objects.create_superuser(**self.admin_user_data)

        self.assertEqual(user.username, self.admin_user_data['username'])
        self.assertEqual(user.email, self.admin_user_data['email'])
        self.assertTrue(user.check_password(self.admin_user_data['password']))
        self.assertIsNone(user.phone_number)
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertIsNone(user.user_type)

    def test_user_creation(self):
        user = User.objects.create_user(**self.normal_user)
        formatted_phone_number = utils.get_international_phone_number_format(self.normal_user['phone_number'])

        self.assertEqual(user.username, formatted_phone_number)
        self.assertEqual(user.phone_number, formatted_phone_number)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertIsNone(user.user_type)

    def test_user_creation_with_invalid_phone_number_input(self):
        with self.assertRaisesMessage(ValueError, 'A valid phone number must be set'):
            User.objects.create_user(phone_number='')

        with self.assertRaisesMessage(ValueError, 'A valid phone number must be set'):
            User.objects.create_user(phone_number='xyz')

    def test_superuser_creation_without_username(self):
        with self.assertRaisesMessage(TypeError,
                                      "create_superuser() missing 1 required positional argument: 'username'"):
            User.objects.create_superuser(email='admin@example.com', password='pass@12345')

        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_superuser(username=None, email='admin@example.com', password='pass@12345')

    def test_user_model_str_representation(self):
        normal_user = User.objects.create_user(**self.normal_user)
        admin_user = User.objects.create_superuser(**self.admin_user_data)

        expected_normal_repr = utils.get_international_phone_number_format(self.normal_user['phone_number'])

        self.assertEqual(str(normal_user), expected_normal_repr)
        self.assertEqual(str(admin_user), self.admin_user_data['email'])

    def test_model_soft_delete(self):
        user = User.objects.create_user(**self.normal_user)

        # delete user
        user.soft_delete()

        # test user still exists but with the deleted is set to True
        formatted_phone_number = utils.get_international_phone_number_format(self.normal_user['phone_number'])

        self.assertEqual(user.username, formatted_phone_number)
        self.assertEqual(user.phone_number, formatted_phone_number)
        self.assertTrue(user.is_deleted)


class FarmerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.farmer = {
            'phone_number': '0700000000'
        }

    def test_farmer_user_type_creation(self):
        user = Farmer.objects.create_user(**self.farmer)

        formatted_phone_number = utils.get_international_phone_number_format(self.farmer['phone_number'])

        self.assertEqual(user.username, formatted_phone_number)
        self.assertEqual(user.phone_number, formatted_phone_number)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        # test user type
        self.assertIs(user.user_type, User.UserTypes.FARMER)


class EquipmentOwnerModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.owner = {
            'phone_number': '0700000000'
        }

    def test_farmer_user_type_creation(self):
        user = EquipmentOwner.objects.create_user(**self.owner)

        formatted_phone_number = utils.get_international_phone_number_format(self.owner['phone_number'])

        self.assertEqual(user.username, formatted_phone_number)
        self.assertEqual(user.phone_number, formatted_phone_number)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        # test user type
        self.assertIs(user.user_type, User.UserTypes.EQUIP_OWNER)


