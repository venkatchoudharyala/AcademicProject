import streamlit as st
from WebComponents import BootLoader as bl
import os
import nltk

def main():
	st.session_state["Flag"] = True
	os.environ['CLASSPATH'] = 'Parser/stanford-corenlp-4.5.6'
	#os.environ['JAVAHOME'] = 'usr/bin/java'
	st.title("Abstract Page")
	with st.spinner("Checking for necessary Dependencies"):
		if st.session_state["Flag"]:
			bl.Booting()
			st.session_state["Flag"] = False

	if st.button("Upload Text"):
		st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
