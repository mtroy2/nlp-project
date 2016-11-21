def main():
	sarc_file = open('sarcasm.txt')
	ser_file = open('serious.txt')
	sarc_out = open('clean_sarcasm.txt', 'w+')
	ser_out = open('clean_serious.txt', 'w+')
	clean_files(sarc_file, sarc_out)
	clean_files(ser_file, ser_out)

def clean_files(in_file, out_file)
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
				s = ''
				rev = False
		# not currently in a review
		else:
			# started a review
			if '<REVIEW>' in line:
				rev = True
				x = line.split('<REVIEW>')[1]	# only take stuff on line after start tag
				# review starts and ends on same line
				if '</REVIEW>' in x:	# only take stuff on line before close tag
					rev = False
					x = x.split('</REVIEW>')[0]
				s += x
	if rev:
		out_file.write(s)

if __name__ == '__main__':
	main()
