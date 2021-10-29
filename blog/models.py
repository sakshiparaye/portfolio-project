from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

