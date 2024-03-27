import streamlit as st
from CompleteSystemProto import Generate
import nltk

def main():
	if 'Questions' in st.session_state:
		with st.spinner("Generating Head Line!!!"):
			st.success(Generate(st.session_state['Questions'][-1]))

if __name__ == "__main__":
	main()
