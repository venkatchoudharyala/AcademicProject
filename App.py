import streamlit as st
from WebComponents import BootLoader as bl
import os
import nltk

def main():
	#os.environ['JAVAHOME'] = 'usr/bin/java'
	st.title("Abstract Page")
	if "Server" not in st.session_state:
		bl.Booting()
	else:
		if st.button("Upload Text"):
			st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
