# flask 프레임워크 로드 
from flask import Flask, render_template, request
import pandas as pd

## Flask class 생성 
## Flask()는 생성자 함수에 인자 값을 필수 항목 
## 파일의 이름 
## 현재 파일의 이름은 __name__ 
app = Flask(__name__)

## 웹 서버의 기본 주소 localhost:8080

#네비게이터 
## '/' -> localhost:8080/ 로 요청이 들어왔을 때 
## 바로 아래의 함수로 연결 (함수를 호출)
@app.route('/')
def index():
    #return "Hello World"
    return render_template('a.html')

@app.route('/second')
def second(): 
    return 'secound page'
## 리스트,딕셔너리 등을 입력하면 OPEN API가 된다. 

@app.route('/third')
def third(): 
    return render_template('third.html')

@app.route('/corona')
def corona():
    # 유저가 보낸 servicekey를 변수에 저장 
    # 데이터를 보내는 방식은 get
    ServiceKey = request.args['ServiceKey']
    print(request.args)
    # 유저가 보낸 서비스키가 일치한다면 데이터를 보낸다. 
    if ServiceKey == 'aaa': 
        df = pd.read_csv('corona.csv', index_col = 0)
        # 필요한 컬럼만 추출 
        df = df[['stateDt', 'deathCnt','decideCnt']]
        # 컬럼의 이름을 변경 
        df.columns = ['기준일','총사망자','총확진자']
        # 데이터프레임을 딕셔너리로 변경 
        result = df.to_dict()
        return result 


    # 일치하지 않는다면 데이터를 보내지 않는다. 
    else : 
        return 'ServiceKey Error'

## Flas class 안에 있는 내장함수 run() 호출 
# host 매개변수 : 해당 웹 접근이 가능한 아이피들을 지정 
# port 매개변수 : 웹서버에 접근할 수 있는 port 번호를 지정 
# debug 매개변수 : 개발자 모드로 웹 서버를 오픈할 것인가 
app.run(port = 8080, debug = True)