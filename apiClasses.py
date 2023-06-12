import requests
import logging
from exceptions import * 


class RateCalculation():
	def calculate_exchanged_value(self,amount_hrn):
		exchanged_value = amount_hrn / self.rate[0]
		return CalculatorResponse(self.rate, exchanged_value)


class PrivatAPI():
	def __init__(self):
		response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
		logging.info(f"Getting api")
		if response.status_code == 200:  
			self.response = response
		else:
			raise BadAPIResponse


class Coin_ETH_API():
	def __init__(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
		headers = {'X-CoinAPI-Key' : "8FBF51F8-332B-416E-A836-4603D4B21753"}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			self.response = response
		else:
			raise BadAPIResponse


class Coin_BTC_API():
	def __init__(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
		headers = {'X-CoinAPI-Key' : "8FBF51F8-332B-416E-A836-4603D4B21753"}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			self.response = response
		else:
			raise BadAPIResponse



class UsdAPI(RateCalculation):
	def __init__(self, response):
		self.rate =  [float(response.json()[0]["sale"]), "Usd"]
			 
class EuroAPI(RateCalculation):
	def __init__(self, response):
		self.rate = [float(response.json()[1]["sale"]), "Euro"]

class EthAPI(RateCalculation):
	def __init__(self, response):
		self.rate = [response.json()["rate"] * UsdAPI().get_rate(), "Eth"]

class BtcAPI(RateCalculation):
	def __init__(self, response):
		self.rate = [response.json()["rate"] * UsdAPI().get_rate(), "Btc"]




class CalculatorResponse():
	def __init__(self, rate, exchanged_value):
		self.rate = round(rate[0], 4)
		self.exchanged_value = round(exchanged_value,4)
		self.currency = rate[1]











		








	


