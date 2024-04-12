import streamlit as st
from headline_gen import ServerInit
import os
import nltk

def main():
	#os.environ['JAVAHOME'] = 'usr/bin/java'
	st.title("Abstract Page")
	if "Server" not in st.session_state:
		st.session_state["Server"] = ServerInit("Start")
	else:
		if st.button("Upload Text"):
			st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
