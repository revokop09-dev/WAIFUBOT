import logging
import os

# 1. This configures how your logs look in the terminal
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# 2. This creates the TRUE logging object that your modules are trying to import
LOGGER = logging.getLogger("YUKIWAFUS")

# 3. We renamed the helper function so it doesn't overwrite the LOGGER variable!
def get_custom_logger(name: str):
    return logging.getLogger(name)
