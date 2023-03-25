import streamlit as st
from src.asset_upload import UploadAssets
from src.routes import Routes 


# Define the app
def app():
    #st.set_page_config(page_title="My App")
    st_routes = Routes()
    
    # Create a dictionary that maps page names to page functions
    pages = {
        "Home": st_routes.home,
        "Upload model and data": st_routes.upload_assets,
        "Add public and model info": st_routes.public_model_info, 
        "Visualise data and model output": st_routes.visualise_data, 
        "Export pdf": st_routes.export
    }

    # Display a list of pages on the left side
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", list(pages.keys()))

    # Display the selected page with the page function
    pages[page]()

# Run the app
if __name__ == "__main__":
    app()
