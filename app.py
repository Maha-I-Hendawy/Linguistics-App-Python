from text import Text
from flask import Flask, render_template, request, url_for, redirect


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		text = request.form['text']
		txt = Text(text)
		words = txt.words()
		sentences = text.sentences()
		return redirect(request.url)
	return render_template("home.html", words=words, sentences=sentences)




txt = Text("this is a sentence. this is another sentence, and that's another sentence")

print(txt) 

txt.words()

txt.sentences()