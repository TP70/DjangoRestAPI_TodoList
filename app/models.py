from django.db import models


class TodoList(models.Model):
    name = models.CharField('name', max_length=50)
    done = models.BooleanField('done', default=False)
    created_at = models.DateTimeField('created_at', auto_now_add=True)  # verify if updated is needed or not
