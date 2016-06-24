#!/usr/bin/env python
import hashlib

pass0 = raw_input('Enter Password: ')
pass0_hash= hashlib.sha1(pass0).hexdigest()

login = raw_input('Enter login specific info: ')
login_hash = hashlib.sha1(login).hexdigest()

iteration = raw_input('Enter number of iterations or press return for default (1): ') or '1'
i = int(iteration)

# You could add another input:
#comment = raw_input('Enter comment: ')
#comment_hash = hashlib.md5(comment).hexdigest()

login_pass_hash = pass0_hash + login_hash #+ comment_hash

def sha_iteration(i):
	sha_hash = hashlib.sha256(login_pass_hash).hexdigest()
	while i >1: 
		sha_hash = hashlib.sha256(sha_hash).hexdigest()
		i=i-1		
	return sha_hash

sha_login_pass = sha_iteration(i)


def better_pass(sha_login_pass):
	characters = """~!@#$%^&*_-+=`|\(){}[]:;"'<>,.?/"""
	pass1 = sha_login_pass.title()
	location_str = ''.join(x for x in sha_login_pass if x.isdigit())
	choice_str = ''.join(x for x in sha_login_pass if x.isdigit())

	loc_0 = int(location_str[0])  #First  location
	loc_1 = int(location_str[1])
	loc_2 = int(location_str[2])
	loc_3 = int(location_str[3])
	loc_4 = int(location_str[4])
	loc_5 = int(location_str[5])
	loc_6 = int(location_str[6])
	loc_7 = int(location_str[7])
	loc_8 = int(location_str[8])
	loc_9 = int(location_str[9])
	loc_list = [loc_0, loc_1, loc_2, loc_3, (loc_4 + 10), (loc_5 + 10), (loc_6 + 10), (loc_7 + 20),  (loc_8 + 20),  (loc_9 + 20)]
	loc_list.sort() # Sorts the list nurmerically from least to greatest
	#print loc_list

	choice_0 = int(location_str[0])  #First choice
	char_0 = characters[choice_0]
	choice_1 = int(location_str[1])
	char_1 = characters[choice_1]
	choice_2 = int(location_str[2])
	char_2 = characters[choice_2]
	choice_3 = int(location_str[3])
	char_3 = characters[choice_3]
	choice_4 = int(location_str[4])
	char_4 = characters[choice_4]
	choice_5 = int(location_str[5])
	char_5 = characters[choice_5]
	choice_6 = int(location_str[6])
	char_6 = characters[choice_6]
	choice_7 = int(location_str[7])
	char_7 = characters[choice_7]
	choice_8 = int(location_str[8])
	char_8 = characters[choice_8]
	choice_9 = int(location_str[9])
	char_9 = characters[choice_9]

	pass_0 = pass1[0:loc_list[0]] + char_0
	pass_1 = pass1[loc_list[0]:loc_list[1]] + char_1 
	pass_2 = pass1[loc_list[1]:loc_list[2]] + char_2 
	pass_3 = pass1[loc_list[2]:loc_list[3]] + char_3 
	pass_4 = pass1[loc_list[3]:loc_list[4]] + char_4 
	pass_5 = pass1[loc_list[4]:loc_list[5]] + char_5
	pass_6 = pass1[loc_list[5]:loc_list[6]] + char_6
	pass_7 = pass1[loc_list[6]:loc_list[7]] + char_7
	pass_8 = pass1[loc_list[7]:loc_list[8]] + char_8
	pass_9 = pass1[loc_list[8]:loc_list[9]] + char_9
	pass_end = pass1[loc_list[9]:]  
	pass2 = pass_0 + pass_1 + pass_2 + pass_3 + pass_4 + pass_5 + pass_6 + pass_7 +pass_8 +pass_9 + pass_end
	return pass2


print better_pass(sha_login_pass)
