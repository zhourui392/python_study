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
    print(aa + "_id is " + str(question.id))

    # get
    question = Question.objects.get(id=1)

    # update
    question.question_text = datetime.now().strftime("%H:%M:%S")
    question.save()

    # delete
    question = Question(question_text="10086", pub_date=datetime.now())
    question.save()
    print("10086_id is "+str(question.id))
    question.delete()

    resp = {'errorcode': 100, 'detail': '数据添加成功！'}
    return HttpResponse(json.dumps(resp), content_type="application/json")
