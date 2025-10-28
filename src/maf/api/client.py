from __future__ import annotations
import os
import requests

class ApiClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url.rstrip("/")

    def health(self) -> int:
        # allow overriding the path via env var
        path = os.getenv("MAF_HEALTH_PATH", "/status/200")
        url = f"{self.base_url}{path}"
        r = requests.get(url, timeout=10)
        return r.status_code
