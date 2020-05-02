from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from accounts.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    serializer for User Registration
    """
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )
    # password_confirm = serializers.CharField(
    #     style={'input_type': 'password'}, write_only=True
    # )

    # def validate_password(self, password):
    #     print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
    #     print(self.data)
    #     print('>>>>>>>>>>>>>>>>>>>>>>>>>>')
    #     if password is not self.password_confirm:
    #         raise serializers.ValidationError("Passwords must match")
    #     return password

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_examiner',
            'is_examinee',
            'password',
            # 'password_confirm'
        )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data.get('password'))
        return validated_data
