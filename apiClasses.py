import requests
from exceptions import * 


class RateCalculation():
	def __init__(self, amount_hrn):
		self.amount_hrn = amount_hrn


	def calculate_exchanged_money(self):
		currency_rate = self.get_rate()
		exchanged_money = self.amount_hrn / currency_rate
		answer = exchanged_money
		return answer


class usdAPI(RateCalculation):
	def get_rate(self):
		response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
		if response.status_code == 200:
			exchange_rates =  float(response.json()[0]["sale"])
			return exchange_rates
		else:
			raise BadAPIResponse

class euroAPI(RateCalculation):
	def get_rate(self):
		response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
		if response.status_code == 200:
			exchange_rates =  float(response.json()[1]["sale"])
			return exchange_rates
		else:
			raise BadAPIResponse


class ethAPI(RateCalculation):
	def get_rate(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
		headers = {'X-CoinAPI-Key' : '8FBF51F8-332B-416E-A836-4603D4B21753'}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			exchange_rates = response.json()["rate"] * usdAPI(0).get_rate()
			return exchange_rates
		else:
			raise BadAPIResponse


class btcAPI(RateCalculation):
	def get_rate(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
		headers = {'X-CoinAPI-Key' : '8FBF51F8-332B-416E-A836-4603D4B21753'}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			exchange_rates = response.json()["rate"] * usdAPI(0).get_rate()
			return exchange_rates
		else:
			raise BadAPIResponse





	


