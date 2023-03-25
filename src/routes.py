import os 
import json 
import pandas as pd 
import streamlit as st 
from src.asset_upload import UploadAssets

class Routes:
    def __init__(self) -> None:
        self.model_name = None 
        self.public_info = None 
        self.assumptions = None 
        self.assumptions_reasons = None
    
    def home(self):
        st.title("Page 1")
        st.write("Welcome to Page 1!")
    
    def upload_assets(self):
        assets = UploadAssets()
        self.model_file = assets.upload_model() 
        validation_data = assets.upload_validation_data()
        
        if validation_data:
            df = pd.read_csv(validation_data)
            st.dataframe(df) 
            df.to_csv('Data/uploaded.csv')
            
    
    def public_model_info(self):
        info_json = {}
        st.write("Add Public and Model Informationn")
    
        label1 = "Model name and info: "
        self.model_name = st.text_input(label1)
        
        if self.model_name: 
            info_json['model_name'] = self.model_name 

        label2 = "Public info: "
        self.public_info = st.text_area(label2)
        
        if self.public_info:
            info_json['public_info'] = self.public_info 

        label3 = "Assumptions: "
        self.assumptions = st.text_area(label3)
        
        if self.public_info:
            info_json['assumptions'] = self.assumptions 

        label4 = "Reason for above decisions"
        self.assumptions_reasons = st.text_area(label4)
        
        if self.assumptions_reasons:
            info_json['assumptions_reasons'] = self.assumptions_reasons 

        # Add a submit button
        if st.button("Submit"):
            # Handle the form submission here
            st.write("Noted all your observations and assumptions")
            # save info_json as json file 
            with open('Data/info_json.json', 'w') as outfile:
                json.dump(info_json, outfile, indent=4)
            st.success("Noted all your assumptions and observations")
            
    
    def setup_for_visualisation(self):
        if not os.path.exists("Data/uploaded.csv"):
            st.warning("Please upload the validation data for visualization")
        
        validation_dataframe = pd.read_csv('Data/uploaded.csv')
        st.dataframe(validation_dataframe)

    
    def visualise_data(self):
        st.write("Visualise Data and Model inference info")
        self.setup_for_visualisation() 
    
    def export(self):
        st.write("Export visualizations in the form of .pdf")
    
    