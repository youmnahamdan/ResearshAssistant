from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from app.core.config import llm
from dotenv import load_dotenv

load_dotenv()


def openai_with_structured_output(structured_output: BaseModel):
    return ChatOpenAI(model=llm).with_structured_output(structured_output)
