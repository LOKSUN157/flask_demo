from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "你好，我是你的好哥哥呀！欢迎访问我的 Flask 网站!"

if __name__ == '__main__':
    app.run(debug=True)