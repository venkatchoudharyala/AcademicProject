import streamlit as st
from WebComponents import BootLoader as bl
from nltk.parse.corenlp import CoreNLPServer
import os
import nltk

def main():
	nltk.download('punkt')
	nltk.download('stopwords')
	os.environ['CLASSPATH'] = 'Parser/stanford-corenlp-4.5.6'
	os.environ['JAVAHOME'] = 'usr/bin/java'
	st.title("Abstract Page")
	with st.spinner("Checking for necessary Dependencies"):
		bl.Booting()
	
	k = os.listdir("Parser/stanford-corenlp-4.5.6")
	flag = 0
	for i in k:
		if i == "stanford-corenlp-4.5.6-models.jar" or i == "stanford-corenlp-4.5.6-sources.jar":
			flag += 1
	if flag == 2:
		st.success('Parser Files Found!', icon="✅")

	st.session_state['server'] = CoreNLPServer()
	#with st.spinner("Initializing CoreNLP Server!"):
	st.session_state['server'].start()
	st.success('Server Initialized', icon="✅")

	if st.button("Upload Text"):
		st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
