from django.db import models

# About Model

class About(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"

# Service Model 

class Service(models.Model):
    name = models.CharField(max_length=100,verbose_name="Service name")
    description = models.TextField(verbose_name="About service")
    image = models.ImageField(upload_to="services")

    def __str__(self):
        return self.name

# Recent Work Model

class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Work title")
    short_description = models.TextField()
    image = models.ImageField(upload_to="works")
    image_url = models.URLField()

    def __str__(self):
        return self.title

# Client Model

class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name