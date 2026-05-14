from django.db import models
from django.conf import settings

class hostel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    warden = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    is_Approved = models.BooleanField(default=False)
    image = models.ImageField(upload_to='hostel_images/', null=True, blank=True)

    def __str__(self):
        return self.name