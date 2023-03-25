import streamlit as st
import matplotlib.pyplot as plt
from fpdf import FPDF
import base64
import numpy as np
from tempfile import NamedTemporaryFile
from datetime import datetime
import pandas as pd
import json

from src.visualisations import MetricsViz


class PdfReportGenerator(MetricsViz):
    def __init__(self) -> None:
        """
        Generates Pdf report for a given page containing documents in forms of text and images
        """

    def prepare_report(self):
        with open("Data/info_json.json", "r") as json_file:
            info_json = json.load(json_file)

        df = pd.read_csv("Data/data.csv")
        df["model_output"] = df["model_output"].apply(self.thresh)
        y_true = df["model_target"]
        y_pred = df["model_output"]

        # convert dict to a string

        overview = info_json["overview"]
        data_prep = info_json["data_prep"]
        model_name = info_json["model_name"]
        model_methadology = info_json["model_methadology"]
        assumptions = info_json["assumptions"]
        conclusion = info_json["conclusion"]

        st.header("Complete Generated Report")
        datetime_ = st.write(datetime.today())

        overview_header = st.subheader("Overview")
        overview_text = st.write(overview)

        data_prep_header = st.subheader("Data Perperation")
        data_prep_text = st.write(data_prep)

        dataframe_header = st.subheader("Validation data results")
        dataframe_about = st.write(
            "Below is our dataframe that contains the model output along with its confidence score"
        )

        st.dataframe(df)

        st.markdown("----")

        # add a dataframe here

        st.markdown("----")
        modelling_header = st.subheader("Modelling and results")
        model_name_info = st.markdown(
            f"The model that has been selected is: **`{model_name}`**"
        )
        model_methadology_info = st.markdown(model_methadology)

        # adding a confusion matrix
        # Data and model visualizations

        st.write("Data descriptions")

        metrics = self.compute_metrics(y_true, y_pred)
        metrics_df = pd.DataFrame(metrics)
        st.dataframe(metrics_df)

        st.markdown("----")
        model_assumptions_header = st.subheader("Assumptions and Reasons")
        model_assumptions_info = st.write(assumptions)

        st.markdown("----")
        model_conclusion_header = st.subheader("Conclusion")
        model_conclusion_info = st.write(conclusion)

        return {
            "datetime_": datetime_,
            "overview_header": overview_header,
            "overview_text": overview_text,
            "data_prep_header": data_prep_header,
            "data_prep_text": data_prep_text,
            "dataframe_header": dataframe_header,
            "dataframe_about": dataframe_about,
            "modelling_header": modelling_header,
            "model_name_info": model_name_info,
            "model_methadology_info": model_methadology_info,
            "model_assumptions_header": model_assumptions_header,
            "mdoel_assumptions_info": model_assumptions_info,
            "model_conclusion_header": model_conclusion_header,
            "model_conclusion_info": model_conclusion_info,
        }

    def create_download_link(self, val, filename):
        """Creates a download link for a given document/page

        Args:
            val (_type_): _description_
            filename (_type_): _description_

        Returns:
            _type_: _description_
        """
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

    def export_page_as_pdf(self, data) -> None:
        ...


# report_text = st.text_input("Report Text")


# export_as_pdf = st.button("Export Report")

# def create_download_link(val, filename):
#     b64 = base64.b64encode(val)  # val looks like b'...'
#     return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

# if export_as_pdf:
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font('Arial', 'B', 16)
#     pdf.cell(40, 10, report_text)

#     html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

#     st.markdown(html, unsafe_allow_html=True)


# from sklearn.datasets import load_iris


# df = load_iris(as_frame=True)["data"]


# figs = []

# for col in df.columns:
#     fig, ax = plt.subplots()
#     ax.plot(df[col])
#     st.pyplot(fig)
#     figs.append(fig)


# export_as_pdf = st.button("Export Report")

# if export_as_pdf:
#     pdf = FPDF()
#     for fig in figs:
#         pdf.add_page()
#         with NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
#                 fig.savefig(tmpfile.name)
#                 pdf.image(tmpfile.name, 10, 10, 200, 100)
#     html = create_download_link(pdf.output(dest="S").encode("latin-1"), "testfile")
#     st.markdown(html, unsafe_allow_html=True)
