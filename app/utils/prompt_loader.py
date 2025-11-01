import os
from app.core.logger import Logger

logger = Logger.get_logger()


def prompt_loader(prompt_file):
    logger.debug(f"Loading prompt from: {prompt_file}")
    file_dir = prompt_file
    if os.path.exists(file_dir):
        with open(file_dir, "r") as file:
            return file.read()
