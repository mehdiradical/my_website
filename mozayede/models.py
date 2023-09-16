from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  #2023-09-13 21:08:05.135289
                                                        #2023-09-13 21:10:49.153755

    def __str__(self):
        return "Name Of Your Contact is : {}".format(self.name)     
                                          
    class Meta:
        verbose_name = "مخاطب"
        verbose_name_plural = "مخاطبین"