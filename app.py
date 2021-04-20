from flask import Flask , render_template, request, redirect #이 메소드는 python을 html 문서로 변환시켜서 요청하는 매체에게 보내준다
from data import Articles
import pymysql

app = Flask(__name__)

app.debug = True

db = pymysql.connect(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db = 'busan'
)



@app.route('/', methods=['GET'])
def index():
    #return "Hello World"
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/articles') #사이트 뒤에 /공간 을 지정해주는 것
def articles():
    cursor = db.cursor()
    sql = 'SELECT * FROM topic;'
    cursor.execute(sql)
    topics = cursor.fetchall()
    print(topics)
    #articles = Articles() #Articles()는 data.py에서 받아옴! 그 함수(정보)를 변수로 지정해주는 정보지정.
    # print(articles[0]['title'])
    return render_template("articles.html", articles = topics) #articles.html = 공간. 사이트가 이동했을 때 존재하는 공간, 즉 바구니. 변수 = articles는 위에서 지정한 정보를 입력해주는 용도. 없으면 안됨!

@app.route('/article/<int:id>')
def article(id):
    cursor = db.cursor()
    sql = 'SELECT * FROM topic WHERE id={}'.format(id)
    cursor.execute(sql)
    topic = cursor.fetchone()
    print(topic)
    #articles = Articles()
    #article = articles[id-1] #딕셔너리에서 가장 첫 값은 0인데 지정으로 불러오면 1이 되기 때문에 0을 만들기 위해 -1을 붙여줌
    #print(articles[id-1])
    return render_template("article.html", article = topic)

@app.route('/add_articles', methods=["GET", "POST"])
def add_articles():
    cursor = db.cursor()
    if request.method=="POST":
        desc = request.form['desc']
        title = request.form['title']
        author = request.form['author']

        sql = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
        input_data = [title, desc, author]
        print(request.form['author'], request.form['title'], request.form['desc']) #request.form을 입력해서 프롬프트를 확인했을 때, 딕셔너리 형태로 나오는 것을 알 수 있다. 그 때문에 변수에 딕셔너리의 키 값을 뽑아내는 것.
        
        cursor.execute(sql, input_data)
        db.commit()
        print(cursor.rowcount)
        #db.close()
        return redirect("/articles")
    #return "<h1>글쓰기 페이지</h1>"

    else:
        return render_template("add_articles.html")

@app.route('/delete/<int:id>', methods=["POST"])
def delete(id):
    cursor = db.cursor()
    sql = 'DELETE FROM topic WHERE id = %s;'
    id = [id]
    #혹은 sql = 'DELETE FROM topic WHERE id = {};'.format(id)
    #cursor.execute(sql)
    cursor.execute(sql, id)
    db.commit()

    return redirect("/articles")


if __name__ == '__main__':
    app.run()