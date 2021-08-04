from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifier
    for authentication instead of usernames
    """
    def create_user(self, email, password):
        if email is None:
            raise ValueError('Email must be set')
        if password is None:
            raise ValueError('Password must be set')

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.save()
        return user

    def create_super_user(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user
