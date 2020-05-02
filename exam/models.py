from django.db import models


# Create your models here.
from accounts.models import User


class Exam(models.Model):
    examiner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exams')
    name = models.CharField(max_length=64)
    info = models.TextField()
    duration = models.DurationField()

    def __str__(self):
        return self.name


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question = models.TextField()

    def __str__(self):
        return self.question


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option = models.CharField(max_length=8)
    text = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.text


class Test(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    examinee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tests')
    start_time = models.DateTimeField(null=True)

    def __str__(self):
        return "{}: {} {}".format(self.exam.name, self.examinee.first_name, self.examinee.last_name)


class Answer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='answers')
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    answer = models.OneToOneField(Option, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer.text
