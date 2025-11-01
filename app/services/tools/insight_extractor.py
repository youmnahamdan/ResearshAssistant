from app.core.config import insights_prompt_path
from app.api.v1.schemas.schemas import Insights
from app.services.tools.base_tool import BaseResearchTool


class InsightsExtractor(BaseResearchTool):
    prompt_path = insights_prompt_path
    response_model = Insights
