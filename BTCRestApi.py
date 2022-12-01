import os
import subprocess
import time

try:
    import requests
except Exception:
    print("Please run 'pip install requests' in terminal to install necessary dependencies.")
    exit(1)


class EPRestApi:
    _ep_location = ''
    #Starter for the EP executable
    def __init__(self, rest_port, ep_location, version, lic=''):
        self._PORT_ = str(rest_port)
        self._ep_location = ep_location
        self.definitively_closed = False
        if not self.is_rest_service_available():
            ml_port = 29300 + (rest_port % 100)
            if ml_port == rest_port:
                ml_port -= 100
            else:
                return
        while not self.is_rest_service_available():
            time.sleep(2)
            print('.', end='')
        print('\nBTC EmbeddedPlatform has started.')

    # closes the application
    def close_application(self):
        print('Exiting EP... please wait while we save your data.')
        request = requests.delete(self._url('/application'))
        print(request.text)
        print("Data saved!")
        self.definitively_closed = True

    def __del__(self):
        # might already be closed. not our problem.
        if not self.definitively_closed:
            try: 
                self.close_application()
            except:
                pass

    # Performs a get request on the given url extension
    def get_req(self, urlappendix):
        if not 'progress' in urlappendix:
            # print this unless it's a progress query (to avoid flooding the console)
            print('Fetching from: '+ self._url(urlappendix))
        response = requests.get(self._url(urlappendix))
        if not response.ok:
            raise Exception("Error during request GET {}: {}".format(urlappendix, response.text))
        return self.check_long_running(response)

    # Performs a post request on the given url extension. The optional requestBody contains the information necessary for the request
    def post_req(self, urlappendix, requestBody=None):
        print('Posting to: ' +  self._url(urlappendix))
        if requestBody == None:
            response = requests.post(self._url(urlappendix))
        else:
            response = requests.post(self._url(urlappendix),json=requestBody)
        if not response.ok:
            raise Exception("Error during request POST {}: {}".format(urlappendix, response.text))
        return self.check_long_running(response)

    # Performs a post request on the given url extension. The optional requestBody contains the information necessary for the request
    def put_req(self, urlappendix, requestBody=None):
        print('Posting to: ' +  self._url(urlappendix))
        if requestBody == None:
            response = requests.put(self._url(urlappendix))
        else:
            response = requests.put(self._url(urlappendix),json=requestBody)
        if not response.ok:
            raise Exception("Error during request PUT {}: {}".format(urlappendix, response.text))
        return self.check_long_running(response)

    # Checks if the REST Server is available
    def is_rest_service_available(self):
        try:
            response = requests.get(self._url('/test'))
        except requests.exceptions.ConnectionError:
            return False
        return response.ok

    # URL appender
    def _url(self, path):
        return self._ep_location + self._PORT_ + '/ep/' + path.lstrip("/")

    # This method is used to poll a request until the progress is done.
    def check_long_running(self, response):
        if response.status_code == 202:
            print('Long running task started:')
            jsonResponse = response.json()
            for key, value in jsonResponse.items():
                if key == 'jobID':
                    #t = 0
                    while response.status_code == 202:
                        time.sleep(3)
                        #t += 2
                        #print('... {} s elapsed'.format(t))
                        print('.', end='')
                        response = self.poll_long_running(value)
                    print('')
            print('Task completed!')
        return response

    def poll_long_running(self, jobID):
        response = requests.get(self._url('/progress/' + jobID))
        if not response.ok:
            raise Exception("Error during request GET {}: {}".format( response.text))
        return response
