from flask install flask
app = Flask(__root1__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __root1__ == '__main__':
    app.run(debug=True)