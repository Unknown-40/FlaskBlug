from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

#git init
#git remote add origin address github
