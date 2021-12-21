'''

def hello(request):
    print("Handling request to home page.")
    return HttpResponse("Hello, Arvinder!")
'''

pip install flask

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<html><body><h1>AZ 104 Exam Preparation!</h1></body></html>\n"
