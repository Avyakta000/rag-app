# RAG Application Backend

## Overview

This repository contains the backend code for a Retrieval-Augmented Generation (RAG) application. The backend is built using FastAPI and integrates with Hugging Face, Chroma DB, and Langchain for text processing and question answering.

## Features

- **File Upload:** Allows uploading of files (e.g., PDFs) for processing.
- **Question Answering:** Processes uploaded files and answers questions based on the content.
- **Text Extraction:** Extracts text from uploaded documents.
- **Text Embedding:** Uses Hugging Face embeddings for document processing.
- **Question Retrieval:** Utilizes Chroma DB for efficient question retrieval.

## Technologies Used

- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **Hugging Face:** Provides pre-trained models for various NLP tasks.
- **Chroma DB:** Vector database for storing and retrieving text embeddings.
- **Langchain:** Tool for managing language model interactions and document processing.
- **SQLAlchemy:** ORM for database interactions (has not been utilized yet).

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)
- Virtual Environment (recommended)

### Setup

 **Clone the Repository**

   ```bash
   git clone https://github.com/Avyakta000/rag-app.git
 
