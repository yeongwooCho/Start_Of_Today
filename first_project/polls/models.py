from django.db import models

# Create your models here.


class Video(models.Model):
    objects = models.Manager()
    num = models.CharField(max_length=10)
    title = models.TextField()
    views = models.TextField()
    url = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'DB_Video'
        verbose_name = "오늘의 영상"
        verbose_name_plural = '오늘의 영상'
