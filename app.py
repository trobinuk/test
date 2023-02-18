from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
	output = 'Risk Assessment Project'
	return output
