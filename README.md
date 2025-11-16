# 🌐 Real-Time Multilingual Query Handler
Minimal AI Pipeline for Language Detection, Translation & Auto-Response

This project is a simple multilingual support system that detects the language of an incoming user query, translates it into English, generates a predefined support response, and translates the response back to the user’s original language.

It provides real-time multilingual assistance with minimal infrastructure and lightweight NLP tools.

# Key Features

- Automatic language detection
- Translation to English & back to original language
- Rule-based customer support responses
- Lightweight, minimal-code AI pipeline
- User can input queries directly in any language
- Beginner-friendly, no heavy ML models required

# Technology Stack

Python

- deep-translator – for translating text
- langdetect – for detecting the query’s language
- langcodes – for converting language codes to readable names

# Project Structure
```
project-folder/
│
├── main.py
├── requirements.txt
└── README.md
```
Everything runs from main.py — no extra files are required.

# Installation
1. Clone the repository
```
git clone https://github.com/AneeshaIyer/multilingual_query_handler_hidevs.git
cd <your-repo>
```

2. Install dependencies
```
pip install -r requirements.txt
```

# How to Run

Run the script:
```
python main.py
```

You'll see:
```
=== Multilingual Translator ===

Example: ¿Dónde está mi pedido? → Where is my order?
```

Then you can type any query in any language.

Quit using:
```
q
```

# Example Usage
User Input:
```
¿Dónde está mi pedido?
```
Output:
```
Detected Language: Spanish
English Translation: where is my order

Response (English):
   You can track your order using the tracking number sent to your email.

Response (Spanish):
   Puede rastrear su pedido usando el número de seguimiento enviado a su correo electrónico.
```

# How It Works

1. Detects language of user input.

2. Translates input to English.

3. Chooses a response using simple keyword rules.

4. Translates response back to the original language.

5. Displays both English and original language responses


# Demo Video

# Contact
- Name: Aneesha Manjunath Iyer
- Email: aneeshamjk@gmail.com
- Github: https://github.com/AneeshaIyer
