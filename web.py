from http.server import HTTPServer,BaseHTTPRequestHandler

content=""""
<html>
    <title>Laptop Details</title>
<body>
    <table border ="6" cellspacing="10" cellpadding="8">
    <caption> Configuration details of laptop </caption>
<tr>
<th>s.no</th>
<th>Hardware</th>
<th>Specs</th>
</tr>
<tr>
<th>1</th>
<th>Display</th>
<th>LCD display 12.9 inch</th>
</tr>
<tr>
<th>2</th>
<th>Ram</th>
<th>16 GB</th>
</tr>
<tr>
<th>3</th>
<th>rom</th>
<th>1 TB</th>
</tr>
<tr>
<th>4</th>
<th>Processor</th>
<th>Intel i5 13th gen</th>
</tr>
<tr>
<th>5</th>
<th>Graphics card</th>
<th>Nvidia Rtx 1040</th>    
</tr>
</body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()