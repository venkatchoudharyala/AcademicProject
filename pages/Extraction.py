import streamlit as st
from WebComponents import ArticleExtractor as ocr

from streamlit_cropper import st_cropper
from PIL import Image

st.set_page_config(layout="wide")
def main():
	tab1, tab2 = st.tabs(['Manual', 'OCR'])
	if 'Questions' not in st.session_state:
		st.session_state['Questions'] = []
	st.session_state['Flag'] = False
	with tab1:
		with st.form("Manual", clear_on_submit = True):
			Question = st.text_area("Question")
			st.write(Question)
			col1, col2 = st.columns(2)
			with col1:
				if st.form_submit_button("Reset"):
					k = 0
					#st.session_state['Questions'].append({"QuestionID": ID, "Question": Question})
			with col2:
				if st.form_submit_button("Generate HL"):
					st.session_state['Question'].append(Question)
					st.switch_page("pages/Final.py")
	with tab2:
		if "file_uploader_key" not in st.session_state:
			st.session_state["file_uploader_key"] = 0
		Image_File = st.file_uploader("Upload the Image", type=['png', 'jpg'], key=st.session_state["file_uploader_key"],)
		if Image_File:
			col1, col2 = st.columns(2)
			with col1:
				img = Image.open(Image_File)
				cropped_img = st_cropper(img, realtime_update = True, box_color = "#FF0012", aspect_ratio = (5, 2))

			with col2:
				st.write("Preview")
				_ = cropped_img.thumbnail((580, 580))
				st.image(cropped_img)
				#if st.button("Extract"):
				ExText = ocr.ocr_with_tesseract(cropped_img)
			with st.form("OCR", clear_on_submit = True):
				Question = st.text_area("Question", value = ExText)
				col1, col2 = st.columns(2)
				with col1:
					if st.form_submit_button("Reset"):
						st.session_state["file_uploader_key"] += 1
						st.rerun()
						#st.session_state['Questions'].append({"Question": Question})
				with col2:
					if st.form_submit_button("Generate HL"):
						st.session_state['Questios'].append(Question)
						st.switch_page("pages/Final.py")
if __name__ == "__main__":
	main()
