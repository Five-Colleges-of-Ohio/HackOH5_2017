import re
import sys

input_f = sys.argv[1]
vector_output_f = sys.argv[2]
label_output_f  = sys.argv[3]

in_fh = open(input_f, 'r')
file_str = in_fh.read()
in_fh.close()

m = re.match("^(\d+) (\d+)\n", file_str)

num_rows = m.group(1)
num_cols = m.group(2)

all_matches = re.findall("(\w+) (.*)\n", file_str)

del all_matches[0]

word_out_str = ""
vector_out_str = ""
for match in all_matches:
	word = match[0]
	word_out_str += word + "\n"

	vector = str.split(match[1], " ")
	first = True
	for v in vector:
		if first:
			vector_out_str += v
			first = False
		else:
			vector_out_str += "\t" + v
		
	vector_out_str += "\n"

out_fh = open(vector_output_f, 'w')
out_fh.write(vector_out_str)
out_fh.close()

out_fh = open(label_output_f, 'w')
out_fh.write(word_out_str)
out_fh.close()
