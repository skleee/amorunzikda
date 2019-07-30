from django.shortcuts import render, redirect
from .models import Score

# Create your views here.
def home(request):
    scores = Score.objects
    return render(request,'home.html',{'scores':scores})

def create(request):
    record = Score()
    record.nickname = request.GET['nickname']
    record.expected_grade = request.GET['expected_grade']
    record.lecture="testttt" #일단. 크롤링해온 것에서 찾는 함수 필요
    record.professor="dtttt" #일단
    record.lecture_type = request.GET['lecture_type']
    record.my_score = request.GET['my_score']
    record.class_average = request.GET['class_average']
    record.class_sd = request.GET['class_sd']
    record.class_total = request.GET['class_total']
    record.mid_ratio = request.GET['mid_ratio']
    record.final_ratio = request.GET['final_ratio']
  
    #함수 추가 필요
    record.first_grade = "A"
    record.first_percentage = 40

    record.save()
    return render(request,'nowgrade.html')