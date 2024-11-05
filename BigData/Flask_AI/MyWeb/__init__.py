# ------------------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py
# ------------------------------------------------------------------------
# 모듈 로딩 ---------------------------------------------------------------
from flask import Flask

APP = Flask(__name__)

def create_app():
    @APP.route("/go")
    def goHome():
        return APP.redirect("/info")

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
        return render_template("info.html", anme=name)
    #     return f"""
    #     <body style ='background-color:yello; text-align:center'>
    #     <h1>{name} INFORMATUIN</h1>  
    #     HELLO
    #     </body>
    # """

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




if __name__ == "__main__":
    app = create_app()
    app.run()