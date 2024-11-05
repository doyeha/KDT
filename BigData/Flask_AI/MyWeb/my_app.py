# ------------------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py
# ------------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
from flask import Flask

# 전역 변수 ----------------------------------------------------------------
# Flask Web Server 인스턴스 생성
APP = Flask(__name__)

# 라우팅 기능 함수 -----------------------------------------------------------
# @Flask Web Server 인스턴스 변수명.route("URL")
# http://127.0.0.1:5000
@APP.route("/")
def index():
    return render_template("index.html")
    # return """
    # <body style ='background-color:skyblue;'>
    #         <h1>HELLO</h1>
    #         </body>
    #         """

# http://127.0.0.1:5000/info
@APP.route("/info")
@APP.route("/info/")    # 둘다 아래 def를 따르게 된다. 
def info():
    return """
    <body style ='background-color:yello; text-align:center'>
            <h1>INFRORMATION</h1>
            </body>
            """


# http://127.0.0.1:5000/info/name=홍길동
@APP.route("/info/<name>")
def print_info(name):
    return f"""
    <body style ='background-color:yello; text-align:center'>
    <h1>{name} INFORMATUIN</h1>  
    HELLO
    </body>
"""

# http://127.0.0.1:5000/info/정수
@APP.route("/info/<name>")
def checkAge(age):
    return f"""
    <body style ='background-color:lightpink; text-align:center'>
    <h1> skdl:{age}
    HELLO
    </body>
"""

# http://127.0.0.1:5000/go
@APP.route("/info/<name>")
def gohome(age):
    return APP.redirect("/")


# 조건부 실행
if __name__ == '__main__':
    # Flask Web Server 구동
    APP.run()


