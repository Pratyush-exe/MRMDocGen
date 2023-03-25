
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt


# Define the contents of the three pages
def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")


def page2():
    label1 = "Model name and info: "
    text1 = st.text_area(label1)

    label2 = "Public info: "
    text2 = st.text_area(label2)

    label3 = "Assumptions: "
    text3 = st.text_area(label3)

    label4 = "Reason for above decisions"
    text4 = st.text_area(label4)

    # Add a submit button
    if st.button("Submit"):
        # Handle the form submission here
        st.write("You clicked the Submit button!")


def thresh(x):
    if x > 0.5:
        return 1
    else:
        return 0


def page3():
    df = pd.read_csv('Data/data.csv')
    df['model_output'] = df['model_output'].apply(thresh)
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




def page4():
    st.title("Page 4")
    st.write("Welcome to Page 3!")


# Define the app
def app():
    st.set_page_config(page_title="My App")

    # Create a dictionary that maps page names to page functions
    pages = {
        "Page 1": page1,
        "Page 2": page2,
        "Page 3": page3
    }

    # Display a list of pages on the left side
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page with the page function
    pages[page]()


# Run the app
if __name__ == "__main__":
    app()
