from flask import Flask
from flask import render_template,request
import json
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/test', methods=['GET'])
def test():
    data = request.args.get("input",None)
    print('接收到的数据：', data)
    return json.dump({'message': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
