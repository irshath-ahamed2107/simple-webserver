# EX01 Developing a Simple Webserver
## Date:28.10.2024

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:

from http.server import HTTPServer,BaseHTTPRequestHandler

content=
```
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
```

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



## OUTPUT:
![alt text](<Web App Lab Exp code.jpg>)

![alt text](<FWAD Lab Exp1.png>)


## RESULT:
The program for implementing simple webserver is executed successfully.
