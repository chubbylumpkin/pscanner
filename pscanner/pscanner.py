import requests

url = "http://" + input("Enter IP: ") + ":"

port = int(input("\nStarting port: "))

endPort = int(input("\nEnding port: "))

while port < endPort:

    combinedURL = url + str(port)

    print(combinedURL)

    try:
        r = requests.get(combinedURL, timeout=.1)
        print(r.status_code)
        if r.status_code:
            port = endPort
    except Exception:
        print("")
    
    port += 1

print("Program terminated")


