import streamlit as st
import os
from werkzeug.utils import secure_filename
import requests
import json
import utils

st.set_page_config(page_title="BEPC-JobEQ", page_icon="static/logo.png", layout='wide')
import base64
# Function to read binary data and convert to base64
def get_image_base64(image_path):
    with open(image_path, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

# Convert your images to base64
sr2new = get_image_base64('static/rs2.png')

# Include the base64 images in your HTML
st.markdown(
    f"""
    <div class="container">
        <h2 class="text-center mt-4">
            <img src="data:image/png;base64,{sr2new}" width="50" height="50" class="d-inline-block align-top" alt="">
            JobEqualizer <span style="font-style: italic; font-size: 17px;">for recruiting V1.1</span>
        </h2>
    </div>
    """,
    unsafe_allow_html=True,
)

job_id = st.text_input('1.- Enter the Job ID')

if st.button('Equalize'):
    with st.spinner('Obtaining Job Description...'):
        # Fetch the original job description
        original_description = utils.fetchjob(job_id)  # Using the equalize function from utils.py
        col1, col2 = st.columns(2)
        col1.header("Job Description")
        col1.markdown(original_description, unsafe_allow_html=True)  # Display the original content in Streamlit

    with st.spinner('Equalizing Job Description...'):
        # Equalize the job description
        equalized_description = utils.equalize(original_description)  # Using the equalize function from utils.py
        col2.header("Equalized Job Description")
        col2.markdown(equalized_description, unsafe_allow_html=True)  # Display the equalized content in Streamlit

    st.success("Job Equalization completed! To equalize another Job, please refresh the page (press F5).")
    

st.markdown("""
<footer class="footer mt-auto py-3">
    <div class="container text-center">
        <p class="text-muted">
            Copyright © 2023 | BEPC Incorporated | All Rights Reserved |
            <a href="https://52840b2d-10d4-472e-8343-b77dcb77c887.filesusr.com/ugd/17c3bf_3ac57d22aa71435a8e092faeab264e45.pdf">Privacy Policy</a> |
            <a href="https://52840b2d-10d4-472e-8343-b77dcb77c887.filesusr.com/ugd/17c3bf_01578308cc1f4718b62978df425c17c3.pdf">Cybersecurity</a> |
            <a href="https://52840b2d-10d4-472e-8343-b77dcb77c887.filesusr.com/ugd/17c3bf_9ba7da42b5104bc5b8060b236b55276f.pdf">HIPAA</a>
            |  MSMMXXIII
        </p>
    </div>
</footer>
""", unsafe_allow_html=True)