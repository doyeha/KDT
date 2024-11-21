from datetime import datetime 
from bs4 import Comment
from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from DBWEB import DB
# from DBWEB import Question, Answer

from DBWEB.models.models import Gold_Comment

bp = Blueprint('answer', __name__, url_prefix="/answer")

@bp.route('/create', methods=('POST',))
def create(comments):
    # DB에 업로드
    comment = request.form['comment']
    answer = Gold_Comment(comment=comment, Date = datetime.now())
    DB.session.add(answer)
    DB.session.commit()
    
    # 모든 데이터 담기
    comments = Gold_Comment.query.all()
    print(comments)
    # comments = [c for c in comments.comment]
    # for c in comments.comment:
    #     print(c)
    
    return render_template('Gold.html', comments=comments)

