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

import logging
import os
import re
import html
import pandas as pd
import streamlit as st
from nltk import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize global variables
cwd = os.getcwd()
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

# Configure logging
logging.getLogger().setLevel(logging.INFO)
logging.basicConfig(
    filename="output.log",
    filemode="a",
    format="%(asctime)s %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.DEBUG,
)

# Streamlit page configuration
st.set_page_config(layout="wide", page_title="Search Corpus")
st.title("Search Corpus")
with st.sidebar:
    st.title("Navigation")
    st.write("Use the links below to navigate:")
    home = st.page_link("streamlit_app.py", label="🏠 Home")
    page1 = st.page_link("pages/app.py", label="📄 1. Application")

st.markdown(
    """
    ## How to Use the App
    1. **Search**:
         Enter a keyword or phrase in the search bar to find relevant documents.
    2. **Filter**:
         Use the sidebar options to narrow down the results by specific criteria.
    3. **Explore Results**:
         Expand the search results to view document snippets and full content.
    4. **Export**:
         Click the "Export Corpus" button to save all documents to a text file.
    """
)

st.markdown(
    """
    **Note:** The search query performs a raw text search across the documents in the corpus. 
    It matches keywords or phrases based on their processed content.
    """
)
query = st.text_input(
    "Enter your search query:",
    help="Type a keyword or phrase to search the corpus for relevant documents.",
)


@st.cache_data
def preprocess_text(text):
    """Preprocess text by tokenizing, lemmatizing, and removing stopwords.

    :param text: Input text to preprocess
    :type text: str
    :return: Preprocessed text
    :rtype: str
    """
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha()]
    pos_tags = pos_tag(tokens)
    tokens = [
        lemmatizer.lemmatize(word, get_wordnet_pos(pos)) for word, pos in pos_tags
    ]
    return " ".join(word for word in tokens if word not in stop_words and len(word) > 1)


@st.cache_data
def get_wordnet_pos(treebank_tag):
    """Map POS tag to the format used by WordNetLemmatizer.

    :param treebank_tag: POS tag in Treebank format
    :type treebank_tag: str
    :return: Corresponding WordNet POS tag
    :rtype: str
    """
    if treebank_tag.startswith("J"):
        return wordnet.ADJ
    if treebank_tag.startswith("V"):
        return wordnet.VERB
    if treebank_tag.startswith("N"):
        return wordnet.NOUN
    if treebank_tag.startswith("R"):
        return wordnet.ADV
    return wordnet.NOUN


@st.cache_data
def extract_title_and_content(content):
    """Extract the title from the content and return the remaining content.

    :param content: Full document content
    :type content: str
    :return: Tuple containing the title and the remaining content
    :rtype: tuple
    """
    lines = content.splitlines()
    for i, line in enumerate(lines):
        line = html.unescape(line.strip())
        if line.isupper():
            title = html.unescape(line.strip())
            return title, "\n".join(lines[i + 1 :])
    return "Untitled Document", content


@st.cache_data
def load_corpus_data(directory="mycorpus"):
    """Load and preprocess corpus data from a directory.

    :param directory: Path to the directory containing corpus files
    :type directory: str
    :return: DataFrame containing corpus data
    :rtype: pandas.DataFrame
    """
    directory = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../", directory)
    )
    if not os.path.exists(directory):
        st.error(f"The directory '{directory}' does not exist.")
        return pd.DataFrame(
            columns=[
                "Document ID",
                "Title",
                "Content",
                "Processed Content",
                "Word Count",
            ]
        )

    corpus_data = []
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            try:
                with open(file_path, "r", encoding="utf-8", errors="replace") as file:
                    content = file.read()
                    relative_path = os.path.relpath(file_path, directory)
                    title, content_without_title = extract_title_and_content(content)
                    corpus_data.append(
                        {
                            "Document ID": relative_path,
                            "Title": title,
                            "Content": content_without_title,
                        }
                    )
            except (IOError, OSError) as error:
                logging.error("Error reading file %s: %s", file_path, error)

    if not corpus_data:
        st.warning(f"No valid text files found in the directory '{directory}'.")
        return pd.DataFrame(
            columns=[
                "Document ID",
                "Title",
                "Content",
                "Processed Content",
                "Word Count",
            ]
        )

    corpus_df = pd.DataFrame(corpus_data)
    corpus_df["Processed Content"] = corpus_df["Content"].apply(preprocess_text)
    corpus_df["Word Count"] = corpus_df["Content"].apply(lambda x: len(x.split()))
    return corpus_df


