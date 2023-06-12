import requests
import logging
from exceptions import * 


class RateCalculation():

	def get_rate(self):
		raise NotImplementedError 

	def calculate_exchanged_money(self,amount_hrn ):
		currency_rate = self.get_rate()
		logging.info(f"Getting api")
		exchanged_money = amount_hrn / currency_rate
		return exchanged_money


class UsdAPI(RateCalculation):
	def get_rate(self):
		response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
		if response.status_code == 200:  
			return round(float(response.json()[0]["sale"]),4)
		else:
			raise BadAPIResponse

class EuroAPI(RateCalculation):
	def get_rate(self):
		response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
		if response.status_code == 200:
			return round(float(response.json()[1]["sale"]), 4)

		else:
			raise BadAPIResponse


class EthAPI(RateCalculation):
	def get_rate(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
		headers = {'X-CoinAPI-Key' : '8FBF51F8-332B-416E-A836-4603D4B21753'}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return round(response.json()["rate"] * UsdAPI().get_rate(),4)
		else:
			raise BadAPIResponse


class BtcAPI(RateCalculation):
	def get_rate(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
		headers = {'X-CoinAPI-Key' : '8FBF51F8-332B-416E-A836-4603D4B21753'}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return round(response.json()["rate"] * UsdAPI().get_rate(),4)
		else:
			raise BadAPIResponse





	


