import time
from flask import Flask , render_template , request , redirect , url_for
from forms import DateForm

from apiwork import *
from exceptions import * 

app = Flask(__name__)
app.config["SECRET_KEY"] = 'c42e8d7a0a1003456342385cb9e30b6b'


@app.route("/" , methods = ["GET"])
def home_get():
	currentTime = time.localtime()
	currentTime = time.strftime("%m.%d.%Y %H:%M " , currentTime )
	form = DateForm()
	return render_template("index_get.html" ,currentTime = currentTime , form=form)

@app.route("/" , methods = ["POST"])
def home_post():
	currentTime = time.localtime()
	currentTime = time.strftime("%m.%d.%Y %H:%M " , currentTime )

	amount_money = request.form.get("amount_money")

	try:
		amount_money = float(amount_money)
		answer = calculate_exchanged_money(amount_money)
		return render_template("index_post.html" ,currentTime = currentTime , answer = answer) 

	except BadAPIResponse as ex:
		return render_template("index_post_error.html" ,message = ex)

	except ValueError as ex:
		return render_template("index_post_error.html" ,message = "Сумма введена некоректно")









if __name__ == '__main__':
    app.run(debug=True)