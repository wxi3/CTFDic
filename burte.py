import hashlib

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()+-'
admin = '6d0bc1'

for i in range(100000000):

	i = hashlib.md5(str(i).encode('utf-8')).hexdigest()

	if i[0:6] == '6d0bc1':
		print(i) 