from django.db import models


class BlogEntries(models.Model):
    entry_text = models.TextField(max_length=500)
    date_published = models.DateTimeField('date published')
