from flask import Flask,jsonify

app = Flask(__name__)

@app.route('/')

#app.route("/result",methods=["POST","GET"])

def apiTesting():
	output = 'Risk Assessment Project'
	return output
