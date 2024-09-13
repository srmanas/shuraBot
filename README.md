# Sekiro Chatbot

## Overview

**ShuraBot** is a local chatbot designed to assist players of *Sekiro: Shadows Die Twice*. Using OpenAI's GPT-4o-mini model, it provides detailed responses on various aspects of the game, including mechanics, lore, combat strategies, and technical issues. The project is built with Flask for the backend API and Streamlit for the user interface.

## Features

- **Game Mechanics**: Get detailed explanations and strategies for game mechanics.
- **Lore**: Learn about the game's lore and background.
- **Combat Strategies**: Receive tips and strategies for combat and boss fights.
- **Technical Support**: Find solutions to common game errors and issues.
- **User-Friendly UI**: A chat interface built with Streamlit for an intuitive experience.

## Installation

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/srmanas/shuraBot.git

2. Navigate to the project directory:

   ```bash
   cd shuraBot

3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4. Install required packages:

   ```bash
   pip install -r requirements.txt

**Running the Application**
1. Start the Flask server and run the Streamlit application:

   ```bash
   python app.py

2. Open your browser and go to http://localhost:8501 to interact with the chatbot.

----------------------------------------------------------------------------------------

**Usage**
Chat Interface: Use the Streamlit UI to ask questions and receive answers.
Suggestions: Select topics from the suggestions dropdown to get relevant information.
Contributing
Feel free to open issues or submit pull requests if you have suggestions or improvements.


**Acknowledgments**

OpenAI for providing the GPT-4o-mini model.

Streamlit and Flask for the frameworks used in this project.
