import flet as ft
from ..config import THEME
from .styles import Styles
import json
class ResponseDisplay(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.setup_controls()

    def setup_controls(self):
        # 状态和响应时间显示
        self.status_text = ft.Text(
            size=16,
            color=THEME["PRIMARY_COLOR"]
        )
        
        self.time_text = ft.Text(
            size=16,
            color=THEME["SECONDARY_COLOR"]
        )

        # 响应内容显示
        self.response_content = ft.TextField(
            label="Response",
            multiline=True,
            min_lines=10,
            max_lines=20,
            read_only=True,
            **Styles.INPUT_FIELD
        )

        # 保存按钮
        self.save_button = ft.ElevatedButton(
            text="Save as HAR",
            **Styles.SECONDARY_BUTTON
        )

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Row([
                    self.status_text,
                    self.time_text
                ]),
                self.response_content,
                ft.Row([
                    self.save_button
                ], alignment=ft.MainAxisAlignment.END)
            ]),
            **Styles.CARD
        )

    def update_response(self, response_data: dict):
        """更新响应显示"""
        if response_data["success"]:
            self.status_text.value = f"Status: {response_data['status_code']}"
            self.time_text.value = f"Response Time: {response_data['response_time']:.2f}s"
            self.response_content.value = json.dumps(response_data["content"],ensure_ascii=False,indent=4)
        else:
            self.status_text.value = "Error"
            self.response_content.value = str(response_data["error"])
        
        self.update() 