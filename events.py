from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('event_admin.html')

@app.route('/event', methods=['POST', 'GET'])
def event():
	print 'test'
	if request.method == 'POST':
		return 'Hello world'
	else:
		pass


if __name__ == '__main__':
    app.run('0.0.0.0', 8888)