from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from config import GOOGLE_API_KEY

# Personality Modes
PERSONA_TEMPLATES = {
    "Friendly": "You are a kind and helpful chatbot, responding in a cheerful tone.",
    "Professional": "You are a knowledgeable and formal assistant providing concise answers.",
    "Humorous": "You are a witty chatbot that responds with humor.",
}

def get_prompt_template(persona):
    """Returns a dynamic prompt template based on persona selection."""
    system_message = PERSONA_TEMPLATES.get(persona, PERSONA_TEMPLATES["Friendly"])
    return ChatPromptTemplate.from_messages([
        ("system", system_message),
        ("human", "Question: {question}")
    ])

# Function to generate responses
def generate_response(user_input, persona="Friendly"):
    """Processes input through LangChain and returns response."""
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        google_api_key=GOOGLE_API_KEY,
        temperature=0.7,  # Slight randomness for creativity
        max_tokens=200,
        timeout=None,
        max_retries=2,
    )
    
    prompt = get_prompt_template(persona)
    output_parser = StrOutputParser()
    
    chain = prompt | llm | output_parser
    return chain.invoke({'question': user_input})
