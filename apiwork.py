
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






def get_crypto_exchanges_rates():
	url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
	headers = {'X-CoinAPI-Key' : '8FBF51F8-332B-416E-A836-4603D4B21753'}
	response = requests.get(url, headers=headers)

	exchange_rates = {"Ethereum" : response.json()["rate"]}

	return exchange_rates


def calculate_exchanged_money_cryto(amount_money):
	exchange_rates = get_crypto_exchanges_rates()
	answer = {"exchange_rates_crypto" : {"Ethereum" : exchange_rates["Ethereum"]},
				"exchanged_crypto" : {"exchanged_in_crupto" : round(amount_money / exchange_rates["Ethereum"], 2)}}


	return answer


# class BaseAPI():
# 	def __init__(self):
# 		pass

# 	def calculate_exchanged_money(self):
# 		pass

		
