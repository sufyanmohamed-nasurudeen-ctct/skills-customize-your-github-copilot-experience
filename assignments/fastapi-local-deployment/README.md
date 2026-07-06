# 📘 Assignment: FastAPI Local Deployment Checklist

## 🎯 Objective

In this assignment, you will prepare a FastAPI app so another developer can run it reliably on any machine. You will practice environment-based configuration, health checks, and repeatable launch commands.

## 📝 Tasks

### 🛠️ Add Runtime Configuration

#### Description
Update the starter code so host, port, and environment values come from environment variables with sensible defaults.

#### Requirements
Completed program should:

- Implement `get_runtime_config()` using `APP_HOST`, `APP_PORT`, and `APP_ENV`
- Use defaults `127.0.0.1`, `8000`, and `dev` when variables are not set
- Convert `APP_PORT` to an integer and raise a clear error for invalid values


### 🛠️ Build a Deployment Health Endpoint

#### Description
Implement a health payload and endpoint so deployment checks can confirm that the app is running correctly.

#### Requirements
Completed program should:

- Implement `build_health_payload(config)` to return `status`, `app`, `environment`, and `uptime_seconds`
- Return `"status": "ok"` when the app is healthy
- Expose a GET `/health` endpoint that returns the payload as JSON


### 🛠️ Verify with Auto-Gradable Checks

#### Description
Run the provided checks to verify your deployment setup works before sharing it with a teammate.

#### Requirements
Completed program should:

- Pass `python starter-code.py --check` with all tests reporting `PASS`
- Produce a launch command string with `build_start_command()` that includes the configured host and port
- Start the app locally with the generated command and confirm `/health` responds