@st.cache_data
def remove_duplicates(corpus_df):
    """Remove duplicate documents from the corpus.

    :param corpus_df: DataFrame containing the corpus
    :type corpus_df: pandas.DataFrame
    :return: DataFrame with duplicates removed
    :rtype: pandas.DataFrame
    """
    return corpus_df.drop_duplicates(subset="Content", keep="first").reset_index(
        drop=True
    )


def generate_snippet(content, sentence_count=1):
    """Generate a snippet by extracting the first few sentences.

    :param content: Full document content
    :type content: str
    :param sentence_count: Number of sentences to include in the snippet
    :type sentence_count: int
    :return: Snippet containing the first few sentences
    :rtype: str
    """
    sentences = content.split(". ")
    return ". ".join(sentences[:sentence_count]) + (
        "." if len(sentences) > sentence_count else ""
    )


def generate_relevant_snippet(content, query_terms, snippet_length=30):
    """Generate a snippet containing the most relevant part of the content.

    :param content: Full document content
    :type content: str
    :param query_terms: List of query tokens
    :type query_terms: list
    :param snippet_length: Length of the snippet in words
    :type snippet_length: int
    :return: Relevant snippet
    :rtype: str
    """
    words = content.split()
    for i, word in enumerate(words):
        if word.lower() in query_terms:
            start = max(0, i - snippet_length // 2)
            end = min(len(words), i + snippet_length // 2)
            return " ".join(words[start:end])
    return " ".join(words[:snippet_length])


@st.cache_data
def format_content_as_markdown(content, tokens_to_highlight):
    """Format content as Markdown and highlight query terms.

    :param content: Full document content
    :type content: str
    :param tokens_to_highlight: List of query tokens
    :type tokens_to_highlight: list
    :return: Formatted content with highlighted query terms
    :rtype: str
    """
    content = re.sub(r"([_*~`])", r"\\\1", content)
    content = re.sub(r"\n", "", content)
    for highlight_token in tokens_to_highlight:
        content = re.sub(
            rf"(?i)\b{re.escape(highlight_token)}\b",
            f"**{highlight_token.upper()}**",
            content,
        )
    return content


with st.spinner("Loading corpus data..."):
    df = load_corpus_data()
    df = remove_duplicates(df)
    df = df[
        ~df.apply(lambda row: row.astype(str).str.contains(".DS_Store").any(), axis=1)
    ]

with st.sidebar:
    st.title("Corpus Filters")
    st.write("Use the options below to filter the corpus data:")
    filterable_columns = [
        col for col in df.columns if col not in ["Word Count", "Processed Content"]
    ]
    columns_to_filter = st.multiselect(
        "Select columns to filter by:", filterable_columns
    )
    case_sensitive = st.checkbox("Case sensitive search", value=False)
    filter_values = {
        col: st.text_input(f"Enter a value to filter '{col}' by:")
        for col in columns_to_filter
    }
    apply_word_count_filter = st.checkbox("Filter by Word Count")
    min_word_count, max_word_count = 0, df["Content"].str.split().str.len().max()
    if apply_word_count_filter:
        min_word_count, max_word_count = st.slider(
            "Select word count range:",
            min_value=0,
            max_value=max_word_count,
            value=(0, max_word_count),
        )


@st.cache_data
def search_corpus(search_query, corpus_df):
    """Search the corpus for a query and return matching results.

    :param search_query: User's search query
    :type search_query: str
    :param corpus_df: DataFrame containing the corpus
    :type corpus_df: pandas.DataFrame
    :return: DataFrame containing search results
    :rtype: pandas.DataFrame
    """
    local_query_tokens = preprocess_text(search_query).split()
    results = []
    for _, row in corpus_df.iterrows():
        content_tokens = row["Processed Content"].split()
        match_count = sum(1 for token in local_query_tokens if token in content_tokens)
        if match_count > 0:
            relevant_snippet = generate_relevant_snippet(
                row["Content"], local_query_tokens
            )
            results.append(
                {
                    "Document ID": row["Document ID"],
                    "Snippet": relevant_snippet,
                    "Relevance": match_count,
                }
            )
    return pd.DataFrame(results).sort_values(by="Relevance", ascending=False)


with st.spinner("Applying filters..."):
    filtered_df = df
    if any(filter_values.values()) or (
        apply_word_count_filter
        and (
            min_word_count > 0
            or max_word_count < df["Content"].str.split().str.len().max()
        )
    ):
        for column, value in filter_values.items():
            if value:
                filtered_df = filtered_df[
                    filtered_df[column]
                    .astype(str)
                    .str.contains(value, case=case_sensitive, na=False)
                ]
        if apply_word_count_filter:
            filtered_df = filtered_df[
                filtered_df["Content"]
                .str.split()
                .str.len()
                .between(min_word_count, max_word_count)
            ]

with st.expander("Explore Corpus Data"):
    if query:
        search_results = search_corpus(query, filtered_df)
        if not search_results.empty:
            matching_ids = search_results["Document ID"].tolist()
            filtered_results = filtered_df[
                filtered_df["Document ID"].isin(matching_ids)
            ]
            st.success(
                f"Found {len(filtered_results)} documents matching the search results."
            )
            st.write(filtered_results)
        else:
            st.warning("No matching documents found for the search query.")
    else:
        if not filtered_df.empty:
            st.success(f"Found {len(filtered_df)} documents matching the filters.")
            st.write(filtered_df)
        else:
            st.warning("No documents match the applied filters.")


def output_corpus(output_path="corpus_output.txt"):
    """Export the corpus to a text file.

    :param output_path: Path to the output file
    :type output_path: str
    """
    with open(output_path, "w", encoding="utf-8") as file:
        for _, document_row in df.iterrows():
            file.write(f"Document ID: {document_row['Document ID']}\n")
            file.write(document_row["Content"] + "\n\n")


if st.button("Export Corpus"):
    output_corpus()
    st.success("Corpus successfully exported to corpus_output.txt!")

if query:
    with st.spinner("Searching the corpus..."):
        search_results = search_corpus(query, filtered_df)
    if not search_results.empty:
        st.write("Search Results:")
        st.success(f"Found {len(search_results)} relevant documents.")
        for _, result_row in search_results.iterrows():
            query_tokens = preprocess_text(query).split()
            snippet = result_row["Snippet"]
            doc_row = df[df["Document ID"] == result_row["Document ID"]]
            extracted_document_title = doc_row.iloc[0].get("Title", "Untitled Document")
            document_content = doc_row.iloc[0]["Content"]
            formatted_content = format_content_as_markdown(
                document_content, query_tokens
            )

            if any(token in snippet.lower() for token in query_tokens):
                for token in query_tokens:
                    snippet = re.sub(
                        rf"(?i)\b{re.escape(token)}\b",
                        f"<span style='color: red; font-weight: bold;'>{token.upper()}</span>",
                        snippet,
                    )
                snippet_display = f"**Snippet:** {snippet}"
            else:
                matched_tokens = ", ".join(query_tokens[:5])
                snippet_display = (
                    f"**No snippet with exact match. Matched Tokens:** {matched_tokens}"
                )

            with st.expander(
                f"Title: {extracted_document_title} (Relevance: {result_row['Relevance']})"
            ):
                st.markdown(snippet_display, unsafe_allow_html=True)
                st.markdown(f"**Document ID:** {result_row['Document ID']}")
                st.markdown(f"**Content:**\n\n{formatted_content}")
    else:
        st.warning("No matching documents found. Please try a different query.")
