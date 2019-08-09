from django.shortcuts import render, redirect
from .models import Score
import scipy.stats as st
import json
import random
import os

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
    record.lecture_professor= request.GET['lecture']
    lecture_type_ = request.GET['lecture_type']
    record.lecture_type = lecture_type_
    record.class_total = request.GET['class_total']
    record.mid_ratio = request.GET['mid_ratio']
    record.final_ratio = request.GET['final_ratio']
    my_score = request.GET['my_score']
    class_average = request.GET['class_average']
    class_sd = request.GET['class_sd']
    
    ratio = subjectratio[lecture_type_]
    lectureandprofessor = (record.lecture_professor).split(' - ')
    
    #교수 학점 비율 가져오기
    lecture = lectureandprofessor[0]
    professor = lectureandprofessor[1]
    # '/static/json/everytime.json'
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, './static/json/everytime.json')
    with open(file_path,'r', encoding='utf-8') as json_file:
        datastore = json.load(json_file)
        for pp in datastore:
            if pp['prof'] == professor and pp['title'] == lecture:
                record.professor_style = pp['details']['학점 비율']
    # professor_style="학점 느님"

    #교수 학점비율에 따라 학점 비율 조정
    for i in range(2):
        if record.professor_style == '비율채워줌':
            ratio[i] -= 5
        elif record.professor_style == '매우깐깐함':
            ratio[i] -= 15
        elif record.professor_style == 'F폭격기':
            ratio[i] -= 25
        else:
            continue
    record.a_ratio = ratio[0]
    record.b_ratio = ratio[1]

    #Zvalue 구해서 상위 비율 구하기
    zscore = (float(my_score) - float(class_average))/float(class_sd)
    pvalue = st.norm.cdf(zscore)
    if zscore == 0:
        first_percentage = 50
    else:
        first_percentage = (1-pvalue)*100
    first_percentage = float('%.2f' % round(first_percentage, 2))
    
    #현재 학점 구하기
    if int(first_percentage) < ratio[0]:
        first_grade = "A"
    elif int(first_percentage) < ratio[1]:
        first_grade = "B"
    else:
        first_grade = "C"
    
    record.first_grade = first_grade
    record.first_percentage = first_percentage
    
    if(record.first_grade=="B") and (record.expected_grade=="B"): #얘는 A에 도전할 수 있도록 해줍시다.
        record.expected_grade = "A"
    record.save()
    return render(request, 'nowgrade.html', {'nowgrade':first_grade})

def nowgrade(request, record):
    first_grade = record.first_grade
    comment_A = ['이런 기만자!!!','아니 이 누추한 곳에 귀하신 분이...']
    comment_B = ['有B無患: B만 있으면 걱정이 없다 했거늘...','나B야~ 나B야~','C 아닌게 어디야!']
    comment_C = ['이번 학기 가C밭 길만 걷자', 'C그널 보내 C그널 보내']
    comment_DF = ['ㅋㅋㅋㅋㅋㅋㅋ','삐빅- 재수강입니다.']
    if first_grade == "A":
        comment = random.choice(comment_A)
    elif first_grade == "B":
        comment = random.choice(comment_B)
    elif first_grade == "C":
        comment = random.choice(comment_C)
    else:
        comment = random.choice(comment_DF)
    return render(request, 'nowgrade.html',{'first_grade':first_grade, 'comment':comment})

def happy(request):
    return render(request, 'happy.html')

#행복회로로 A, B 비율 조정
def happycircuit(request, record):
    happy_thinking = request.GET['happythinking']
    ratio = [record.a_ratio, record.b_ratio]
    for i in range(2):
        if happy_thinking<20:
            ratio[i] -= 10
        elif happy_thinking<40:
            ratio[i] -= 5
        elif happy_thinking<50:
            ratio[i] -= 1
        elif happy_thinking<60:
            ratio[i] += 1
        elif happy_thinking<80:
            ratio[i] += 5
        else :
            ratio[i] += 10
    return render(request, 'result.html', {'a_ratio':ratio[0], 'b_ratio':ratio[1]})

def conclusion(request, record):
    record2=Submit()
    lecture_professor = record.lecture_professor
    nickname = record.nickname
    a2_ratio = record.a_ratio
    b2_ratio = record.b_ratio
    first_percentage = record.first_percentage
    expected_grade = record.expected_grade
    class_total = record.class_total
    mid_ratio = record.mid_ratio
    final_ratio = record.final_ratio
    
    if expected_grade == "A":
        record2.final_percentage = 2*a2_ratio + (mid_ratio*(2*a2_ratio-first_percentage))/final_ratio
    
    if expected_grade == "B":
        record2.final_percentage = 2*b2_ratio + (mid_ratio*(2*b2_ratio-first_percentage))/final_ratio
    
    record2.rivals_to_win = (first_percentage - record2.final_percentage)*class_total/100
    record2.save()
    return render(request, 'result.html', {'nickname':nickname, 'lecture_professor':lecture_professor, 'expected_grade':expected_grade, 'final_percentage':record2.final_percentage, 'livals_to_win':record2.livals_to_win})

def result(request):
    return render(request, 'result.html')

