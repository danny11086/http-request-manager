import requests
from datetime import datetime
from typing import Dict, Any, Optional
from app.config import DEFAULT_HEADERS

class RequestHandler:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)

    async def send_request(
        self,
        url: str,
        method: str = "GET",
        params: Optional[Dict] = None,
        headers: Optional[Dict] = None,
        data: Any = None
    ) -> Dict:
        """
        Send HTTP request and return response details
        """
        start_time = datetime.now()
        
        try:
            headers = headers or {}
            self.session.headers.update(headers)
            
            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data if method in ["POST", "PUT", "PATCH"] else None
            )
            
            end_time = datetime.now()
            response_time = (end_time - start_time).total_seconds()

            return {
                "status_code": response.status_code,
                "response_time": response_time,
                "headers": dict(response.headers),
                "content": response.json() if response.headers.get('content-type', '').startswith('application/json') else response.text,
                "success": True
            }

        except Exception as e:
            return {
                "success": False,
                "error": str(e)
            } 