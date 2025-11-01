from abc import ABC, abstractmethod
from typing import Any, Type, List
from pydantic import BaseModel
from langchain_core.prompts import PromptTemplate
from app.utils.prompt_loader import prompt_loader
from app.utils.llm_with_structured_output import openai_with_structured_output
from app.core.logger import Logger

logger = Logger.get_logger()


class BaseResearchTool(ABC):
    prompt_path: str
    response_model: Type[BaseModel]

    def create_chain(self):
        logger.debug("Creating chain in BaseTool")
        prompt = PromptTemplate.from_template(prompt_loader(self.prompt_path))
        model = openai_with_structured_output(self.response_model)
        chain = prompt | model
        return chain

    async def invoke(self, content: str) -> Type[BaseModel]:
        chain = self.create_chain()
        response = await chain.ainvoke({"research_content": content})
        return response
