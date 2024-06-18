# Chatbot using Google Generative AI

This project demonstrates a simple conversational chatbot using Google's Generative AI API. The chatbot can interact with users in a conversational manner, providing responses based on the input messages.

## Setup

Before running the chatbot, make sure you have the necessary packages and API key configured.

### Prerequisites

- Python 3.x
- Google Generative AI API Key

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/chatbot-google-generative-ai.git
    cd chatbot-google-generative-ai
    ```

2. Install the required Python packages:
    ```sh
    pip install google-generativeai
    ```

3. Set up your API key. Replace `YOUR_API_KEY` with your actual API key in the script:
    ```python
    API_KEY = 'YOUR_API_KEY'
    ```

## Usage

1. Run the chatbot script:
    ```sh
    python chatbot.py
    ```

2. Start the conversation by typing your message. To end the conversation, type `bye`.

### Example:

```plaintext
You: Hello!
Chatbot: Hi there! How can I help you today?
You: What's the weather like?
Chatbot: I'm sorry, I don't have real-time access to weather data at the moment.
You: bye
Chatbot: Goodbye!
