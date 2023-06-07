class BadAPIResponse(Exception):
    def __str__(self):
        return "Bad API response, please try later"