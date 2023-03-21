from django.db import models

class SchoolNews(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    text = models.TextField()

    class Meta:
        verbose_name_plural = 'SchoolNews'

    def __str__(self):
        return self.title
        return self.author
        return self.date
        return self.text

