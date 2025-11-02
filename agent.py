import os
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from tools import WikipediaSearchTool, DuckDuckGoSearchTool


class BlogAgent:
    def __init__(self):
        """Initialize the blog generation agent with LLM and tools."""
        # Initialize Groq LLM
        self.llm = ChatGroq(
            temperature=0.7,
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
        )

        # Initialize tools
        self.wiki_tool = WikipediaSearchTool()
        self.ddg_tool = DuckDuckGoSearchTool()

    def generate_blog(self, topic: str) -> str:
        """Generate a blog post on the given topic."""
        try:
            # Step 1: Research using Wikipedia
            print(f"📚 Searching Wikipedia for: {topic}")
            wiki_info = self.wiki_tool.search(topic)

            # Step 2: Research using DuckDuckGo
            print(f"🔍 Searching DuckDuckGo for: {topic}")
            web_info = self.ddg_tool.search(topic, max_results=3)

            # Step 3: Generate blog using gathered information
            print(f"✍️ Generating blog post...")
            blog_prompt = PromptTemplate(
                input_variables=["topic", "wiki_info", "web_info"],
                template="""You are an expert blog writer. Using the research information provided below, write a comprehensive, well-structured blog post.

Topic: {topic}

Wikipedia Research:
{wiki_info}

Web Search Results:
{web_info}

Write a professional blog post with the following structure:

1. **Heading**: Use # markdown format with an engaging title related to the topic
2. **Introduction**: Write 2-3 engaging paragraphs that introduce the topic and hook the reader
3. **Main Content**: Write 4-6 detailed sections with ## subheadings covering different aspects of the topic. Use the research information to provide facts, examples, and insights.
4. **Summary/Conclusion**: Write 2-3 paragraphs that summarize the key points and provide closing thoughts

Requirements:
- Use markdown formatting (headings, bold, italics where appropriate)
- Write in a professional yet engaging tone
- Aim for 600-1000 words total
- Include specific facts and details from the research
- Make it informative and interesting to read
- Use proper paragraph breaks for readability

Write the complete blog post now:""",
            )

            chain = LLMChain(llm=self.llm, prompt=blog_prompt)
            blog_content = chain.run(
                topic=topic, wiki_info=wiki_info, web_info=web_info
            )

            return blog_content.strip()

        except Exception as e:
            raise Exception(f"Error generating blog: {str(e)}")
