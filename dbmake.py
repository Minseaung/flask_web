import pymysql
db = pymysql.connect(
  host='localhost',
  port = 3306,
  user = 'root',
  password = '1234',
  db = 'busan'
)
sql = '''
  CREATE TABLE `topic` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`title` varchar(100) NOT NULL,
	`body` text NOT NULL,
	`author` varchar(30) NOT NULL,
    `create_date` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (id)
	) ENGINE=innoDB DEFAULT CHARSET=utf8;
'''

#sql_1 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES ('부산', '송도 해수욕장 가고싶다', '김민승');"
#sql_2 = "INSERT INTO `users` (`name`, `email`, `username`, `password`) VALUES ('KIM', 'wws0075@nvaer.com', '김민승', '12345');"
sql_3 = "INSERT INTO `topic` (`title`, `body`, `author`) VALUES (%s, %s, %s);"
cursor = db.cursor()                #커서는 데이터베이스의 정보를 불러오는 연결 메소드. 없으면 안됨!
#title = input('제목을 적으세요')
#body = input("내용을 적으세요")
#author = input("누구세요?")
#input_data = [title, body, author]

# cursor.execute(sql)
# cursor.execute(sql_1)
# cursor.execute(sql_2)
# cursor.execute(sql_3, input_data)

#db.commit()
#db.close()

#cursor.execute('SELECT * FROM users;')
#cursor.execute('SELECT * FROM topic;')
cursor.execute('SELECT * FROM users;')
users = cursor.fetchall()
print(cursor.rowcount, users)