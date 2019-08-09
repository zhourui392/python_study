from django.http import HttpResponse
from polls.models import Question
from datetime import datetime, date
import json


# 数据库操作
def testdb(request):
    if request.method == "POST":
        print("Post")
    elif request.method == "GET":
        print("Get")
        aa = request.GET["aa"]
        question = Question(question_text=aa, pub_date=datetime.now())
        question.save()
    question = Question.objects.get(id=1)
    print(question.question_text)
    resp = {'errorcode': 100, 'detail': '数据添加成功！'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
