# Challenge from HackerDom Training


import hashlib

alplhabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
md5 = ''
dictionary_of_hash = {}
for i in alplhabet:
	md5 = hashlib.md5(i.encode()).hexdigest()
	dictionary_of_hash[md5] = i

with open('hexstrings.txt') as inf:
	for i in inf:
		i = i.strip()
		if i in dictionary_of_hash.keys(): 
			print(dictionary_of_hash.get(i), end='')


