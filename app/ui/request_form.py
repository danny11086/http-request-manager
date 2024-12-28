import flet as ft
from .styles import Styles

class RequestForm(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.setup_controls()

    def setup_controls(self): 
        INPUT_STYLE= {
             **Styles.INPUT_FIELD,
              "width":120,
        }
        # 请求方法选择
        self.request_method = ft.Dropdown(
            label="Method",
            options=[
                ft.dropdown.Option("GET"),
                ft.dropdown.Option("POST"),
                ft.dropdown.Option("PUT"),
                ft.dropdown.Option("DELETE"),
                ft.dropdown.Option("OPTIONS"),
            ],
            value="GET",
           ** INPUT_STYLE,
        )
        REQUEST_NAME_STYLE= {
             **Styles.INPUT_FIELD,
              "width":300,
        }
        self.request_name = ft.TextField(
            label="Request Name",
            **REQUEST_NAME_STYLE
        )
        
        self.request_url = ft.TextField(
            label="Request URL",
            **Styles.INPUT_FIELD
        )
        
        self.request_params = ft.TextField(
            label="Request Parameters (JSON)",
            multiline=True,
            min_lines=3,
            max_lines=5,
            **Styles.INPUT_FIELD
        )
        
        self.request_headers = ft.TextField(
            label="Request Headers (JSON)",
            multiline=True,
            min_lines=2,
            max_lines=4,
            **Styles.INPUT_FIELD
        )

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    self.request_method,
                    self.request_name,
                ]),
                self.request_url,
                self.request_params,
                self.request_headers
            ]),
            **Styles.CARD
        )

    def get_request_data(self):
        return {
            "method": self.request_method.value,
            "name": self.request_name.value,
            "url": self.request_url.value,
            "params": self.request_params.value,
            "headers": self.request_headers.value
        } 