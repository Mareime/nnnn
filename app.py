from flask import Flask
# just commentaire23
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello word*2'
if __name__ == '__main__':
    # app.logger.info("message")
    app.run(host='0.0.0.0',port=5000)