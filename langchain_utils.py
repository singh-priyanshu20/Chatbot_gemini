from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from config import GOOGLE_API_KEY

# Initialize Google Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    google_api_key=GOOGLE_API_KEY,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Define Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a chatbot"),
    ("human", "Question: {question}")
])

# Output Parser
output_parser = StrOutputParser()

# Create Processing Chain
chain = prompt | llm | output_parser

def generate_response(user_input):
    """Processes input through LangChain and returns response."""
    return chain.invoke({'question': user_input})
