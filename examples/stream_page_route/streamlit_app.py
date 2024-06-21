import streamlit as st

# Define your pages as separate functions
def home_page():
    st.title("Home Page")
    st.write("Welcome to the home page!")

def about_page():
    st.title("About Page")
    st.write("This is the about page.")

def contact_page():
    st.title("Contact Page")
    st.write("This is the contact page.")

# Dictionary to map routes to pages
pages = {
    "Home": home_page,
    "About": about_page,
    "Contact": contact_page
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
page = pages[selection]
page()
