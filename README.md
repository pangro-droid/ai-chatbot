# 💬 AI Chatbot

A simple, modern AI chatbot built with Streamlit and OpenAI's GPT-4o-mini model. Features real-time streaming responses and a clean, intuitive interface.

## ✨ Features

- 🗨️ **Real-time chat interface** with streaming responses
- 🤖 **Powered by OpenAI GPT-4o-mini** for intelligent conversations
- 💾 **Session-based chat history** that persists during your session
- 🎯 **Clean and modern UI** built with Streamlit
- ⚡ **Fast and responsive** with minimal setup required

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### Installation

1. Clone this repository:
```bash
git clone https://github.com/pangro-droid/ai-chatbot.git
cd ai-chatbot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.streamlit/secrets.toml` file in the project root:
```toml
OPENAI_API_KEY = "your-api-key-here"
```

4. Run the app:
```bash
streamlit run app.py
```

## 🌐 Deploy to Streamlit Cloud

1. Fork this repository to your GitHub account
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" and select your forked repository
4. Add your OpenAI API key in the Streamlit Cloud secrets:
   - Go to App settings → Secrets
   - Add: `OPENAI_API_KEY = "your-api-key-here"`
5. Click "Deploy"!

## 📝 Usage

1. Open the app in your browser
2. Type your message in the chat input at the bottom
3. Watch as the AI responds in real-time
4. Use the "Clear Chat History" button in the sidebar to start fresh

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io)** - Web framework for the UI
- **[OpenAI API](https://openai.com)** - AI model for chat responses
- **Python 3.8+** - Programming language

## 💻 Project Structure

```
ai-chatbot/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## ⚙️ Configuration

You can customize the chatbot by modifying `app.py`:

- **Model**: Change `model="gpt-4o-mini"` to use a different OpenAI model
- **Streaming**: Set `stream=False` to disable real-time streaming
- **UI**: Modify the Streamlit components to customize the appearance

## 🔒 Security

- Never commit your API key to version control
- Always use Streamlit secrets or environment variables for sensitive data
- The `.gitignore` file is configured to exclude secrets files

## 👤 Author

**pangro-droid**

## 📝 License

This project is open source and available for anyone to use and modify.
