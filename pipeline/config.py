import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
REQUIRED_KEYS = ["GEMINI_API_KEY", "GROQ_API_KEY", "PEXELS_API_KEY"]


def load():
    with open(ROOT / "config.yaml", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    load_dotenv(ROOT / ".env")
    missing = [k for k in REQUIRED_KEYS if not os.getenv(k)]
    return config, missing
