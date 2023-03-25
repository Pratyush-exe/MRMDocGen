import streamlit as st

# Define the contents of the three pages
def page1():
    st.title("Page 1")
    st.write("Welcome to Page 1!")

def page2():
    st.title("Page 2")
    st.write("Welcome to Page 2!")

def page3():
    st.title("Page 3")
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
