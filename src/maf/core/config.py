from __future__ import annotations
from pydantic import BaseModel
import os

class Config(BaseModel):
    base_url: str = os.getenv("MAF_BASE_URL", "https://www.saucedemo.com")
    api_base: str = os.getenv("MAF_API_BASE", "https://httpbin.org")
    headless: bool = os.getenv("MAF_HEADLESS", "true").lower() != "false"

CFG = Config()
