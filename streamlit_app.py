"""
LIS4693 - IR & Text Mining - Project 2

* The project involves developing an information retrieval system.
* Takes a user query and returns a sorted list of relevant results.
* Displays the relevant text snippets that match the query.

Date: 2025-04-05
Version: 1
Authors: Cody Bennett
         - codybennett@ou.edu
"""

import streamlit as st
import nltk

nltk.download('stopwords')
st.set_page_config(layout="wide", page_title="LIS 4693 - IR & Text Mining - Project 2")

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    st.write("Use the links below to navigate:")
    home = st.page_link("streamlit_app.py", label="🏠 Home")
    page1 = st.page_link("pages/app.py", label="📄 1. Application")


# Homepage content
st.title("Welcome to the IR & Text Mining Project")

st.markdown(
    """
# About The Project

_This application is an advanced information retrieval system designed for analyzing and exploring text data._

------------

* Accepts user queries and returns a ranked list of relevant results.
* Highlights matching text snippets for better context and understanding.
* Provides tools for filtering, exploring, and exporting corpus data.

## Features

* **Search Functionality**: Perform keyword or phrase searches across the corpus.
* **Corpus Exploration**: Explore and filter documents directly within the application.
* **Export Capability**: Save the corpus or search results to a file for offline use.

## Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Getting Started

1. Navigate to the [Application](pages/app.py) to perform searches, explore the corpus, and retrieve relevant results.

## Development

Source code for this project is located in a private GitHub repository.

The application is deployed as a Streamlit application via [Community Cloud](https://streamlit.io/cloud).

## License

Distributed under the GNU GPL3 License.

## Contact

* Cody Bennett - <codybennett@ou.edu>

Project Link: [https://github.com/codybennett/LIS4693-Project2](https://github.com/codybennett/LIS4693-Project2)
"""
)
