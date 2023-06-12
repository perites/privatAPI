import requests
import logging
from exceptions import * 



class CalculatorResponse():
	def __init__(self, rate, exchanged_value):
		self.rate = round(rate[0], 4)
		self.exchanged_value = round(exchanged_value,4)
		self.currency = rate[1]


class RateCalculation():
	def calculate_exchanged_value(self,amount_hrn):
		exchanged_value = amount_hrn / self.get_rate()[0]
		return CalculatorResponse(self.get_rate(), exchanged_value)

class PrivatAPI():
	response = None
	def get_privat_api(self):
		response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
		logging.info(f"Getting api")
		if response.status_code == 200:  
			PrivatAPI.response = response
		else:
			raise BadAPIResponse


class UsdAPI(PrivatAPI, RateCalculation):
	def get_rate(self):
		if PrivatAPI.response:
			return [float(PrivatAPI.response.json()[0]["sale"]), "Usd"]
		else:
			self.get_privat_api()
			return [float(PrivatAPI.response.json()[0]["sale"]), "Usd"]
			 
class EuroAPI(RateCalculation):
	def get_rate(self):
		if PrivatAPI.response:
			return [float(PrivatAPI.response.json()[1]["sale"]), "Euro"]
		else:
			self.get_privat_api()
			return [float(PrivatAPI.response.json()[1]["sale"]), "Euro"]

class EthAPI(RateCalculation):
	def get_rate(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
		headers = {'X-CoinAPI-Key' : "8FBF51F8-332B-416E-A836-4603D4B21753"}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return [response.json()["rate"] * UsdAPI().get_rate(), "Eth"]
		else:
			raise BadAPIResponse

		
class BtcAPI(RateCalculation):
	def get_rate(self):
		url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
		headers = {'X-CoinAPI-Key' : "8FBF51F8-332B-416E-A836-4603D4B21753"}
		response = requests.get(url, headers=headers)
		if response.status_code == 200:
			return [response.json()["rate"] * UsdAPI().get_rate(), "Btc"]
		else:
			raise BadAPIResponse






# class PrivatAPI():
# 	def __init__(self):
# 		response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
# 		logging.info(f"Getting api")
# 		if response.status_code == 200:  
# 			self.response = response
# 		else:
# 			raise BadAPIResponse


# class Coin_ETH_API():
# 	def __init__(self):
# 		url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
# 		headers = {'X-CoinAPI-Key' : "8FBF51F8-332B-416E-A836-4603D4B21753"}
# 		response = requests.get(url, headers=headers)
# 		if response.status_code == 200:
# 			self.response = response
# 		else:
# 			raise BadAPIResponse


# class Coin_BTC_API():
# 	def __init__(self):
# 		url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
# 		headers = {'X-CoinAPI-Key' : "8FBF51F8-332B-416E-A836-4603D4B21753"}
# 		response = requests.get(url, headers=headers)
# 		if response.status_code == 200:
# 			self.response = response
# 		else:
# 			raise BadAPIResponse






















		








	


