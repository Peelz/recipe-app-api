from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_creat_user_with_email_successful(self):
        """Test Creating a new User"""
        email = "monopeelz@gmai.com"
        password = "123123"
        user = get_user_model().objects.create_user(
            email,
            password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'monopeelz@GMAIL.COM'
        user = get_user_model().objects.create_user(email, '123123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123123')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            'monopeelz@gmail.com',
            '123123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
