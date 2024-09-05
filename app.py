from flask import Flask, request, render_template, make_response, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dapp.html')
    
if __name__ == '__main__':
    app.run("0.0.0.0",8080)

