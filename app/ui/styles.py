import flet as ft
from ..config import THEME

class Styles:
    # Text styles
    TITLE = {
        "size": 30,
        "weight": ft.FontWeight.BOLD,
        "color": THEME["PRIMARY_COLOR"]
    }
    
    SUBTITLE = {
        "size": 20,
        "weight": ft.FontWeight.BOLD,
        "color": THEME["SECONDARY_COLOR"]
    }

    # Input field styles
    INPUT_FIELD = {
        "width": 400,
        "border_color": THEME["PRIMARY_COLOR"],
        "focused_border_color": THEME["SECONDARY_COLOR"],
        "border_radius": 8
    }

    # Button styles
    PRIMARY_BUTTON = {
        "bgcolor": THEME["PRIMARY_COLOR"],
        "color": THEME["BACKGROUND_COLOR"],
        "height": 40,
        "width": 120
    }

    SECONDARY_BUTTON = {
        "bgcolor": THEME["SECONDARY_COLOR"],
        "color": THEME["BACKGROUND_COLOR"],
        "height": 40,
        "width": 120
    }

    # Container styles
    CARD = {
        "padding": 20,
        "bgcolor": THEME["BACKGROUND_COLOR"],
        "border_radius": 10,
        "border": ft.border.all(2, THEME["PRIMARY_COLOR"])
    } 