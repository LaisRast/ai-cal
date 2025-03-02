from dotenv import load_dotenv
from fastapi import HTTPException, Request

from app.config import PROMPT_MIN_LENGTH, PROMPT_MAX_LENGTH
from app.models.prase_request import ParseRequest
from app.models.prase_respones import ParseResponse
from app.services.llm_service import parse_using_ai
from app.setup.cors import setup_cors
from app.setup.rate_limiter import setup_rate_limiter, limiter

from fastapi import FastAPI


# app
app = FastAPI()

# rate limiter
setup_rate_limiter(app)

# setup cors
setup_cors(app)

# load env
load_dotenv()


@app.post("/parse")
@limiter.limit("5/minute")
async def parse(request: Request, parse_request: ParseRequest) -> ParseResponse:
    if len(parse_request.prompt) < PROMPT_MIN_LENGTH:
        raise HTTPException(
            status_code=400, detail=f"prompt must be at least{PROMPT_MIN_LENGTH}"
        )
    if len(parse_request.prompt) > PROMPT_MAX_LENGTH:
        raise HTTPException(
            status_code=400, detail=f"prompt must be at most {PROMPT_MAX_LENGTH}"
        )
    return parse_using_ai(parse_request=parse_request)
