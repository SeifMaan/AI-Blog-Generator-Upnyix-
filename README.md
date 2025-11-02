# AI Blog Generator

An intelligent blog generation system that uses LangChain agents to research topics and create well-structured blog posts.

## Features

- 🤖 **AI-Powered Research**: Uses Wikipedia and DuckDuckGo for comprehensive topic research
- ✍️ **Structured Output**: Generates blogs with proper heading, introduction, content, and summary
- 🎨 **Clean UI**: Simple Streamlit interface with example topics
- 📋 **Easy Export**: Copy to clipboard and download as Markdown (.md)
- 🚀 **Fast & Free**: Uses Groq's Llama 3.1 70B model (free tier available)

## Prerequisites

- Python 3.8 or higher
- Groq API key (free from [console.groq.com](https://console.groq.com))

## Installation

1. **Clone or extract the project**

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Set up environment variables**
   - Copy `.env.example` to `.env`
   - Add your Groq API key:

```
GROQ_API_KEY=your_actual_api_key_here
```

## Getting Your Groq API Key

1. Visit [console.groq.com](https://console.groq.com)
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

## Usage

1. **Run the application**

```bash
streamlit run app.py
```

2. **Generate a blog**

   - Enter a topic in the input field, or
   - Click on one of the example topics in the sidebar
   - Click "Generate Blog"
   - Wait for the AI to research and write (30-60 seconds)

3. **Export your blog**
   - Use "Copy to Clipboard" to copy the content
   - Use "Download .md" to save as a Markdown file

## Project Structure

```
blog-generator/
├── app.py              # Streamlit UI application
├── agent.py            # LangChain agent implementation
├── tools.py            # Wikipedia & DuckDuckGo tools
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .env               # Your actual environment variables (create this)
└── README.md          # This file
```

## How It Works

1. **Agent Architecture**: Uses LangChain's ReAct agent pattern
2. **Research Phase**: Agent searches Wikipedia and DuckDuckGo for information
3. **Generation Phase**: Llama 3.1 70B synthesizes research into a structured blog
4. **Output Format**: Markdown with heading, introduction, content sections, and summary

## Technologies Used

- **LangChain**: Agent orchestration and tool management
- **Groq**: Fast LLM inference (Llama 3.1 70B)
- **Wikipedia API**: Factual information retrieval
- **DuckDuckGo Search**: Web search capabilities
- **Streamlit**: User interface

## Example Topics

- Artificial Intelligence in Healthcare
- Climate Change Solutions
- Future of Quantum Computing
- Sustainable Energy Technologies
- Space Exploration Advances
- And more in the sidebar!

## Troubleshooting

**Issue**: "GROQ_API_KEY not found"

- **Solution**: Make sure you created a `.env` file with your API key

**Issue**: "Module not found"

- **Solution**: Run `pip install -r requirements.txt`

**Issue**: "Rate limit exceeded"

- **Solution**: Groq free tier has rate limits. Wait a moment and try again

**Issue**: Blog generation is slow

- **Solution**: This is normal. The agent needs time to research (Wikipedia + DuckDuckGo) and generate content. Typically takes 30-60 seconds.

## Challenges Encountered

1. **Search Tool Integration**: Needed to handle various edge cases (disambiguation pages, no results, timeouts)
2. **Agent Prompt Engineering**: Refined prompt to ensure consistent blog structure
3. **Error Handling**: Added robust error handling for API failures and network issues

## Future Improvements

- Add more search engines (Bing, Google Custom Search)
- Implement blog tone selection (formal, casual, technical)
- Add length control (short, medium, long)
- Support multiple languages
- Cache search results to reduce API calls
- Add image suggestion capabilities

## License

This project is open source and available for educational purposes.

## Credits

Built with LangChain, Groq, Wikipedia API, and DuckDuckGo Search.
