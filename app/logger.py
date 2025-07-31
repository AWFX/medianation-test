import logging

def setup_loggers():
    uvicorn_handler = logging.FileHandler("logs/app.log")
    uvicorn_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))

    for name in ("uvicorn.access", "uvicorn.error"):
        uv_logger = logging.getLogger(name)
        uv_logger.setLevel(logging.INFO)
        uv_logger.handlers = [uvicorn_handler]
        uv_logger.propagate = False
