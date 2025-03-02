from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

origins = ["https://ai-cal.xyz", "https://www.ai-cal.xyz"]


def setup_cors(app: FastAPI) -> None:
    app.add_middleware(
        CORSMiddleware,  # type: ignore
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
