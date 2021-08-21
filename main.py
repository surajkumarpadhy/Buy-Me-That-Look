from final_Pipeline import Pipeline
import streamlit as st
from PIL import Image

@st.cache(suppress_st_warning=True,allow_output_mutation=True)
def get_setup():
    final= Pipeline()
    return final

final=get_setup()
st.title("Upload Image")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    image = image.save("./Sample/crop/sample.jpg")
    final.pred_look("./Sample/crop/sample.jpg")
