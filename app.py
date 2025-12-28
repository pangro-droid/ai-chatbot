import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="AI Chatbot",
    page_icon="💬",    layout="wide"
)

# Custom CSS for space-themed background
st.markdown("""
    <style>
    /* Main app background with space gradient */
    .stApp {
        background: linear-gradient(135deg, #0c0e27 0%, #1a1b3d 25%, #2d1b4e 50%, #1a1b3d 75%, #0c0e27 100%);
        background-attachment: fixed;
    }
    
    /* Animated stars */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: 
            radial-gradient(2px 2px at 20% 30%, white, transparent),
            radial-gradient(2px 2px at 60% 70%, white, transparent),
            radial-gradient(1px 1px at 50% 50%, white, transparent),
            radial-gradient(1px 1px at 80% 10%, white, transparent),
            radial-gradient(2px 2px at 90% 60%, white, transparent),
            radial-gradient(1px 1px at 33% 80%, white, transparent),
            radial-gradient(1px 1px at 15% 90%, white, transparent);
        background-size: 200% 200%;
        animation: stars 60s linear infinite;
        pointer-events: none;
        z-index: 0;
    }
    
    /* Planet decoration */
    .stApp::after {
        content: '';
        position: fixed;
        bottom: -100px;
        right: -100px;
        width: 400px;
        height: 400px;
        background: radial-gradient(circle at 30% 30%, #4a5f8f, #1a2332);
        border-radius: 50%;
        box-shadow: 0 0 100px rgba(74, 95, 143, 0.4);
        z-index: 0;
    }
    
    /* More visible stars */
    .stApp::before {
        box-shadow:
            100px 100px white,
            200px 150px white,
            300px 250px white,
            400px 100px white,
            500px 300px white,
            600px 200px white,
            700px 400px white,
            800px 150px white,
            900px 350px white,
            1000px 250px white,
            150px 450px white,
            250px 350px white,
            350px 500px white,
            450px 400px white,
            550px 550px white,
            650px 450px white,
            750px 600px white,
            850px 500px white;
        width: 2px;
        height: 2px;
        background: white;
        border-radius: 50%;
    }
    
    @keyframes stars {
        0% { background-position: 0% 0%; }
        100% { background-position: 100% 100%; }
    }
    
    /* Make content visible on top of background */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 15, 35, 0.85);
        backdrop-filter: blur(10px);
    }
    
    /* Chat messages styling */
    .stChatMessage {
        background-color: rgba(30, 30, 60, 0.7) !important;
        backdrop-filter: blur(5px);
        border-radius: 10px;
    }
    
    /* Input box styling */
    .stChatInputContainer {
        background-color: rgba(20, 20, 40, 0.8);
        backdrop-filter: blur(5px);
    }
    
    
    /* Force white text on ALL elements */
    .stApp, .stApp * {
        color: #ffffff !important;
    }
    
    /* Title styling */
    h1 {
        color: #ffffff !important;
        text-shadow: 0 0 20px rgba(255, 255, 255, 0.5);
    }
    
    /* Chat message text */
    .stChatMessage, .stChatMessage *, [data-testid="stChatMessage"], [data-testid="stChatMessage"] * {
        color: #ffffff !important;
    }
    
    /* Sidebar text */
    [data-testid="stSidebar"], [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
