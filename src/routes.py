import os 
import json 
import pandas as pd 
import streamlit as st 
import numpy as np
import matplotlib.pyplot as plt 
from src.asset_upload import UploadAssets
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


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

    
    def thresh(self, x):
        if x > 0.5:
            return 1
        else:
            return 0
    
    def visualise_data(self):
        st.write("Visualise Data and Model inference info")
        #self.setup_for_visualisation() 
        
        df = pd.read_csv('Data/data.csv')
        df['model_output'] = df['model_output'].apply(self.thresh)
        y_true = df['model_target']
        y_pred = df['model_output']

        st.title('Data')
        st.dataframe(df)

        st.title('Data stats')
        st.dataframe(df.describe())

        st.title('Confusion Matrix')
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


        st.title('Scatter Plots')
        col1, col2 = st.columns([2, 1])
        with col1:
            x_column = st.selectbox('Select X column', df.columns)
        with col2:
            y_column = st.selectbox('Select Y column', df.columns)

        fig, ax = plt.subplots()
        ax.scatter(df[x_column], df[y_column])
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)

        st.pyplot(fig)
    
    def prepare_text_for_export(self):
        # read Data/info_json.json and convert it to a dict 
        with open('Data/info_json.json', 'r') as json_file:
            info_json = json.load(json_file)

        # convert dict to a string
        print(info_json)

        model_name = info_json['model_name']
        public_info  = info_json['public_info']
        assumptions = info_json['assumptions']
        assumptions_reasons = info_json['assumptions_reasons']
        
        header = st.header("Here is your final information about observations you have gathered")
        
        public_info_header = st.subheader("Public information")
        public_info = st.write(public_info)
        
        assumptions_header = st.subheader("Assumptions")
        assumptions_info = st.write(assumptions)
        
        assumptions_header = st.subheader("Assumptions Reasons")
        assumptions_info = st.write(assumptions_reasons)
        
        # add a dataframe here 
        
        st.markdown("----")
        modelling_header = st.subheader("Modelling and results")
        
        model_name_info = st.markdown(f"The model that has been selected is: **`{model_name}`**")
                
        dataframe_header = st.subheader("Validation data results")
        dataframe_about = st.write("Below is our dataframe that contains the model output along with its confidence score")
        
        df = pd.read_csv('Data/data.csv')
        st.dataframe(df)
        
        st.markdown("----")
        
        # Data and model visualizations 
        
        st.write("Data descriptions")
        
        y_true = df['model_target']
        y_pred = df['model_output']

        st.dataframe(df.describe())

        st.title('Confusion Matrix')
        cm = confusion_matrix(y_true, y_pred)

        fig, ax = plt.subplots()
        im = ax.imshow(cm, cmap=plt.cm.Blues)

        ax.set_xticks(np.arange(cm.shape[1]))
        ax.set_yticks(np.arange(cm.shape[0]))
        ax.set_xticklabels(['Negative', 'Positive'])
        ax.set_yticklabels(['Negative', 'Positive'])
        ax.set_title("Confusion Matrix")
        plt.colorbar(im)
        
                
        
    
    def export(self):
        st.write("Export visualizations in the form of .pdf")
        import json
        f1 = open('Data\info_json.json', 'r')
        info = json.load(f1)

        text = getTextGPT(info)
        st.title("Problem Defined")
        st.write(text["problem_statement"])

        st.title("Model Used")
        st.write(text["model_name"])

        st.title("Public Info")
        st.write(text["public_info"])

        st.title("Assumptions")
        st.write(text["assumptions"])

        st.title("Reason for assumptions")
        st.write(text["assumptions_reasons"])

        df = pd.read_csv('Data/data.csv')
        df['model_output'] = df['model_output'].apply(self.thresh)
        y_true = df['model_target']
        y_pred = df['model_output']
        st.title('Data stats')
        st.dataframe(df.describe())

        st.title('Confusion Matrix')
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

            return {'Accuracy': accuracy, 'Precision': precision, 'Recall': recall, 'F1': f1}

        metrics = compute_metrics()
        col1, col2 = st.columns([2, 1])
        with col1:
            st.pyplot(fig)
        with col2:
            for key, value in metrics.items():
                st.write(key + ':', value)

        st.title("Correlation Matrix")
        corr = df.corr()
        heatmap = sns.heatmap(corr, annot=True)
        st.pyplot(heatmap.figure)
        
    
    
