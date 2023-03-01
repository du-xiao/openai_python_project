from flask import Flask,request,render_template,url_for
from flask_cors import CORS
import os
import openai
app = Flask(__name__)
CORS(app,supports_credentials=True)

@app.route('/testVue')
def testVue():
        return render_template('testVue.html')

@app.route('/question')
def question():
	return render_template('question.html')

@app.route('/')
def hello_world():
	text='helloword world!!'
	return text

@app.route('/callChatGPT',methods=['GET','POST'])
def callChatGPT():
	input = request.args.get('input')
	openai.api_key = "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"
	#openai.api_key = os.getenv("OPENAI_API_KEY")
	response =  openai.Completion.create(model="text-davinci-003",prompt=input,temperature=0.5,max_tokens=500,frequency_penalty=0.0,presence_penalty=0.0)
	return response.choices[0].text
@app.route('/createPic',methods=['GET','POST'])
def createPic():
        input = request.args.get('input')
        openai.api_key = "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"
        #openai.api_key = os.getenv("OPENAI_API_KEY")
        #response =  openai.Completion.create(model="text-davinci-003",prompt=input,temperature=0.5,max_tokens=500,frequency_penalty=0.0,presence_penalty=0.0)
        response = openai.Image.create( prompt=input,n=1,size="1024x1024")
        image_url = response['data'][0]['url']
        return image_url

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=50000,debug=True)
