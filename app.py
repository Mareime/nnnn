from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'hello evry one d'
if __name__ == '__main__':
    # app.logger.info("message")
    app.run(host='0.0.0.0',port=5000)