from django.db import models
from django.contrib.auth.models import AbstractUser

# Özel Kullanıcı -- settings özelleştirme
class User(AbstractUser):
    pass 


# Temsilci
class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # lead = models.ForeignKey("Lead", on_delete=CASCADE)
    def __str__(self):
        return self.user.username


class Lead(models.Model):
    
    # SOURCE_CHOICES = (
    #     ('YouTube', 'YouTube'),    
    #     ('Google', 'Google'),    
    #     ('Newsletter', 'Newsletter'),    
    # )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    # phoned = models.BooleanField(default=False)
    # source = models.CharField(choices=SOURCE_CHOICES, max_length=100)

    # profil_picture = models.ImageField(blank=True, null=True)
    # spacial_files = models.FileField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
