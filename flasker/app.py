from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
	#templates/index.htmlを使用する
	#message という変数に"hello"を代入する
	return render_template('index.html', message='hello')

@app.route("/input")
def input():
	return render_template('input.html', message='INPUT')

@app.route("/output", methods=["GET", "POST"])
def output():
	if request.method == "POST":
		word = request.form["word"]
		return render_template("output.html", word=word)
	else:
		return redirect(url_for("input"))

if __name__ == "__main__":
	app.run()
