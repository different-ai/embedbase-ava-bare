import os
from embedbase import get_app

from embedbase.settings import get_settings
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from middlewares.history.history import PRODUCTION_IGNORED_PATHS, DetailedError, History
from embedbase.supabase_db import Supabase
import semantic_version
import logging

settings = get_settings()
MINIMUM_VERSION = os.getenv("MINIMUM_VERSION", "2.19.0")

app = (
    get_app(settings)
    .use(Supabase(settings.supabase_url, settings.supabase_key))
    .use(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
)

app = app.run()
