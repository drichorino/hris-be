# Generated by Django 5.0.3 on 2024-03-09 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='Email Address')),
                ('employee_number', models.CharField(blank=True, max_length=50, verbose_name='Employee Number')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='First Name')),
                ('middle_name', models.CharField(blank=True, max_length=50, verbose_name='Middle Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Last Name')),
                ('birth_ddate', models.DateField(verbose_name='Birt Date')),
                ('home_street_address', models.CharField(blank=True, max_length=255, verbose_name='Home Street Address')),
                ('municipality', models.CharField(blank=True, max_length=50, verbose_name='Municipality')),
                ('province', models.CharField(blank=True, max_length=50, verbose_name='Province')),
                ('contact_number', models.CharField(blank=True, max_length=11, verbose_name='Contact Number')),
                ('designation', models.CharField(blank=True, max_length=50, verbose_name='Designation')),
                ('company_address', models.CharField(blank=True, max_length=100, verbose_name='Company Address')),
                ('is_verified', models.BooleanField(default=False, verbose_name='Is Verified')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Is Staff')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Is Superuser')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='account_set', related_query_name='account', to='auth.group', verbose_name='Groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='account_set', related_query_name='account', to='auth.permission', verbose_name='User permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
