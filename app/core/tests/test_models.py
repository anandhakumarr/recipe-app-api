from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating new user with email is sucessful"""
        email = 'test@datamattic.com'
        password = 'testpass123'

        user = get_user_model().objects.create_user(email, password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Testing User email normalized"""
        email = 'test@DATAMATTIC.COM'
        user = get_user_model().objects.create_user(email, 'password')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Testing invalid email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'password')
            get_user_model().objects.create_user(None, 'password')

    def test_create_new_super_user(self):
        """Creating new super user """
        user = get_user_model().objects.create_superuser(
            'test@datamattic.com',
            'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
