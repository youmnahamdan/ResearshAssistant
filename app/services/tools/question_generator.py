from app.core.config import questions_prompt_path
from app.api.v1.schemas.schemas import Questions
from app.services.tools.base_tool import BaseResearchTool


class QuestionGenerator(BaseResearchTool):
    prompt_path = questions_prompt_path
    response_model = Questions
