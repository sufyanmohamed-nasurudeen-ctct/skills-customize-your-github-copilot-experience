import os
import time
from typing import Any

from fastapi import FastAPI

PROJECT_NAME = "TODO: set your app name"
PROJECT_VERSION = "TODO: set your app version"
START_TIME = time.time()

app = FastAPI(title="FastAPI Local Deployment Checklist")


def get_runtime_config() -> dict[str, Any]:
    """Return host/port/env values used to run the API."""
    # TODO: Read APP_HOST, APP_PORT, and APP_ENV from environment variables.
    # Use defaults: host=127.0.0.1, port=8000, env=dev.
    # Convert port to int and raise ValueError("APP_PORT must be an integer") if invalid.
    raise NotImplementedError


def build_health_payload(config: dict[str, Any]) -> dict[str, Any]:
    """Return a standard health payload for monitoring checks."""
    # TODO: Return a dictionary with keys:
    # status, app, environment, uptime_seconds
    # status must be "ok"
    # app should use PROJECT_NAME
    # environment should come from config["env"]
    # uptime_seconds should be a non-negative integer
    raise NotImplementedError


def build_start_command(config: dict[str, Any]) -> str:
    """Build a reproducible command to run this API locally."""
    return f"uvicorn starter-code:app --host {config['host']} --port {config['port']}"


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "FastAPI deployment checklist starter app"}


@app.get("/health")
def health() -> dict[str, Any]:
    config = get_runtime_config()
    return build_health_payload(config)


def run_checks() -> None:
    """Simple auto-gradable checks for assignment requirements."""
    print("Running checks...")

    original_values = {
        "APP_HOST": os.environ.get("APP_HOST"),
        "APP_PORT": os.environ.get("APP_PORT"),
        "APP_ENV": os.environ.get("APP_ENV"),
    }

    try:
        os.environ["APP_HOST"] = "0.0.0.0"
        os.environ["APP_PORT"] = "9001"
        os.environ["APP_ENV"] = "staging"

        config = get_runtime_config()
        assert config["host"] == "0.0.0.0", "APP_HOST was not read correctly"
        assert config["port"] == 9001, "APP_PORT was not converted to int"
        assert config["env"] == "staging", "APP_ENV was not read correctly"

        command = build_start_command(config)
        assert "--host 0.0.0.0" in command, "Start command is missing host"
        assert "--port 9001" in command, "Start command is missing port"

        payload = build_health_payload(config)
        expected_keys = {"status", "app", "environment", "uptime_seconds"}
        assert expected_keys.issubset(payload.keys()), "Health payload keys are incorrect"
        assert payload["status"] == "ok", "status must be 'ok'"
        assert payload["environment"] == "staging", "environment must match config"
        assert isinstance(payload["uptime_seconds"], int), "uptime_seconds must be int"
        assert payload["uptime_seconds"] >= 0, "uptime_seconds must be non-negative"

        print("PASS: All checks passed")
    finally:
        for key, value in original_values.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def main() -> None:
    if "--check" in os.sys.argv:
        run_checks()
    else:
        config = get_runtime_config()
        print("Suggested launch command:")
        print(build_start_command(config))


if __name__ == "__main__":
    main()
