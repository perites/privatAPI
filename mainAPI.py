import time
import logging 

from flask import Flask , render_template , request , redirect , url_for
from forms import DateForm



from apiClasses import *
from exceptions import * 



logging.basicConfig(format='%(levelname)s: %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',  filename='currencyAPI_logs.log', filemode='w', level=logging.DEBUG)

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
		logging.info(f"Got {amount_money} money ")		

		value_in_usd = UsdAPI()#(amount_money)
		value_in_euro = EuroAPI()#(amount_money)
		value_in_eth = EthAPI()#(amount_money)
		value_in_btc = BtcAPI()#(amount_money)
		answer = []

		for v in (value_in_usd, value_in_euro, value_in_eth, value_in_btc):
			list1 = []
			list1.append(v.get_rate())
			list1.append(v.calculate_exchanged_money(amount_money))
			answer.append(list1)



		logging.info(f"Got resolts :  {answer} , now render index_post.html ")
		return render_template("index_post.html" ,currentTime = currentTime , answer = answer)


	except BadAPIResponse as ex:
		logging.error("Exception occurred", exc_info=True)
		return ex.html()

	except ValueError as ex:
		logging.error("Exception occurred", exc_info=True)
		return render_template("index_post_error.html" ,message = "Сумма введена некоректно")










if __name__ == '__main__':
    app.run(debug=True)