import subprocess
from flask import Flask, render_template, request, redirect, url_for
import json

from janome.tokenizer import Tokenizer

import os

t = Tokenizer()

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
		#word = request.form["word"]
		#json_linesの読み込み
		word = request.form["word"]
		print(word)

		# 入力された値を形態素解析する
		for token in t.tokenize(word):
			print(token)
			#ここに形態素された値とキーワードの一致を確認するコードを記述する

		# ファイルを一度削除することで検索結果が重なることを防いでいる
		if os.path.exists('./python_scraping2/pydocTest.jl'):
			os.remove('./python_scraping2/pydocTest.jl')

		if not os.path.exists('./python_scraping2/pydocTest.jl'):
			open('./python_scraping2/pydocTest.jl', "w")

		subprocess.check_output(["scrapy", "crawl", "-a", "categories=" + word, "pydoc", "-o", "pydocTest.jl"], cwd="./python_scraping2")
		items = []
		with open('./python_scraping2/pydocTest.jl', 'r') as f:
		    for line in f:
		        items.append(json.loads(line))
		return render_template("output.html", word=request.form["word"], items=items)
	else:
		return redirect(url_for("input"))

if __name__ == "__main__":
	app.run()
