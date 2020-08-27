from django.db import models

# Create your models here.


class Board(models.Model):
    objects = models.Manager()
    num = models.CharField(max_length=10)
    title = models.TextField()
    rate = models.CharField(max_length=20)
    link = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'DB_board'
        verbose_name = "오늘의 게시글"
        verbose_name_plural = '오늘의 게시글'
