import streamlit as st
from WebComponents import BootLoader as bl
import os
import nltk

def main():
	st.session_state["Flag"] = True
	#os.environ['JAVAHOME'] = 'usr/bin/java'
	st.title("Abstract Page")
	if st.session_state["Flag"]:
		bl.Booting()
		st.session_state["Flag"] = False

	if st.button("Upload Text"):
		st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
