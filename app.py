from flask import Flask , render_template #이 메소드는 python을 html 문서로 변환시켜서 요청하는 매체에게 보내준다
from data import Articles

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
    #return "Hello World"
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/articles') #사이트 뒤에 /공간 을 지정해주는 것
def articles():
    articles = Articles() #Articles()는 data.py에서 받아옴! 그 함수를 변수로 지정해주는 정보지정.
    # print(articles[0]['title'])
    return render_template("articles.html", articles = articles) #articles.html = 공간. 사이트가 이동했을 때 존재하는 공간, 즉 바구니를 지정해줌. 변수 = articles는 위에서 지정한 정보를 입력해주는 용도. 없으면 안됨!

@app.route('/article/<int:id>')
def article(id):
    articles = Articles()
    article = articles[id-1] #딕셔너리에서 가장 첫 값은 0인데 지정으로 불러오면 1이 되기 때문에 0을 만들기 위해 -1을 붙여줌
    print(articles[id-1])
    return render_template("article.html", article = article)

if __name__ == '__main__':
    app.run()