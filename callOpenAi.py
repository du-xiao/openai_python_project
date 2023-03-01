from flask import Flask, request, render_template, url_for,jsonify
from flask_cors import CORS
import os
import openai
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/testVue')
def testVue():
    return render_template('testVue.html')


@app.route('/question')
def question():
    return render_template('question.html')


@app.route('/')
def hello_world():
    text = 'helloword world!!'
    return text


@app.route('/callChatGPT', methods=['GET', 'POST'])
def callChatGPT():
    input = request.args.get('input')
    # 加载环境变量配置文件
    load_dotenv('.env')
    # 获取环境变量的值
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    response = openai.Completion.create(model="text-davinci-003", prompt=input, temperature=0.5, max_tokens=500,
                                        frequency_penalty=0.0, presence_penalty=0.0)
    return response.choices[0].text


@app.route('/createPic', methods=['GET', 'POST'])
def createPic():
    data = request.json
    input = data['input']
    #openai.api_key = "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"
    # 加载环境变量配置文件
    load_dotenv('.env')
    # 获取环境变量的值
    openai.api_key = os.environ.get('OPENAI_API_KEY')
    # response =  openai.Completion.create(model="text-davinci-003",prompt=input,temperature=0.5,max_tokens=500,frequency_penalty=0.0,presence_penalty=0.0)
    response = openai.Image.create(prompt=input, n=1, size="1024x1024")
    image_url = response['data'][0]['url']
    response_data = {'image_url':image_url}
    return jsonify(response_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=50000, debug=True)
