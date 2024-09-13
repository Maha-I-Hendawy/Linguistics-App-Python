from text import Text
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '311e3b5283ce0f3fc7fdb5e772db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lang.db'
app.config['SQLALCHEMY_DATABASE_TRACK_MODIFICATION'] = False


db = SQLAlchemy(app)
app.app_context().push()

class TEXT(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)

	def __str__(self):
		return f"{self.text}"


@app.route('/', methods=['GET', 'POST'])
def home():
	txt = TEXT.query.all()
	if request.method == 'POST':
		text = request.form['text']
		txt = TEXT(text=text)
		db.session.add(txt)
		db.session.commit()
		return redirect(request.url)
	else:
		db.session.query(TEXT).delete()
		db.session.commit()
	return render_template("home.html", txt=txt)




