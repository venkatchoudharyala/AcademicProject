import streamlit as st
from headline_gen.Control import Generate

def main():
	if 'Questions' in st.session_state:
		with st.spinner("Generating Head Line!!!"):
			st.subheader(st.session_state['Questions'][-1])
			st.success(Generate(st.session_state['Questions'][-1], st.sessio_state["Server"]))
	else:
		st.error("Please Navigate back to Extraction Page and Upload your Article")

if __name__ == "__main__":
	main()
