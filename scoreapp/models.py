from django.db import models

# Create your models here.
class Score(models.Model):
    nickname = models.CharField(max_length=20)
    expected_grade = models.CharField(max_length=3)
    lecture = models.CharField(max_length=50)
    professor = models.CharField(max_length=15)
    lecture_type = models.IntegerField()
    my_score = models.FloatField()
    class_sd = models.FloatField()
    class_average = models.FloatField()
    class_total = models.IntegerField()
    mid_ratio = models.FloatField(default=50)
    final_ratio = models.FloatField(default=50)

    first_grade = models.CharField(max_length=5)
    first_percentage = models.FloatField()
    
    def __str__(self):
        return self.nickname
# user_id:string
# user_content:string

# professor_style:string