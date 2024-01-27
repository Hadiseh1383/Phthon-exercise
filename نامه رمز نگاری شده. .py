def decode_string(encoded_string):
	encoded_list = encoded_string.split()
	encoded_list.sort(key=lambda x: int(x[1:]))
	for i in encoded_list:
		print(i[0],end='')
input_string = input()
decode_string(input_string)