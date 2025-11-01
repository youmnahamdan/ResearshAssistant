from fastapi import APIRouter, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from app.api.v1.schemas.schemas import ResearchAnalysisResult
from app.services.research_service import analyze_research
from app.utils.input_parser import FileParser
from app.core.logger import Logger

logger = Logger.get_logger()


router = APIRouter(prefix="/analyze-research", tags=["Research Analysis"])


@router.post(
    "/",
    # response_model=ResearchAnalysisResult,
    summary="Parse input file and prompt AI assistant for response.",
    description=(
        "Upload a research document (PDF, DOCX, TXT). "
        "The agent analyzes it and returns a one string incorporating "
        "containing a summary, insights, and follow-up questions."
    ),
)
async def analyze_research_endpoint(
    file: UploadFile = File(..., description="Your research file (PDF, DOCX, or TXT)")
):
    try:
        logger.debug(f"Parsing File: {file}")
        text = FileParser().parse_file(file)
        if text == "UNSUPPORTED FILE":
            raise HTTPException(
                status_code=400,
                detail="Unsupported file type. Supported: PDF, DOCX, TXT",
            )

        logger.debug(type(text))
        logger.debug(text)

        response = await analyze_research(text)
        logger.debug(f"Analysis result: {response}")
        return response

    except HTTPException as he:
        logger.error(f"HTTPException in api.analyze_research: {he}")
        raise he
    except Exception as e:
        logger.error(f"Exception in api.analyze_research: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {e}")
