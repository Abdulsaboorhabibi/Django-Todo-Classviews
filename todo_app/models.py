from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    doc = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Todo"
        verbose_name_plural = "Todos"
