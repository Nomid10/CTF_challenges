# Challenge from HackerDom training 

import hashlib
import itertools
import string


sha_1 = '6ddc3c39fbe045ad9712232e48c4c9a6c4053a0a'

for d in map(''.join, itertools.product(string.digits, repeat=8)):
	if hashlib.sha1(d.encode()).hexdigest() == sha_1:
		print(d)

