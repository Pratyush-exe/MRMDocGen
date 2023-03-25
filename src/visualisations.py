import streamlit as st
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
)
from datetime import datetime
from typing import Union, List, Dict
import matplotlib.pyplot as plt
import pandas as pd


class MetricsViz:
    def __init__(self):
        ...

    def thresh(self, x: float) -> int:
        """Common threshold function

        Args:
            x (float): input

        Returns:
            int: whether it crosses the threshold
        """
        if x > 0.5:
            return 1
        else:
            return 0

    def compute_metrics(
        self,
        y_true: Union[List[float], np.ndarray],
        y_pred: Union[List[float], np.ndarray],
    ) -> Dict[str, List[float]]:
        """Calculates common model metrics

        Args:
            y_true Union[List[float], np.ndarray]: True value
            y_pred Union[List[float], np.ndarray]: Predicted values

        Returns:
            _type_: _description_
        """
        accuracy = accuracy_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)
        f1 = f1_score(y_true, y_pred)
        return {
            "accuracy": [accuracy],
            "precision": [precision],
            "recall": [recall],
            "f1": [f1],
        }

    def visualise(self):
        st.title("Data Visualization")
        # self.setup_for_visualisation()

        df = pd.read_csv("Data/data.csv")
        df["model_output"] = df["model_output"].apply(self.thresh)
        y_true = df["model_target"]
        y_pred = df["model_output"]

        st.subheader("Data")
        st.dataframe(df)

        st.subheader("Data stats")
        st.dataframe(df.describe())

        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y_true, y_pred)

        fig, ax = plt.subplots()
        im = ax.imshow(cm, cmap=plt.cm.Blues)

        ax.set_xticks(np.arange(cm.shape[1]))
        ax.set_yticks(np.arange(cm.shape[0]))
        ax.set_xticklabels(["Negative", "Positive"])
        ax.set_yticklabels(["Negative", "Positive"])
        ax.set_title("Confusion Matrix")
        plt.colorbar(im)

        metrics = self.compute_metrics(y_true, y_pred)
        metrics_df = pd.DataFrame(metrics)
        st.dataframe(metrics_df)

        st.subheader("Scatter Plots")
        col1, col2 = st.columns([2, 1])
        with col1:
            x_column = st.selectbox("Select X column", df.columns)
        with col2:
            y_column = st.selectbox("Select Y column", df.columns)

        fig, ax = plt.subplots()
        ax.scatter(df[x_column], df[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)

        st.pyplot(fig)
