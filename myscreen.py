#!/usr/bin/env python3
"""
vim ~/.config/lxsession/LXDE-pi/autostart 
@/home/pi/raspi-myscreen/start.sh 
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.request, requests, json

class S(BaseHTTPRequestHandler):
    def get_weather(self):
        weather = requests.get('https://api.forecast.io/forecast/' + weather_api)
        weather_today = weather.json()['daily']['data'][0]
        return json.dumps(weather_today)

    def get_subway(self):
        page = urllib.request.urlopen('http://www.mbta.com/stops/place-shmnl')
        times = page.read().decode().split('m-tnm-sidebar__time-number">')
        time1 = times[1].split('</div>')[0]
        time2 = times[2].split('</div>')[0]
        time3 = times[3].split('</div>')[0]
        time4 = times[4].split('</div>')[0]
        return json.dumps({'northbound1':time1, 'northbound2':time2, 
                           'southbound1':time3, 'southbound2':time4})

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    
    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        if (self.path == '/'):
            f = open('/home/pi/raspi-myscreen/index.html', "r")
            self.wfile.write(f.read().encode())
            f.close()
        else:
            self.wfile.write(self.path.encode())

    def do_POST(self):
        if (self.path == '/weather'):
            self.data_string = self.get_weather()
        elif (self.path == '/subway'):
            self.data_string = self.get_subway()
        else:
            self.data_string = self.path

        self.wfile.write(self.data_string.encode())


def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

f = open('/home/pi/raspi-myscreen/weather_api.txt', "r")
weather_api = f.read().strip()
f.close()
print(weather_api)

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()

