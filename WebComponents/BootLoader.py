import requests
import zipfile
import os

def ParserDownload():
	url = "https://nlp.stanford.edu/software/stanford-corenlp-4.5.6.zip"
	
	filename = "stanford-corenlp-4.5.6.zip"
	
	directory = "./Parser/"
	
	os.makedirs(directory, exist_ok=True)
	
	response = requests.get(url)
	
	if response.status_code == 200:
	    with open(os.path.join(directory, filename), 'wb') as f:
	        f.write(response.content)
	    print("Download successful.")
	
	    with zipfile.ZipFile(os.path.join(directory, filename), 'r') as zip_ref:
	        zip_ref.extractall(directory)
	    print("Extraction successful.")
	else:
	    print("Failed to download file.")
