import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from pynput.keyboard import Key, Controller
import time
from datetime import datetime
import pandas as pd
import json
from src.gpt import getTextGPT
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns

from src.visualisations import MetricsViz


def thresh(x):
    if x > 0.5:
        return 1
    else:
        return 0


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

        info_json = getTextGPT(info_json)

        overview = info_json["overview"]
        data_prep = info_json["data_prep"]
        model_name = info_json["model_name"]
        model_methadology = info_json["model_methadology"]
        assumptions = info_json["assumptions"]
        conclusion = info_json["conclusion"]

        header_container = st.container()
        keyboard = Controller()
        with header_container:
            st.header("Complete Generated Report")
            pressed = st.button("Download PDF")
            if pressed:
                keyboard.press(Key.ctrl)
                keyboard.press('p')
                keyboard.release('p')
                keyboard.release(Key.ctrl)
                time.sleep(5)
        datetime_ = st.write(datetime.today())

        overview_header = st.subheader("Overview")
        overview_text = st.write(overview)

        data_prep_header = st.subheader("Data Preparation")
        data_prep_text = st.write(data_prep)

        dataframe_header = st.subheader("Validation data results")
        dataframe_about = st.write(
            "Below is our dataframe that contains the model output along with its confidence score"
        )

        st.dataframe(df)

        st.markdown("----")
        df = pd.read_csv(r'Data/data.csv')
        df['model_output'] = df['model_output'].apply(thresh)
        y_true = df['model_target']
        y_pred = df['model_output']

        st.subheader('Data stats')
        st.dataframe(df.describe())

        st.markdown("----")

        st.subheader("Correlation Matrix")
        corr = df.corr()
        heatmap = sns.heatmap(corr, annot=True)
        st.pyplot(heatmap.figure)

        st.markdown("----")

        modelling_header = st.subheader("Modelling and results")
        model_name_info = st.markdown(
            f"The model that has been selected is: **`{model_name}`**"
        )
        model_methadology_info = st.markdown(model_methadology)


        st.subheader('Confusion Matrix')
        cm = confusion_matrix(y_true, y_pred)

        fig, ax = plt.subplots()
        im = ax.imshow(cm, cmap=plt.cm.Blues)

        ax.set_xticks(np.arange(cm.shape[1]))
        ax.set_yticks(np.arange(cm.shape[0]))
        ax.set_xticklabels(['Negative', 'Positive'])
        ax.set_yticklabels(['Negative', 'Positive'])
        ax.set_title("Confusion Matrix")
        plt.colorbar(im)

        def compute_metrics():
            accuracy = accuracy_score(y_true, y_pred)
            precision = precision_score(y_true, y_pred)
            recall = recall_score(y_true, y_pred)
            f1 = f1_score(y_true, y_pred)

            return {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1}

        metrics = compute_metrics()
        col1, col2 = st.columns([2, 1])
        with col1:
            st.pyplot(fig)
        with col2:
            for key, value in metrics.items():
                st.write(key + ':', value)

        st.markdown("----")

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
