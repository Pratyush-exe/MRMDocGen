import streamlit as st 
from src.asset_upload import UploadAssets

class Routes:
    def __init__(self) -> None:
        pass 
    
    def home(self):
        st.title("Page 1")
        st.write("Welcome to Page 1!")
    
    def upload_assets(self):
        assets = UploadAssets()
        self.model_file = assets.upload_model() 
        self.validation_data = assets.upload_validation_data()
    
    def public_model_info(self):
        st.write("Add Public and Model Informationn")
    
    def visualise_data(self):
        st.write("Visualise Data and Model inference info")
    
    def export(self):
        st.write("Export visualizations in the form of .pdf")
    
    