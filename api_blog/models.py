from django.contrib.auth.models import User
from django.db import models


# modelo de dados
class Phrases(models.Model):
    # titulo
    title = models.CharField(max_length=255)
    # conteúdo
    content = models.TextField()
    # id do usuario pertencente
    user_id = models.IntegerField()
    # hora de criação
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        # Ordernar por id dos usuários
        ordering = ['user_id']
        verbose_name = 'Phrase'
        verbose_name_plural = 'Phrases'

    def __str__(self):
        return self.title
