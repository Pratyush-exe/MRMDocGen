import streamlit as st

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
