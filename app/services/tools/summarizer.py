from app.core.config import summarize_prompt_path
from app.api.v1.schemas.schemas import Summary
from app.services.tools.base_tool import BaseResearchTool


class Summarizer(BaseResearchTool):
    prompt_path = summarize_prompt_path
    response_model = Summary
