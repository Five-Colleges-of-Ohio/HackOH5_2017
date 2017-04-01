''' Load data into easy to read txt files from JSON '''
import json
import os
from datetime import datetime

schools = ["wooster", "denison", "kenyon", "oberlin", "wesleyan"]

minYear = 1990
maxYear = 1999

if not os.path.exists("input_files/"):
	os.makedirs("input_files/")

for school in schools:
	indir = "oh5_json_data/" + school + "/issues/"

	input_files = os.listdir(indir)

	if not os.path.exists("input_files/" + school):
		os.makedirs("input_files/" + school)

	txt_by_year = dict()
	for year in range(minYear, maxYear + 1):
		txt_by_year[year] = ""

	for infile_name in input_files:
		in_fh = open(indir + infile_name, 'r')
		raw_in_data = in_fh.read()
		in_fh.close()

		file_dict = json.loads(raw_in_data)
		issue_year = datetime.strptime(file_dict["navDate"], "%Y-%m-%dT00:00:00Z").year

		if issue_year < minYear or issue_year >= maxYear+1:
			continue
		
		issue_articles = file_dict["sequences"][0]["canvases"]
		
		issue_txt = ""
		for article in issue_articles:
			issue_txt += " " + article["metadata"][2]["value"]

		txt_by_year[issue_year] += " " + issue_txt

	for year, txt in txt_by_year.items():
		out_fh = open("input_files/" + school + "/" + str(year) + ".txt", 'w')
		out_fh.write(txt)
		out_fh.close()
