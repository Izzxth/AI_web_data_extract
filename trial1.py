import streamlit as st
import pandas as pd
import os
import openai
from serpapi import GoogleSearch

st.title("AI-Powered Information Extractor")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(data.head())

    # Column selection
    columns = data.columns.tolist()
    selected_column = st.selectbox("Select the column with entities:", columns)
    if st.button("Confirm Selection"):
        st.write(f"Selected column: {selected_column}")

# Function to perform search using SerpAPI
def search_entity(entity):
    search = GoogleSearch({
        "q": f"Find the email address for {entity}",
        "location": "United States",
        "hl": "en",
        "api_key": "b84a53fca36994502aa86fcedd893e859a044a0f295731ba77235e1a3238187a"
    })
    results = search.get_dict()
    return results.get("organic_results", [])

# Set OpenAI API key
openai.api_key = "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"

# Function to parse results using OpenAI API
def parse_results(entity, search_results):
    prompt = f"Extract the email address for {entity} from the following search results: {search_results}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return response.choices[0].text.strip()

# Perform search and extract information
if st.button("Start Search"):
    entities = data[selected_column].dropna().tolist()
    st.write(f"Searching for {len(entities)} entities...")

    # Initialize results and extracted_data
    results = {}
    extracted_data = []

    # Search and parse results for each entity
    for entity in entities:
        search_results = search_entity(entity)
        results[entity] = search_results

        # Parse search results using OpenAI
        extracted_info = parse_results(entity, search_results)
        extracted_data.append({"Entity": entity, "Extracted Info": extracted_info})

    st.write("Search complete!")

    # Display extracted information
    st.write("Extracted Information:")
    st.dataframe(pd.DataFrame(extracted_data))

    # Download as CSV
    def download_csv(dataframe):
        return dataframe.to_csv(index=False).encode('utf-8')

    csv_data = download_csv(pd.DataFrame(extracted_data))
    st.download_button(
        label="Download Results as CSV",
        data=csv_data,
        file_name="extracted_results.csv",
        mime="text/csv"
    )
