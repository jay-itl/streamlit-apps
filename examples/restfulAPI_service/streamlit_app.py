import streamlit as st
import requests

# Define the backend URL
backend_url = "http://127.0.0.1:5000/api/items"
# backend_url = "https://dummyjson.com/posts/add"

st.title("Streamlit with Flask API Example")

# Form to collect item data
with st.form("item_form"):
    name = st.text_input("Name")
    description = st.text_input("Description")
    price = st.number_input("Price", min_value=0.0)
    tax = st.number_input("Tax", min_value=0.0, value=0.0)
    submitted = st.form_submit_button("Submit")

if submitted:
    # Create the item data
    item_data = {
        "name": name,
        "description": description,
        "price": price,
        "tax": tax
    }

    # Send a POST request to the Flask API
    response = requests.post(backend_url, json=item_data)

    if response.status_code == 200:
        st.success("Item created successfully!")
        st.json(response.json())
    else:
        st.error("Failed to create item.")
