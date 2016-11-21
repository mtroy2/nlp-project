import os

def main():
	sarc_file = open(os.getcwd() + '/Data/sarcasm.txt')
	ser_file = open(os.getcwd() + '/Data/serious.txt')
	sarc_out = open(os.getcwd() + '/Data/clean_sarcasm.txt', 'w+')
	ser_out = open(os.getcwd() + '/Data/clean_serious.txt', 'w+')
	clean_files(sarc_file, sarc_out, 'sarcastic')
	clean_files(ser_file, ser_out, 'serious')
	# combo file
	combine_files(open(os.getcwd() + '/Data/clean_sarcasm.txt'), open(os.getcwd() + '/Data/clean_serious.txt'), open(os.getcwd() + '/Data/clean_data.txt', 'w+') )
	combine_files(open(os.getcwd() + '/Data/clean_sarcasm.txt').readlines()[:306], open(os.getcwd() + '/Data/clean_serious.txt').readlines()[:573], open(os.getcwd() + '/Data/train_data.txt', 'w+') )
	combine_files(open(os.getcwd() + '/Data/clean_sarcasm.txt').readlines()[306:], open(os.getcwd() + '/Data/clean_serious.txt').readlines()[573:], open(os.getcwd() + '/Data/test_data.txt', 'w+') )
	
def clean_files(in_file, out_file, tag):
	rev = False
	s = ''
	for line in in_file:
		line = line.strip('\n')
		# currently in a review
		if rev:
			s += line.split('</REVIEW>')[0]	# only take stuff on line before close tag
			# have reached end of review
			if '</REVIEW>' in line:
				out_file.write(s)
				out_file.write('\n')
				s = ''
				rev = False
		# not currently in a review
		else:
			# started a review
			if '<REVIEW>' in line:
				rev = True
				x = tag + ' '
				x += line.split('<REVIEW>')[1]	# only take stuff on line after start tag
				# review starts and ends on same line
				if '</REVIEW>' in x:	# only take stuff on line before close tag
					rev = False
					x = x.split('</REVIEW>')[0]
				s += x
	if rev:
		out_file.write(s)

def combine_files(f1, f2, outfile):
	for line in f1:
		line = line.strip('\n') + '\n'
		outfile.write(line)
	for line in f2:
		line = line.strip('\n') + '\n'
		outfile.write(line)

if __name__ == '__main__':
	main()
