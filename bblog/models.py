from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # Atributos.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date =  models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    # Metodos.
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    # Convertimos en string lo que queremos mostrar.
    def __str__(self):
        return self.title
