import streamlit as st
from WebComponents import BootLoader as bl

def main():
	with st.spinner("Checking for necessary Dependencies"):
		bl.Booting()
	if st.button("Upload Text"):
		st.switch_page("pages/Extraction.py")
if __name__ == "__main__":
	main()
