from flask import Flask , render_template #이 메소드는 python을 html 문서로 변환시켜서 요청하는 매체에게 보내준다
from data import Articles

app = Flask(__name__)

app.debug = True

@app.route('/', methods=['GET'])
def index():
    #return "Hello World"
    return render_template("index.html", data = 'KIM')

@app.route('/about')
def about():
    return render_template("about.html", hello = "Gary Kim")

@app.route('/articles')
def articles():
    articles = Articles()
    print(articles[0]['title'])
    return render_template("articles.html", articles = articles)

if __name__ == '__main__':
    app.run()