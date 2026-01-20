## AI Restaurant Idea Generator using LangChain and Streamlit

**This project is an AI-powered web application that generates unique restaurant names and signature menu ideas based on the selected cuisine.**
**It uses Google's Gemini model through LangChain and provides an interactive user interface built with Streamlit.**

**The application allows users to choose a cuisine and instantly receive creative restaurant branding ideas powered by Generative AI.**

## Project Components

## User Interface
Built using Streamlit for fast interactive web UI.
Sidebar allows users to select cuisine.
Displays AI-generated restaurant name and menu items.

## AI Engine
Uses LangChain framework.
Integrates Google Gemini (gemini-2.5-flash).
Prompt templates dynamically generate content.

## Environment Management
Uses python-dotenv for secure API key handling.
Environment variables stored in .env file.

## Project Structure

## app.py
Main Streamlit application.

## langchain_helper.py
Handles AI model initialization and prompt chaining.

## .env
Stores Google API key securely.

## requirements.txt
Project dependencies.

## .gitignore
Ignored files configuration.

## Features
Generates unique restaurant names automatically.
Generates 5-item signature menus.
Supports multiple cuisines (Indian, Italian, Mexican, Japanese, Turkish).
Interactive UI with live AI responses.
Secure environment variable handling.
Fast response using Gemini Flash model.

## Tech Stack
Language: Python
Framework: Streamlit
AI Framework: LangChain
LLM: Google Gemini
Environment Management: python-dotenv
Prompt Engineering: LangChain PromptTemplate

Installation

## Step 1: Create virtual environment
python -m venv venv
Activate on Windows:
venv\Scripts\activate

## Step 2: Install dependencies
pip install -r requirements.txt

## Step 3: Setup environment variables
Create a file named .env in the project root.
Add your Google API key:
google_api_key=YOUR_API_KEY_HERE

## Run the Application
streamlit run app.py
Open the browser link shown in the terminal.

## Output
User selects a cuisine from sidebar.
AI generates a restaurant name.
AI generates five menu items.
Results display instantly in the UI.

## Future Improvements
Add more cuisine categories.
Add image generation for dishes.
Deploy on cloud platform.
Add user feedback scoring.
Improve UI styling.

## Author

**Name:** Nishant Nirmal
**Field:** Computer Science Engineering | AI | Machine Learning | Data Engineering |
**Email:** nishant4245@gmail.com
**LinkedIn:** https://www.linkedin.com/in/nishant-nirmal-2198b52a7
**GitHub:** https://github.com/NishantNirmalSingh