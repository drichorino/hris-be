from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import Account

class AccountSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs.pop('confirm_password'):
            raise serializers.ValidationError({"confirm_password": "Password fields didn't match."})
        
        # Hash the password before saving
        attrs['password'] = make_password(attrs['password'])
        return attrs

    def create(self, validated_data):
        # Use AccountManager's create_user method to handle user creation
        return Account.objects.create_user(**validated_data)
