from django.contrib.auth.models import User
from django.db import models


class Problem(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.title}: {self.name}'


class Code(models.Model):
    code = models.TextField()
    description = models.TextField()
    problem = models.ForeignKey(Problem, null=True, on_delete=models.SET_NULL)
    handle = models.CharField(max_length=30)
    score = models.IntegerField()

    def __str__(self):
        return f'Code for problem {self.problem} by {self.handle} with score {self.score}'


class Comment(models.Model):
    code = models.ForeignKey(Code, null=False, on_delete=models.CASCADE)
    handle = models.CharField(max_length=30)
