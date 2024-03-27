import streamlit as st
from WebComponents import BootLoader as bl
from nltk.parse.corenlp import CoreNLPServer
import os
import nltk

def main():
	os.environ['CLASSPATH'] = 'Parser/stanford-corenlp-4.5.6'
	#os.environ['JAVAHOME'] = 'usr/bin/java'
	st.title("Abstract Page")
	with st.spinner("Checking for necessary Dependencies"):
		bl.Booting()

	if st.button("Upload Text"):
		st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
