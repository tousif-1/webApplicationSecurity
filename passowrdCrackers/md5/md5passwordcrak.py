'''
This program verifies the MD5 hash given, by converting list of passwords to md5

'''

import hashlib


flag = 0     # flag to check if password is found
counter = 0  # Location of password in the list or number of times loop is run


# Get the md5 Has
pass_hash = input("Enter md5 hash: ")


# Get the wordlist to compare the md5values
wordlist = input("Enter filename: ")


try:
	pass_file = open(wordlist, "r")
except:
	print ("No File Found")
	quit()

for word in pass_file:

	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	print (digest)
	counter += 1
	if digest == pass_hash:
		print ("Password Found: ")
		
		print ( pass_hash + ":" + word)
		flag = 1
		print ("Location of Password in the list: " + str(counter))
		break
	
if flag == 0:
	print ("Passphrase not in List")

