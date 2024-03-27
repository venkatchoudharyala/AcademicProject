import streamlit as st
from CompleteSystemProto import Generate

def main():
  st.success(Generate(st.session_state['Question']))

if __name__ == __main__():
  main()
