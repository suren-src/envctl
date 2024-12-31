import logging
from datetime import datetime
from pathlib import Path

# Module-level private variable for logger
_logger = None

def _get_logger():
    global _logger
    if _logger is None:
        _logger = _setup_logging()
    return _logger

def _setup_logging(logger_name: str = 'envctl', dirname: str = '.envctl', log_level = logging.DEBUG):
    log_dir = Path.home() / dirname / 'logs'
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = log_dir / f'{timestamp}.log'

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    console_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_format)

    # File Handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(log_level)
    file_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_format)

    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info(f'Logging initialized. Log file: {log_file}')
    return logger

# single logger instance
logger = _get_logger()