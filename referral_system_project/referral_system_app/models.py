from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    referral_code = models.CharField(max_length=100, blank=True, null=True)
    registration_timestamp = models.DateTimeField(auto_now_add=True)

class Referral(models.Model):
    referrer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referrals')
    referred_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='referred_by')
    registration_timestamp = models.DateTimeField(auto_now_add=True)
