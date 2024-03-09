from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The email field is required.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True, verbose_name="Username")
    email = models.EmailField(max_length=60, unique=True, verbose_name="Email Address")
    employee_number = models.CharField(max_length=50, blank=True, verbose_name="Employee Number")
    first_name = models.CharField(max_length=50, blank=True, verbose_name="First Name")
    middle_name = models.CharField(max_length=50, blank=True, verbose_name="Middle Name")
    last_name = models.CharField(max_length=50, blank=True, verbose_name="Last Name")    
    birth_ddate = models.DateField(verbose_name="Birt Date")
    home_street_address = models.CharField(max_length=255, blank=True, verbose_name="Home Street Address")
    municipality = models.CharField(max_length=50, blank=True, verbose_name="Municipality")
    province = models.CharField(max_length=50, blank=True, verbose_name="Province")    
    contact_number = models.CharField(max_length=11, blank=True, verbose_name="Contact Number")    
    designation = models.CharField(max_length=50, blank=True, verbose_name="Designation")
    company_address = models.CharField(max_length=100, blank=True, verbose_name="Company Address")    
    is_verified = models.BooleanField(default=False, verbose_name="Is Verified")
    is_active = models.BooleanField(default=True, verbose_name="Is Active")
    is_staff = models.BooleanField(default=False, verbose_name="Is Staff")
    is_superuser = models.BooleanField(default=False, verbose_name="Is Superuser")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = AccountManager()
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name="account_set",
        related_query_name="account",
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='User permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="account_set", 
        related_query_name="account",
    )

    def __str__(self):
        return self.username
