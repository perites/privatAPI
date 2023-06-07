
import requests
from exceptions import * 


def get_exchanges_rates():

	response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
	if response.status_code == 200:
		exchange_rates = {"dollar" : float(response.json()[0]["sale"]), 
							"euro" : float(response.json()[1]["sale"])}
		return exchange_rates

	else:
		raise BadAPIResponse

def calculate_exchanged_money(amount_money):
	exchange_rates = get_exchanges_rates()
	answer = {"exchange_rates" : {"dollar" : exchange_rates["dollar"] ,"euro" : exchange_rates["euro"]}, 
				"exchanged_money" : {"exchanged_in_dollar" : round(amount_money / exchange_rates["dollar"], 2), 
										"exchanged_in_euro" : round(amount_money / exchange_rates["euro"], 2)}}

	return answer




