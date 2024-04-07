from rest_framework import serializers
from .models import User, Referral

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '_all_'

class ReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referral
        fields = '_all_'