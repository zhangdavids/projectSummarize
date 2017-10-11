
import json

from django.db import models
from django.contrib.auth.models import User
from json_field import JSONField
import numpy as np


# Create your models here.
# 存储注册用户
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    array = JSONField()
    arrayratedmoviesindxs = JSONField()
    name = models.CharField(max_length=1000)
    lastrecs = JSONField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        create = kwargs.pop('create', None)
        recsvec = kwargs.pop('recsvec', None)
        print('create:', create)
        if create:
            super(UserProfile, self).save(*args, **kwargs)
        elif not recsvec:
            self.lastrecs = json.dumps(recsvec.tolist())
            super(UserProfile, self).save(*args, **kwargs)
        else:
            nmovies = MovieData.objects.count()
            array = np.zeros(nmovies)
            ratedmovies = self.ratedmovies.all()
            self.arrayratedmoviesindxs = json.dumps([m.movieindx for m in ratedmovies])
            for m in ratedmovies:
                array[m.movieindx] = m.value
            self.array = json.dumps(array.tolist())
            super(UserProfile, self).save(*args, **kwargs)


# 记录每位用户为哪些电影打过分
class MovieRated(models.Model):
    user = models.ForeignKey(UserProfile, related_name='ratedmovies')
    movie = models.CharField(max_length=100)
    movieindx = models.IntegerField(default=-1)
    value = models.IntegerField()

    def __str__(self):
        return self.movie


# 存储每部电影的相关数据：名称，简介，向量表示（ndim向量的维度）
class MovieData(models.Model):
    title = models.CharField(max_length=100)
    array = JSONField()
    ndim = models.IntegerField(default=300)
    description = models.TextField()

    def __str__(self):
        return self.title
