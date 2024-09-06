# This is the logger.py file. It sets up our special way of keeping track of what's happening.

import logging
import os
from datetime import datetime

# Create a special folder for our notebooks (logs) if it doesn't exist
log_directory = "logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Set up our special notebook (logging configuration)
def setup_logger():
    # Create a new notebook (log file) with today's date and time in the name
    log_filename = os.path.join(log_directory, f"songwriter_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    
    # Set up how we want to write in our notebook
    logging.basicConfig(
        filename=log_filename,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )