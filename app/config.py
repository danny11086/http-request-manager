"""
Configuration settings for the HTTP Request Manager
"""

# Application settings
APP_NAME = "HTTP Request Manager"
APP_VERSION = "1.0.0"

# UI Theme settings
THEME = {
    "PRIMARY_COLOR": "#2196F3",  # Blue
    "SECONDARY_COLOR": "#4CAF50",  # Green
    "ERROR_COLOR": "#F44336",  # Red
    "BACKGROUND_COLOR": "#FFFFFF",  # White
    "TEXT_COLOR": "#000000",  # Black
}

# Request settings
DEFAULT_HEADERS = {
    "User-Agent": f"{APP_NAME}/{APP_VERSION}",
    "Accept": "application/json",
}

# File settings
HAR_SAVE_DIR = "saved_responses" 