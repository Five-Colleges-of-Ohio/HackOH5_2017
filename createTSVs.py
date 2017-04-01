from subprocess import call
import os
import sys

# call(["python get_txt_from_json.py 1990 1999"]) # uncomment if you need to extract data from get_txt_from_json

if not os.path.exists("models/"):
	os.makedirs("models/")

if not os.path.exists("txtModels/"):
	os.makedirs("txtModels/")

if not os.path.exists("TSVs/"):
	os.makedirs("TSVs/")

schools = os.listdir("input_files/")
for school in schools:
	years = os.listdir("input_files/" + school + "/")
	for y in years:
		year = y[0:4]
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
