from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"


from mode_admin import admin

app.register_blueprint(admin)




#git init
#git remote add origin address github
#  pip3 freeze > requirements.txt
#  git config --global user.email "mansourosmani4050mnr@gmail.com"
#  git config --global user.name "Unknown-21-m"
#  git -m commit "Initialize Project"
#  git push --set-upstream origin master
#  git push


# to add a file and update
# git add filename
# git commit -m "Update filename"
# git push
