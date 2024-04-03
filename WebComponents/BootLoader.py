import requests
import zipfile
import os
from nltk.parse.corenlp import CoreNLPServer
import streamlit as st
import nltk

def Booting():
	directory_path = "Parser/stanford-corenlp-4.5.6"
	
	if os.path.exists(directory_path) and os.listdir(directory_path):
		st.success("Files Found", icon="✅")
		
	else:
		ParserDownload()
	
	print("Attempting to Start the server")
	Server()

def ParserDownload():
	nltk.download('punkt')
	nltk.download('stopwords')
	
	with st.spinner("Checking for necessary Dependencies"):
		url = "https://nlp.stanford.edu/software/stanford-corenlp-4.5.6.zip"
		
		filename = "stanford-corenlp-4.5.6.zip"
		
		directory = "Parser"
		
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

def Server():
	os.environ['CLASSPATH'] = 'Parser/stanford-corenlp-4.5.6'
	st.session_state['Server'] = CoreNLPServer()
	with st.spinner("Initializing CoreNLP Server!"):
		st.session_state['Server'].start()
		st.success('Server Initialized', icon="✅")
	print("Server up and running")
