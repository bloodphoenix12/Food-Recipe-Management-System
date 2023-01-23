from django.db import  models
from django.core.validators import MinLengthValidator

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=50)

    def registerData(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Contact.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Contact.objects.filter(email = self.email):
            return True

        return  False


