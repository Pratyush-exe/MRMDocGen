import os
import json
import pandas as pd
import streamlit as st
import numpy as np

import seaborn as sns
import matplotlib.pyplot as plt
from src.asset_upload import UploadAssets
from datetime import datetime

from src.infos import ModelDataInfo
from src.gpt import getTextGPT
from src.visualisations import MetricsViz
from src.pdf_report import PdfReportGenerator



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
            df.to_csv("Data/uploaded.csv")

    def public_model_info(self):
        ModelDataInfo().get_document_general_info()

    def visualise_data(self):
        MetricsViz().visualise()

    def export(self):
        # TODO Integrate chatGPT for better writing output 
        pdf_report = PdfReportGenerator()
        pdf_report.prepare_report()
