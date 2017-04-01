'''
Generate vector and label TSV files

Usage: python createTSVs_search.py minYear maxYear [school]
'''


from subprocess import call
import os
import sys

min_year = int(sys.argv[1])
max_year = int(sys.argv[2])
s = None
if len(sys.argv) > 3:
	s = sys.argv[3]

# call(["python get_txt_from_json.py " + min_year + " " + max_year + (" " + s) if not s == None else ""])

if not os.path.exists("models/"):
	os.makedirs("models/")

if not os.path.exists("txtModels/"):
	os.makedirs("txtModels/")

if not os.path.exists("TSVs/"):
	os.makedirs("TSVs/")

schools = os.listdir("input_files/")
if not s == None:
	schools = [s]
for school in schools:
	years = range(min_year, max_year + 1)
	for y in years:
		year = str(y)
		print("Processing " + school.upper() + " articles from " + year + "...")

		# Create .model file
		print("Creating model file...")
		os.system("python trainword2vec.py input_files/" + school + "/" + year + ".txt models/" + year + school + ".model")
		print("Done.")

		# Create .txt files from .model files
		print("Extracting model file to txt...")
		os.system("python model_to_txt.py models/" + year + school + ".model txtModels/" + year + school + ".txt")
		print("Done.")

		# Create TSV files, the desired output
		print("Generating TSV files...")
		os.system("python extract_word_metadata.py txtModels/" + year + school + ".txt TSVs/" + year + school + "Vectors.tsv TSVs/" + year + school + "Labels.tsv")
		print("Done.")
