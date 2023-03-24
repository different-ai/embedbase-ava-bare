import os
from embedbase import get_app

from embedbase.settings import get_settings
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from embedbase.supabase_db import Supabase
import logging


settings = get_settings()

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
