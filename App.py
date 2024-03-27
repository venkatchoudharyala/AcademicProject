import streamlit as st
from WebComponents import BootLoader as bl

def main():
	with st.spinner("Checking for necessary Dependencies"):
		bl.Booting()
	st.switch_page("Pages/Extraction.py")
if __name__ == "__main__":
	main()
