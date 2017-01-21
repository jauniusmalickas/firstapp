from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return ("hello world from first app")

if __name__ == '__main__':
	app.run(port=5000, debug=True) 
