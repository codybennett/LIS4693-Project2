"""LIS4693 - IR & Text Mining - Project 2

* The project involves developing and implementing a data a collection tool
  for creating/generating various corpus documents.
* This module utilizes the Reuters corpus which inlcudes over 10,000 documents


:Date: 2025-03-02
:Version: 2
:Authors: - Cody Bennett
            - codybennett@ou.edu

"""

from pathlib import Path

import nltk

import log_config

logger = log_config.create_logger()

nltk.download("reuters", quiet=True)

corpus = nltk.corpus.reuters

# Collect all documents containing > 50 words
tmp_documents = [
    tmp_document for tmp_document in corpus.fileids() if len(corpus.words(tmp_document)) > 50
]

class DataCollector:
    def __init__(self):
        """Retrieves Reuters corpus documents longer than 50 words."""
        logger.debug("Initializing DataCollector and downloading Reuters Corpus")
        logger.info(f"Retrieving {len(tmp_documents)} documents matching criteria")

        # Initialize metadata dictionary
        self.document_metadata = {}
        self.documents = tmp_documents

        # Process documents
        for fileid in tmp_documents:
            doc_root = fileid.split("/")[0]
            # Create directory tree if needed
            if doc_root not in self.document_metadata:
                Path(f"mycorpus/{doc_root}").mkdir(parents=True, exist_ok=True)
                self.document_metadata[doc_root] = {"num_documents": 0, "num_words": 0}

            # Update metadata
            self.document_metadata[doc_root]["num_documents"] += 1
            self.document_metadata[doc_root]["num_words"] += len(corpus.words(fileid))

        logger.info(f"Corpus Metadata: {self.document_metadata}")

    def get_documents(self):
        """Returns documents in the corpus."""
        return self.documents

    def get_metadata(self):
        """Returns metadata for the corpus."""
        return self.document_metadata

    def get_document(self, fileid):
        """Returns the specified document."""
        if fileid in self.documents:
            return corpus.raw(fileid)
        logger.error(f"Document {fileid} not found in corpus.")
        return None

    def get_word_count(self, fileid):
        """Returns the word count for the specified document."""
        if fileid in self.documents:
            return len(corpus.words(fileid))
        logger.error(f"Document {fileid} not found in corpus.")
        return None
