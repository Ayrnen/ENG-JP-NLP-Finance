import requests

class Requester(object):
    @ staticmethod
    def Request(url, header=None):
        try:
            response = requests.get(url, headers=header)
            response.raise_for_status()  # This will raise an HTTPError if the response was an HTTP error status
            print("Successfully retrieved data:")
            return response
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Error:", err)