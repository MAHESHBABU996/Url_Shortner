# 🔗URL Shortener

A simple Python project that shortens long URLs using the **pyshorteners** library and **TinyURL** service. This tool automatically adds `https://` if it's missing and generates a shortened link in seconds. 🚀

---

## ✨ Features

- 🔗 Shorten long URLs instantly
- 🌐 Uses the TinyURL service
- ⚡ Automatically adds `https://` if omitted
- 💻 Simple command-line interface
- 🐍 Beginner-friendly Python project

---

## 📋 Requirements

- 🐍 Python 3.8 or higher
- 🌐 Internet connection
- 📦 `pyshorteners`

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/python-url-shortener.git
cd python-url-shortener
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the program:

```bash
python app.py
```

Example:

```text
Enter URL:
google.com

Short URL:
https://tinyurl.com/xxxxx
```

You can also enter a complete URL:

```text
Enter URL:
https://www.python.org

Short URL:
https://tinyurl.com/yyyyy
```

---

## 📁 Project Structure

```
python-url-shortener/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. 📝 Accepts a URL from the user.
2. 🔍 Checks whether the URL starts with `http` or `https`.
3. ➕ Automatically adds `https://` if needed.
4. 🔗 Sends the URL to TinyURL using the `pyshorteners` library.
5. ✅ Displays the shortened URL.

---

## 📌 Example

**Input**

```text
github.com
```

**Output**

```text
Short URL:
https://tinyurl.com/abc123
```

---

## ❗ Error Handling

If an invalid URL is entered or there is no internet connection, the program displays an error message instead of crashing.

Example:

```text
Error: <error message>
```

---

## 🤝 Contributing

Contributions are welcome! 🎉

1. 🍴 Fork the repository
2. 🌿 Create a new branch
3. 💻 Make your changes
4. 📤 Submit a Pull Request

---

## 📄 License

📝 This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 📢 Share it with others

Happy Coding! 🚀🐍
