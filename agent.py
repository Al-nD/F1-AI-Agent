from dotenv import load_dotenv
import os
from langchain.sql_database import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_sql_agent

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables. Please set it in the .env file.")

db = SQLDatabase.from_uri("sqlite:///f1db.db")
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
)

agent_executor = create_sql_agent(
    llm=llm,
    db=db,
    agent_type="openai-tools",
    verbose=True,
)

question = "What is the most recent race where Max Verstappen finished 1st"
response = agent_executor.run(question)
print(response)
