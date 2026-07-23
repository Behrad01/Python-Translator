# 🌍 Translator

This program is a very lightweight and fast command-line translator built with **Python** and powered by the **DeepL API**. This application translates text into more than 35 languages through a clean and user-friendly terminal interface. The main file of this application is translator.py and the secondary file is languages.py which is imported into translator.py, I seperated them to make the code look more readable and easier to understand.

---

## 📸 Demo

<img width="896" height="804" alt="image" src="https://github.com/user-attachments/assets/d91aa0cf-b0b1-4a71-a49e-04f39f0946d5" />

<img width="600" height="357" alt="image" src="https://github.com/user-attachments/assets/12ca8c0b-08c4-4bc5-9f67-c3e6b8d19087" />

---

## ✨ Features

- 🌍 Translate text into **35+ languages**
- 🔎 Accepts both language codes (e.g. `FR`) and language names (e.g. `French`)
- ⚡ Fast translations using the DeepL API
- ⏳ Animated loading spinner while the translation is processed
- ✅ Input validation with clear error messages
- 💻 Simple command-line interface
- 📦 Lightweight with minimal dependencies

---

## 🛠️ Built With

- Python 3.12+
- Requests
- DeepL API

---

## 📂 Project Structure

```text
translator/
│
├── translator.py        # Main application
├── languages.py         # Supported languages
├── requirements.txt
├── README.md
├── LICENSE
```

## 🔑 API

This project uses the **DeepL API** to perform translations.

To use the application, you'll need your own free DeepL API key.

You can create one by signing up at:

https://www.deepl.com/pro-api

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Behrad01/translator.git
cd translator
```

### 2. Install the required package

```bash
pip install -r requirements.txt
```

### 3. Configure your API key

Open `translator.py` and replace:

```python
API_KEY = "Put your API key here"
```

with your own DeepL API key.

You can obtain a free API key from the DeepL API website.

---

## ▶️ Running the Program

Run the application with:

```bash
python translator.py
```

---

## 🌐 Supported Languages

The translator supports over **35 languages** provided by the DeepL API, including:

- English
- French
- German
- Spanish
- Portuguese
- Italian
- Dutch
- Japanese
- Korean
- Chinese
- Arabic
- Russian
- Ukrainian
- Turkish

and many more.

---

## 📋 Requirements

- Python 3.12 or newer
- Internet connection
- DeepL API key

---

## 📄 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👤 Author

**Behrad**

GitHub: https://github.com/Behrad01
