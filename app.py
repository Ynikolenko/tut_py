from bottle import Bottle, run

app = Bottle()

@app.route('/')
@app.route('/hello')

def hello():
	return "Hello Youtubers of Archivizers Team!"

run(app, host = '0.0.0.0', port = 8080)
