# Instagram Viral Writing Assistant

## Overview

The Instagram Viral Writing Assistant is a Python-based application designed to help users generate engaging and viral content for Instagram. Using OpenAI's language model, this tool allows users to input a theme and receive creative titles and content tailored for social media.

<img width="325" alt="image" src="https://github.com/user-attachments/assets/29950d86-4624-4ff8-b66c-0145fb7b1eea">


## Features

- Generate 5 catchy Instagram titles with emoji expressions.
- Create a main post content based on the provided theme.
- Easy integration with OpenAI's API for content generation.
- User-friendly interface built with Streamlit.

## Requirements

To run this project, you need the following:

- Python 3.7 or higher
- Streamlit
- LangChain
- OpenAI Python client
- Pydantic

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amaris72/instagram-viral-writing-assistant.git
   cd instagram-viral-writing-assistant
   ```

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Obtain your OpenAI API key** from [OpenAI](https://platform.openai.com/account/api-keys).

## Usage

1. **Run the Streamlit application:**
   ```bash
   streamlit run main_ins.py
   ```

2. **Open your web browser** and go to `http://localhost:8501`.

3. **Enter your OpenAI API key** and the topic you want to generate content for.

4. **Click on "Start writing"** to generate your Instagram content!

## Code Structure

- **`main_ins.py`**: Main application file that runs the Streamlit interface.
- **`utils_ins.py`**: Contains the function to generate Instagram content using OpenAI.
- **`prompt_template_ins.py`**: Defines the system and user prompts for generating content.
- **`ins_model.py`**: Defines the data model for Instagram content using Pydantic.
