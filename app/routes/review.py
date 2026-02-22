from fastapi import APIRouter, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
from app.services.diff_parser import parse_diff
from app.services.llm_parser import review_code
from pydantic import BaseModel

limiter = Limiter(key_func=get_remote_address)
router = APIRouter()

class ReviewRequest(BaseModel):
  raw_git_diff: str

@router.post("/review")
@limiter.limit("10/minute")
async def review(request: Request, body: ReviewRequest):
  parsed_files = parse_diff(body.raw_git_diff)
  result = []
  for file_data in parsed_files:
    review_result = review_code(file_data)
    result.append({
      "filename": file_data["filename"],
      "review":review_result
    })
  return {"results": result}