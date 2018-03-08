from django.db import models

# Create your models here.

class Data(models.Model):
    inputName = models.CharField(max_length=200)
    inputEmail = models.EmailField()
    inputTel = models.IntegerField()
    submitTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.inputName