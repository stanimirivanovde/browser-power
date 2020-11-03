from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

# Simple HTTP server that serves over HTTPS
# Make sure that key.pem and cert.pem are generated.
# You can use the ./generate-certs.sh script provided in this repo.

class web_server(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path = '/encrypt-file.html'
		try:
			#Reading the file
			file_to_open = open(self.path[1:]).read()
			self.send_response(200)
		except:
			file_to_open = "File not found"
			self.send_response(404)
		
		self.end_headers()
		self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('192.168.93.122', 4443), web_server)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile="./key.pem",
        certfile='./cert.pem', server_side=True)

httpd.serve_forever()