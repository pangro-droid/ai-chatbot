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
                background: linear-gradient(135deg, #5a6fa8 0%, #7b8fc4 25%, #99aed9 50%, #7b8fc4 75%, #5a6fa8 100%);
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
        
    /* Bold white text for all content */
    * {
        color: white !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Title
st.title('💬 AI Chatbot')         
# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get AI response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True
        )
        
        # Stream the response
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with info and clear button
with st.sidebar:
    st.header("About")
    st.info(
        "This is a simple AI chatbot powered by OpenAI's GPT-4o-mini model. "
        "Ask me anything!"
    )
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
