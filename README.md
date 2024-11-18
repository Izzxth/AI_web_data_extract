               AI-Powered Information Extractor


The AI-Powered Information Extractor allows users to upload a CSV file, select a column containing entity names, and automatically extract specific information such as email addresses for each entity. The system uses SerpAPI for web search and OpenAI GPT-3 for parsing search results and extracting the relevant information. The results can then be displayed and downloaded as a CSV file.

Features 

1️⃣ CSV File Upload: Upload a CSV file containing entities (e.g.,  company names).
2️⃣ Column Selection: Choose the column containing entity names.
3️⃣ Search for Information: Use SerpAPI to search for relevant information (e.g., email addresses) based on the entity.
4️⃣ AI-Powered Data Parsing: Use OpenAI GPT-3 to process search results and extract specific information.
5️⃣ Download Results: Download the extracted information in CSV format.
Open AI
Serp APIYou need to obtain the following API keys to use this project:

SerpAPI: You can get your API key by signing up at SerpAPI.
OpenAI: You can get your API key by signing up at OpenAI.
Once you have the keys, replace the placeholders in the code:

Replace serp_api_key in the search_entity function with your SerpAPI key.
Replace openai.api_key with your OpenAI key.
## Run Locally

Clone the project

```bash
  git clone https://github.com/Izzxth/AI_web_data_extract.git
```


## Requirements

Python 3.x
pip (Python package installer)
Dependencies (can be installed via requirements.txt)
You can install required dependencies by using the following command:
pip install -r requirements.txt

Here are the essential libraries used in this project:

streamlit: For creating the interactive web interface.
pandas: For data manipulation and handling CSV files.
serpapi: To interface with the SerpAPI for web searches.
openai: For interacting with OpenAI's GPT-3 model to process data.## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |


## Usage

Usage Guide

1️⃣ Upload your CSV file: Click on the file uploader in the app to upload a CSV containing the entities (e.g., company names).
Select the column with entities: After uploading the file, choose the column that contains the entity names.

2️⃣ Start the search: Press the "Start Search" button to begin the search process.

3️⃣ View the extracted data: The extracted information (e.g., email addresses) will be displayed in a table.

4️⃣ Download the results: Once the search and extraction are complete, you can download the extracted data as a CSV file.


## Features

AI-Powered Extraction: Utilizes machine learning models to intelligently extract relevant data from websites.
Easy Setup: Simple configuration with minimal setup required.
Customizable: Easily extendable for different web scraping tasks, including handling dynamic content (JavaScript) and various HTML structures.
Data Cleaning: Automatically processes and structures extracted data for easy use in analysis or further processing.
Cross-Platform: Compatible with both Windows and Linux environments.

## Expected flow


## Expected flow

1. File Upload Screen
After launching the app (streamlit run trial1.py), you'll see an upload button to upload a CSV file.

2. Column Selection
After selecting and uploading the file, the app will prompt you to select a column that contains the entities (e.g., company names, personal names).
You’ll see a dropdown menu that allows you to choose the correct column.

3. Search Process
Once you select the column and click "Start Search", the system will initiate the search process using SerpAPI to fetch results.
You'll see the text "Searching for [X] entities...", where [X] will be the number of entities from the selected column.

4. Results Display
After the search is completed, the extracted information will be displayed in a table. This will include the Entity (e.g., company name) and the Extracted Info (e.g., email address).

5. Download Button
Once the data is displayed, you will also have the option to download the results as a CSV file.
A Download Results as CSV button will be visible.
## Authors

Izzath Fathima (https://github.com/Izzxth)
mail: izzu0512@gmail.com
## Appendix

Any additional information goes here


## Deployment

To deploy this project run

```bash
  npm run deploy
```

