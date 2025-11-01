import asyncio
from app.services.tools.summarizer import Summarizer
from app.services.tools.question_generator import QuestionGenerator
from app.services.tools.insight_extractor import InsightsExtractor
from app.api.v1.schemas.schemas import ResearchAnalysisResult
from app.core.logger import Logger

logger = Logger.get_logger()


async def analyze_research(research_content: str) -> ResearchAnalysisResult:
    logger.debug(f"Orchestrating LLM calls inside analyze_research")
    summary_task = Summarizer().invoke(research_content)
    insights_task = InsightsExtractor().invoke(research_content)
    question_task = QuestionGenerator().invoke(research_content)

    # await the tools
    summary, insights, questions = await asyncio.gather(
        summary_task, insights_task, question_task
    )

    return ResearchAnalysisResult(
        summary=summary, insights=insights, questions=questions
    )
