from django.shortcuts import render, redirect
from .models import Score
import scipy.stats as st
import json
import random

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
    with open('/static/json/everytime.json') as json_file:
        datastore = json.loads(json_file.read())
        for pp in datastore:
            if pp['prof'] == professor and pp['title'] == lecture:
                record.professor_style = pp['details']['학점 비율']
    # professor_style="학점 느님"

    #교수 학점비율에 따라 학점 비율 조정
    for i in range(2):
        if professor_style == '비율채워줌':
            ratio[i] -= 5
        elif professor_style == '매우깐깐함':
            ratio[i] -= 15
        elif professor_style == 'F폭격기':
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
    
    if(first_grade=="B") and (record.expected_grade=="B"): #얘는 A에 도전할 수 있도록 해줍시다.
        expected_grade = "A"
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
def happycircuit(request):
    happy_thinking = request.GET['happythinking']
    ratio = [record.a_ratio, ratio.b_ratio]
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
    return render(request, 'result.html', {'a_ratio':'ratio[0]', 'b_ratio':'ratio[1]'})

def conclusion(request):
    #final_pectentage
    #final_grade
    #rivals_to_win
    #user_content
    record.save()
    return render(request, 'result.html')

def result(request):
    return render(request, 'result.html')

