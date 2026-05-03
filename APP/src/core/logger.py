
import logging
from pathlib import Path
LOG_DIR = Path.home() / '.myenterprisexmlapp' / 'logs'
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / 'app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

def get_logger(name):
    return logging.getLogger(name)
