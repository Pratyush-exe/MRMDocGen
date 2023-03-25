import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pdfkit

# Load data
data = pd.read_csv('Data/data.csv')

# Create dashboard
st.title('My Dashboard')
st.write('This is a dashboard created using Streamlit.')

# Display data
st.subheader('Data')
st.dataframe(data)

# Display charts
st.subheader('Charts')

# Chart 1: Scatter plot
st.write('## Scatter plot')
sns.scatterplot(data=data, x='monthly_salary', y='card_interest_rate')
st.pyplot()

# Chart 2: Bar chart
st.write('## Bar chart')
plt.bar(data['monthly_salary'], data['card_interest_rate'])
st.pyplot()

# Download as PDF function
def download_pdf(url):
    options = {
        'page-size': 'A4',
        'margin-top': '0mm',
        'margin-right': '0mm',
        'margin-bottom': '0mm',
        'margin-left': '0mm'
    }
    pdfkit.from_url(url, 'dashboard.pdf', options=options)

# Add download button
if st.button('Download PDF'):
    url = st.url_builder.build()
    download_pdf(url)

