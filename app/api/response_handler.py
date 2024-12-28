import json
import os
from datetime import datetime
from typing import Dict
from app.config import HAR_SAVE_DIR, APP_NAME, APP_VERSION

class ResponseHandler:
    @staticmethod
    def format_response(response_data: Dict) -> str:
        """Format response data for display"""
        if not response_data["success"]:
            return f"Error: {response_data['error']}"

        if isinstance(response_data["content"], dict):
            return json.dumps(response_data["content"], indent=2)
        return str(response_data["content"])

    @staticmethod
    def save_as_har(request_data: Dict, response_data: Dict) -> str:
        """Save request and response data as HAR file"""
        if not os.path.exists(HAR_SAVE_DIR):
            os.makedirs(HAR_SAVE_DIR)

        """ har_data = {
            "log": {
                "version": "1.2",
                "creator": {
                    "name": APP_NAME,
                    "version": APP_VERSION
                },
                "entries": [{
                    "startedDateTime": datetime.now().isoformat(),
                    "request": {
                        "method": request_data.get("method", "GET"),
                        "url": request_data["url"],
                        "headers": request_data.get("headers", {}),
                        "queryString": request_data.get("params", {})
                    },
                    "response": {
                        "status": response_data.get("status_code"),
                        "headers": response_data.get("headers", {}),
                        "content": {
                            "text": ResponseHandler.format_response(response_data)
                        }
                    },
                    "time": response_data.get("response_time", 0) * 1000
                }]
            }
        } """
        postman_har={
            "name":request_data.get("name", "未命名"),
            "request": {
                "method": request_data.get("method", "GET"),
                "header": [],
                "body": {
                    "mode": "raw",
                    "raw": request_data.get("params", {}) ,
                    "options": {
                        "raw": {
                            "language": "json"
                        }
                    }
                },
                "url": {
                    "raw":  request_data.get("url", "")
                }
            },
            "response": [
                {
                    "name": "successfully / 200",
                    "status": "OK",
                    "code": response_data.get("status_code"),
                    "_postman_previewlanguage": "json",
                    "header": [
                        {
                            "key": "content-type",
                            "value": "application/json;charset=UTF-8"
                        }
                    ],
                    "cookie": [],
                    "body":  ResponseHandler.format_response(response_data)
                }
            ]
        }

        filename = f"{HAR_SAVE_DIR}/response_{datetime.now().strftime('%Y%m%d_%H%M%S')}.har"
        with open(filename, 'w',encoding='utf-8') as f:
            json.dump(postman_har, f, indent=2,ensure_ascii=False)
        
        return filename 