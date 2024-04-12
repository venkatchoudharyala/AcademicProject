import streamlit as st
from headline_gen.Control import ServerInit
import os
import nltk
from spacy_download import load_spacy
def main():
	nlp = load_spacy("en_core_web_sm") 
	#os.environ['JAVAHOME'] = 'usr/bin/java'
	st.title("Abstract Page")
	if "Server" not in st.session_state:
		with st.spinner("Booting Server"):
			st.session_state["Server"] = ServerInit("Start")
	else:
		if st.button("Upload Text"):
			st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
