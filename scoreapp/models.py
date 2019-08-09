from django.db import models

# Create your models here.
class Score(models.Model):
    nickname = models.CharField(max_length=20)
    expected_grade = models.CharField(max_length=3)
    lecture_professor = models.CharField(max_length=50)
    professor_style = models.CharField(max_length=8)
    lecture_type = models.CharField(max_length=5)
    a_ratio = models.IntegerField()
    b_ratio = models.IntegerField()
    class_total = models.IntegerField()
    mid_ratio = models.FloatField(default=50)
    final_ratio = models.FloatField(default=50)
    first_grade = models.CharField(max_length=5)
    first_percentage = models.FloatField()
    def __str__(self):
        return self.nickname

class Happy(models.Model):
    final_percentage = models.FloatField()
    first = models.ForeignKey('Score', on_delete=models.CASCADE)
    a_ratio2 = models.IntegerField()
    b_ratio2 = models.IntegerField()
    happythinking = models.FloatField()
    def __str__(self):
        return self.nickname

class Submit(models.Model):
    first = models.ForeignKey('Score', on_delete=models.CASCADE)
    second = models.ForeignKey('Happy', on_delete=models.CASCADE)
    final_grade = models.CharField(max_length=5)
    rivals_to_win = models.IntegerField()
    user_content = models.CharField(max_length=100, default=" ")

    def __str__(self):
        return self.nickname