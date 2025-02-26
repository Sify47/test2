from flask import Flask , render_template
# import psycopg2
# conn = psycopg2.connect(host = "localhost" , user="postgres" , port="5432" , password="01141117352" , dbname="test")
# cur = conn.cursor()
# cur.execute('SELECT * FROM users ')
# val = cur.fetchall()
# print(val)
app = Flask(__name__)

orders = [{
    'FullName' : "Mohamed",
    'Phone' : '01141117352' ,
    'Price' : '400'
}]

@app.route("/")
def hello():
    return render_template('home.html' , orders=orders)

@app.route("/login")
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run()