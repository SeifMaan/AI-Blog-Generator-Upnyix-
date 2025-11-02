import streamlit as st
import os
from dotenv import load_dotenv
from agent import BlogAgent

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="AI Blog Generator", page_icon="✍️", layout="wide")

# Custom CSS
st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .blog-output {
        background-color: #f8f9fa;
        padding: 2rem;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        margin-top: 1rem;
    }
    .example-topic {
        padding: 0.5rem;
        margin: 0.3rem 0;
        background-color: #e7f3ff;
        border-radius: 5px;
        cursor: pointer;
        border: 1px solid #b3d9ff;
    }
    .example-topic:hover {
        background-color: #cce5ff;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Initialize session state
if "blog_content" not in st.session_state:
    st.session_state.blog_content = None
if "blog_topic" not in st.session_state:
    st.session_state.blog_topic = ""
if "show_copy" not in st.session_state:
    st.session_state.show_copy = False

# Header
st.markdown(
    '<div class="main-header">✍️ AI Blog Generator</div>', unsafe_allow_html=True
)
st.markdown(
    '<div class="sub-header">Generate comprehensive blogs using AI-powered research</div>',
    unsafe_allow_html=True,
)

# Sidebar with example topics
with st.sidebar:
    st.header("📚 Example Topics")
    st.markdown("Click on any topic to use it:")

    example_topics = [
        "Artificial Intelligence in Healthcare",
        "Climate Change Solutions",
        "Future of Quantum Computing",
        "Sustainable Energy Technologies",
        "Space Exploration Advances",
        "Blockchain Technology Applications",
        "Mental Health in Digital Age",
        "Electric Vehicle Revolution",
        "Cybersecurity Best Practices",
        "Virtual Reality in Education",
    ]

    for topic in example_topics:
        if st.button(topic, key=f"ex_{topic}", use_container_width=True):
            st.session_state.blog_topic = topic
            st.rerun()

    st.markdown("---")
    st.markdown("### About")
    st.info(
        "This system uses LangChain agents with Wikipedia and DuckDuckGo search to research and generate well-structured blog posts."
    )

# Main content area
col1, col2 = st.columns([3, 1])

with col1:
    topic_input = st.text_input(
        "Enter Blog Topic:",
        value=st.session_state.blog_topic,
        placeholder="e.g., The Impact of AI on Modern Education",
        key="topic_input",
    )

with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing
    generate_button = st.button(
        "🚀 Generate Blog", type="primary", use_container_width=True
    )

# Generate blog
if generate_button and topic_input:
    if not os.getenv("GROQ_API_KEY"):
        st.error("⚠️ GROQ_API_KEY not found! Please add it to your .env file.")
    else:
        with st.spinner(
            "🔍 Researching and generating your blog... This may take a minute."
        ):
            try:
                agent = BlogAgent()
                blog_content = agent.generate_blog(topic_input)
                st.session_state.blog_content = blog_content
                st.session_state.blog_topic = topic_input
                st.success("✅ Blog generated successfully!")
            except Exception as e:
                st.error(f"❌ Error generating blog: {str(e)}")
                st.session_state.blog_content = None

# Display blog output
if st.session_state.blog_content:
    st.markdown("---")

    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 4])

    with col1:
        # Download button
        filename = st.session_state.blog_topic.replace(" ", "_").lower() + ".md"
        st.download_button(
            label="💾 Download .md",
            data=st.session_state.blog_content,
            file_name=filename,
            mime="text/markdown",
            use_container_width=True,
        )

    # Blog content display
    st.markdown('<div class="blog-output">', unsafe_allow_html=True)
    st.markdown(st.session_state.blog_content)
    st.markdown("</div>", unsafe_allow_html=True)

    # Text area for copying (shown when copy button is clicked)
    if st.session_state.get("show_copy", False):
        st.info("👇 Select all text below (Ctrl+A / Cmd+A) and copy (Ctrl+C / Cmd+C)")
        st.text_area(
            "Copy this content:",
            value=st.session_state.blog_content,
            height=300,
            key="copy_area",
        )
        if st.button("✅ Done"):
            st.session_state.show_copy = False
            st.rerun()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>Powered by LangChain, Groq (Llama 3.1 70B), Wikipedia & DuckDuckGo</div>",
    unsafe_allow_html=True,
)
