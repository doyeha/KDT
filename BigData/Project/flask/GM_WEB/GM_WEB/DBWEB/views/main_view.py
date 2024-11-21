# --------------------------------------------------------
# Flask FrameWork 에서 모듈단위 URL 처리 ㅊ파일
# - 파일명 : main_view.py
# --------------------------------------------------------
# 모듈 로딩
from flask import Blueprint, render_template, request   # ★request 추가됨
from DBWEB.models.models import *

# Blueprint 인스턴스 생성
mainBP = Blueprint('main_view',
                   import_name=__name__,
                   url_prefix="/",
                   template_folder="templates")


# http://localhost:8080/ URL 처리 라우팅 함수 정의

@mainBP.route("/")  # 새놈 되는 중
def index():    
    # data = NF_Preds.query.first() # NF_Preds에서 처음 나오는 값 현재 결과값은  <NF_Preds 2024-10-25>
    return render_template('index.html')


@mainBP.route("/NF", methods=['GET', 'POST'])
def NFindex():
    all_data = NF_Preds.query.all()   # 모든 데이터.
    # print(all_data[0].Date , type(all_data[0].Date))
    nf_filtered_data = None  # 초기화
    if request.method == 'POST':
        selected_date = request.form['date']  # 선택한 날짜
        # print(selected_date, type(selected_date))
        # 선택한 날짜에 해당하는 데이터 필터링
        nf_filtered_data = [data for data in all_data if data.Date == selected_date]
        
    return render_template("NF.html", all_data=all_data, filtered_data=nf_filtered_data)



from datetime import datetime 
from bs4 import Comment
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from DBWEB import DB
# from DBWEB import Question, Answer

from DBWEB.models.models import Gold_Comment

@mainBP.route("/Gold", methods=['GET', 'POST'])
def Goldindex():
    all_data = Gold_Preds.query.all()   # 모든 데이터.
    # print(all_data)   # 데이터 확인
    # print("all_data : ",all_data[0].Date, type(all_data[0].Date))
    gold_filtered_data = None  # 초기화
    if request.method == 'POST':
        selected_date = request.form['date']  # 선택한 날짜
        # selected_date = str(selected_date)
        # 선택한 날짜에 해당하는 데이터 필터링
        # 
        print("selected_date : ", selected_date , type(selected_date))
        selected_date = str(selected_date)
        print("selected_date : ", selected_date , type(selected_date))
        gold_filtered_data = [data for data in all_data if str(data.Date) == selected_date]

    # comments부분
    all_comment = Gold_Comment.query.all()
    
    if request.method == 'POST':
        comment = request.form['comment']
        answer = Gold_Comment(comment=comment, Date = datetime.now())
        DB.session.add(answer)
        DB.session.commit()

    
    comments = [c for c in all_comment]
    print(comments)


    return render_template("Gold.html", all_data=all_data, filtered_data=gold_filtered_data, comments=comments)





@mainBP.route("/GG", methods=['GET', 'POST'])
def GGindex():
    all_data = GG_Preds.query.all()   # 모든 데이터.
    gg_filtered_data = None  # 초기화
    if request.method == 'POST':
        selected_date = request.form['date']  # 선택한 날짜
        # 선택한 날짜에 해당하는 데이터 필터링
        gg_filtered_data = [data for data in all_data if str(data.Date) == selected_date]
    return render_template("GG.html", all_data=all_data, filtered_data=gg_filtered_data)



@mainBP.route("/AP", methods=['GET', 'POST'])
def APindex():
    all_data = AP_Preds.query.all()   # 모든 데이터.
    ap_filtered_data = None  # 초기화
    
    if request.method == 'POST':
        selected_date = request.form['date']  # 선택한 날짜
        # 선택한 날짜에 해당하는 데이터 필터링
        ap_filtered_data = [data for data in all_data if str(data.Date) == selected_date]
    return render_template("AP.html", all_data=all_data, filtered_data=ap_filtered_data)

# "/qdetail/<int:qid>"

# @mainBP.route("/qlist")
# def printlist():
#     q_list = .query.all()
#     return render_template("question_list.html", question_list=q_list)

# @mainBP.route("/qdetail/<int:qid>")
# def questionItem(qid):
#     ## DB에서 조회한 1개의 question 인스턴스를 전달
#     q = Question.query.get(qid)
#     return render_template("question_detail.html",question=q)