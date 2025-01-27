from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where mobile_number is the unique identifier
    for authentication instead of username.
    """

    def create_user(self, mobile_number, password, **extra_fields):
        """
        Create and save a user with the given mobile number and password.
        """
        if not mobile_number:
            raise ValueError(_("The Mobile number must be set"))
        user = self.model(mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile_number, password, **extra_fields):
        """
        Create and save a superuser with the given mobile number and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(mobile_number, password, **extra_fields)
