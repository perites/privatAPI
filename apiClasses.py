import requests
import logging
from exceptions import *


from collections import namedtuple
from getcryptoresponse import *


class CalculatorResponse():
    def __init__(self, rate, exchanged_value):
        self.rate = round(rate.rate, 4)
        self.exchanged_value = round(exchanged_value, 4)
        self.currency = rate.currency


class RateCalculation():
	def __init__(self):
		self.answer = namedtuple("answer", "rate, currency")

	def calculate_exchanged_value(self, amount_hrn):
		exchanged_value = amount_hrn / self.get_rate().rate
		return CalculatorResponse(self.get_rate(), exchanged_value)


class PrivatAPI():
    response = None

    def get_privat_api(self):
        response = requests.get(
            "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5")
        logging.info(f"Getting api for privat")
        if response.status_code == 200:
            PrivatAPI.response = response
        else:
            raise BadAPIResponse


class UsdAPI(PrivatAPI, RateCalculation):
    def get_rate(self):
        if not PrivatAPI.response:
            self.get_privat_api()
        return self.answer(float(PrivatAPI.response.json()[0]["sale"]), "Usd")


class EuroAPI(PrivatAPI, RateCalculation):
    def get_rate(self):
        if not PrivatAPI.response:
            self.get_privat_api()
        return self.answer(float(PrivatAPI.response.json()[1]["sale"]), "Euro")


class CryptoAPI():
	response = None

	def get_crypto_api(self):
		logging.info(f"Getting api for crypto")
		write_response()
		CryptoAPI.response == True


class EthAPI(CryptoAPI, RateCalculation):
	def get_rate(self):
		if not CryptoAPI.response:
			self.get_crypto_api()

		with open("response.json", "r") as answer_file:
			# print(answer)
			return self.answer(json.load(answer_file)[1]["rate"] * UsdAPI().get_rate().rate, "Eth")


class BtcAPI(CryptoAPI, RateCalculation):
	def get_rate(self):
		if not CryptoAPI.response:
			self.get_crypto_api()

		with open("response.json", "r") as answer_file :
			# print(answer)
			return self.answer(json.load(answer_file)[0]["rate"] * UsdAPI().get_rate().rate, "Btc")





    # def get_rate(self):
    # 	logging.info(f"Getting api")
    #     url = 'https://rest.coinapi.io/v1/exchangerate/ETH/USD'
    #     headers = {'X-CoinAPI-Key': "8FBF51F8-332B-416E-A836-4603D4B21753"}
    #     response = requests.get(url, headers=headers)
    #     if response.status_code == 200:
    #         return self.answer(response.json()["rate"] * UsdAPI().get_rate().rate, "Eth")
    #     else:
    #         raise BadAPIResponse


# class BtcAPI(RateCalculation):
#     def get_rate(self):
#     	logging.info(f"Getting api")
#         url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
#         headers = {'X-CoinAPI-Key': "8FBF51F8-332B-416E-A836-4603D4B21753"}
#         response = requests.get(url, headers=headers)
#         if response.status_code == 200:
#             return self.answer(response.json()["rate"] * UsdAPI().get_rate().rate, "Btc")
#         else:
#             raise BadAPIResponse







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






















		








	


