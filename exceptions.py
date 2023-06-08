from flask import Flask , render_template

import logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',  filename='privatAPI_logs.log', filemode='w', level=logging.DEBUG)



class BadAPIResponse(Exception):
    def html(self):
    	return render_template("index_post_error.html" ,message = "Bad API response, please try later")





