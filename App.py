import streamlit as st
from WebComponents import BootLoader as bl
import os

st.set_page_config(layout="centered")
def main():
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
	if st.button("Upload Text"):
		st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
