# bbc data preprocessor

import os

def main():
	ser_file = open(os.getcwd() + '/bbc.txt', encoding='utf-8', errors='ignore')
	ser_out = open(os.getcwd() + '/clean_bbc.txt', 'w+')
	clean_files(ser_file, ser_out, 'serious')
	
def clean_files(in_file, out_file, tag):
	for line in in_file:
		x = tag + ' '
		x += line
		out_file.write(x)

if __name__ == '__main__':
	main()
