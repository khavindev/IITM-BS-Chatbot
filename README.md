# IIT Madras BS Degree Chatbot

## Note: This project is not affiliated with or endorsed by IIT Madras. It is an independent project developed to assist prospective and current students of the IIT Madras BS degree program.

This repository contains a chatbot designed to answer any questions related to the IIT Madras BS degree program. The chatbot is built using the Google Generative API and Streamlit.

## Features

- **Interactive Q&A:** The chatbot can respond to a wide range of queries related to the IIT Madras BS degree program.
- **Real-time Responses:** Leveraging Google Generative API for generating accurate and relevant answers.
- **User-friendly Interface:** Built with Streamlit to provide a simple and intuitive user interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your machine.
- Access to Google Generative API.
- Streamlit library installed (`pip install streamlit`).

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/iit-madras-bs-chatbot.git
    cd iit-madras-bs-chatbot
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Set up the Google Generative API:
    - Sign up and get access to the Google Generative API.
    - Set up your API key and save it in an environment variable or a configuration file.
    - paste the database.txt in system instructions
    - set the model to gemini-1.5-flash

## Usage

To run the chatbot, navigate to the project directory and execute the following command:

```sh
streamlit run app.py
```

This will start a local server, and you can interact with the chatbot via your web browser.

##Project Structure

```sh
iit-madras-bs-chatbot/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md           # Project readme file
└── databasetxt.txt     #prompt/system_instructions
```

##License
This project is under a private license. The code is proprietary and not for public use. Only authorized individuals with explicit permission are allowed to access and use the code.

##Contact
If you have any questions or suggestions, feel free to reach out to the project maintainer:

LinkedIn: https://www.linkedin.com/in/s-khavin73/ \n
GitHub: khavindev





