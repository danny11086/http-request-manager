import flet as ft
import json
from .ui.request_form import RequestForm
from .ui.response_display import ResponseDisplay
from .api.request_handler import RequestHandler
from .api.response_handler import ResponseHandler
from .ui.styles import Styles
from .config import APP_NAME

class HttpRequestManager:
    def __init__(self, page: ft.Page):
        self.page = page
        self.setup_page()
        self.setup_controls()
        self.setup_handlers()

    def setup_page(self):
        """设置页面基本属性"""
        self.page.title = APP_NAME
        self.page.padding = 20
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.window_width = 1200
        self.page.window_height = 800

    def setup_controls(self):
        """设置UI控件"""
        # 标题
        self.title = ft.Text(APP_NAME, **Styles.TITLE)

        # 请求表单
        self.request_form = RequestForm()
        
        # 响应显示
        self.response_display = ResponseDisplay()
        
        # 发送按钮
        self.send_button = ft.ElevatedButton(
            text="Send Request",
            on_click=self.handle_send_request,
            **Styles.PRIMARY_BUTTON
        )

        # 左侧面板：请求表单
        left_panel = ft.Container(
            content=ft.Column([
                self.request_form,
                ft.Row([self.send_button], alignment=ft.MainAxisAlignment.END),
            ]),
            width=500,
        )

        # 右侧面板：响应显示
        right_panel = ft.Container(
            content=self.response_display,
            expand=True,
        )

        # 添加到页面
        self.page.add(
            self.title,
            ft.Divider(),
            ft.Row([
                left_panel,
                ft.VerticalDivider(),
                right_panel
            ], expand=True)
        )

    def setup_handlers(self):
        """设置处理器"""
        self.request_handler = RequestHandler()
        self.response_display.save_button.on_click = self.handle_save_response

    async def handle_send_request(self, e):
        """处理发送请求"""
        try:
            request_data = self.request_form.get_request_data()
            
            # 解析JSON参数
            params = json.loads(request_data["params"]) if request_data["params"] else {}
            headers = json.loads(request_data["headers"]) if request_data["headers"] else {}
            
            # 发送请求
            response_data = await self.request_handler.send_request(
                url=request_data["url"],
                method=request_data["method"],
                params=params,
                headers=headers,
                data=params if request_data["method"] in ["POST", "PUT", "PATCH"] else None
            )
            
            # 更新响应显示
            self.response_display.update_response(response_data)
            
            # 保存当前请求和响应数据
            self.current_request = request_data
            self.current_response = response_data

        except json.JSONDecodeError:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text("Invalid JSON format in parameters or headers"))
            )
        except Exception as e:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"Error: {str(e)}"))
            )

    def handle_save_response(self, e):
        """处理保存响应"""
        try:
            if hasattr(self, 'current_request') and hasattr(self, 'current_response'):
                filename = ResponseHandler.save_as_har(
                    self.current_request,
                    self.current_response
                )
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text(f"Response saved to {filename}"))
                )
            else:
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("No response to save"))
                )
        except Exception as e:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"Error saving response: {str(e)}"))
            )

def main(page: ft.Page):
    HttpRequestManager(page)

if __name__ == '__main__':
    ft.app(target=main) 