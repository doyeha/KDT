# 모듈 로딩 
from DBWEB import DB

class NF_Preds(DB.Model):
    __tablename__ = 'nf_preds'
    Date = DB.Column(DB.Date, primary_key=True)
    predicted = DB.Column(DB.Float, nullable=False)

# AP_Preds 테이블 모델 정의
class AP_Preds(DB.Model):
    __tablename__ = 'ap_reds'
    Date = DB.Column(DB.Date, primary_key=True)
    predicted = DB.Column(DB.Float, nullable=False)

# Gold_Preds 테이블 모델 정의
class Gold_Preds(DB.Model):
    __tablename__ = 'gold_preds'
    Date = DB.Column(DB.Date, primary_key=True)
    predicted = DB.Column(DB.Float, nullable=False)

# GG_Preds 테이블 모델 정의
class GG_Preds(DB.Model):
    __tablename__ = 'gg_Preds'
    Date = DB.Column(DB.Date, primary_key=True)
    predicted = DB.Column(DB.Float, nullable=False)



class NF_Comments(DB.Model):
    __tablename__ = 'nf_Comments'
    Date = DB.Column(DB.Date, primary_key=True)
    comment = DB.Column(DB.String(50), nullable=False)

# AP_Preds 테이블 모델 정의
class AP_Comments(DB.Model):
    __tablename__ = 'ap_Comments'
    Date = DB.Column(DB.Date, primary_key=True)
    comment = DB.Column(DB.String(50), nullable=False)

# Gold_Preds 테이블 모델 정의
class Gold_Comments(DB.Model):
    __tablename__ = 'gold_comments'
    Date = DB.Column(DB.Date, primary_key=True)
    comment = DB.Column(DB.String(50), nullable=False)

# GG_Preds 테이블 모델 정의
class GG_Comments(DB.Model):
    __tablename__ = 'gg_comments'
    Date = DB.Column(DB.Date, primary_key=True)
    comment = DB.Column(DB.String(50), nullable=False)


# import pymysql

# db = pymysql.connect(host="172.20.60.119", user="member4", password="1234", db="webdb", charset="utf8")

# cursor = db.cursor()

# sql = "select * from netflix"

# cursor.execute(sql)

# cursor.fetchall()
# cursor.fetchone()
# # cursor.fetchall(100)

# db.commit()

# db.close()