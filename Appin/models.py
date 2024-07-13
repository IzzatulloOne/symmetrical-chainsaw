from django.db import models


class Hobby(models.Model):
    title = models.CharField(max_length = 25)
    deteil = models.TextField()
    image = models.ImageField(upload_to = 'hobby/')
    
    def __str__(self):
        return self.title


class About_Me(models.Model):
    title = models.CharField(max_length = 25)
    deteil = models.TextField()
    image = models.ImageField(upload_to = 'about-me/') 

    def __str__(self):
        return self.title


class Blog_adventure(models.Model):
    title = models.CharField(max_length=50)
    deteil = models.TextField()
    image_for_adbenture = models.ImageField(upload_to = 'adventure-blog/')

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length = 60)
    deteil = models.TextField()
    image = models.ImageField(upload_to = 'article-blog/')

    def __str__(self):
        return self.title