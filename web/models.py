from django.db import models
from django.db.models.fields import EmailField
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    btype = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    bgtemplate = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone_number = PhoneNumberField()
    content = models.TextField()
    bimage = models.ImageField(null=True, blank=True, upload_to="bimages")
    date_posted = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ('-date_posted', )

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return str(reverse('post_detail', kwargs={'pk': self.pk}))


