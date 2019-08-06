from django.shortcuts import render, redirect
from .models import Score

subjectratio = {
    '국제어': [50, 90],
    '전공핵심': [30, 65],
    '전공일반': [40, 75],
    '기타교양': [30, 65]
}

def home(request):
    scores = Score.objects
    return render(request,'home.html',{'scores':scores})

def create(request):
    record = Score()
    record.nickname = request.GET['nickname']
    record.expected_grade = request.GET['expected_grade']
    record.lecture_professor="dtttt" #일단
    lecture_type_ = request.GET['lecture_type']
    record.lecture_type = lecture_type_
    record.class_total = request.GET['class_total']
    record.mid_ratio = request.GET['mid_ratio']
    record.final_ratio = request.GET['final_ratio']
    my_score = request.GET['my_score']
    class_average = request.GET['class_average']
    class_sd = request.GET['class_sd']
    
    ratio_ = subjectratio[lecture_type_]

    #교수 학점비율에 따라 학점 비율 조정
    professor_style = '학점느님' #json에서 찾아오기
    for i in range(2):
        if professortype == '비율채워줌':
            ratio[i] -= 5
        elif professortype == '매우깐깐함':
            ratio[i] -= 15
        elif professortype == 'F폭격기':
            ratio[i] -= 25
        else:
            continue
    record.ratio = ratio_

    #Zvalue 구하기
    zscore = (my_score - class_average)/class_sd


    #함수 추가 필요
    record.first_grade = "A"
    record.first_percentage = 40

    #final_pectentage
    #final_grade
    #rivals_to_win
    #user_pw
    #user_content
    record.save()
    return render(request,'nowgrade.html')

def nowgrade(request):
    return render(request, 'nowgrade.html',{'first_grade':'A'}) #'A'는 앞 페이지에서 받아올 학점 