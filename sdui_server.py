# sdui_server.py
from fastapi import FastAPI, Query
from typing import List, Dict, Any

app = FastAPI()

def get_ui_schema(user_role: str) -> Dict[str, Any]:
    if user_role == "admin":
        return {
            "type": "screen",
            "components": [
                {"type": "header", "text": "Admin Dashboard"},
                {"type": "stats", "metrics": ["users", "revenue", "uptime"]},
                {"type": "button", "text": "Manage Users", "action": "navigate", "target": "/users"}
            ]
        }
    elif user_role == "guest":
        return {
            "type": "screen",
            "components": [
                {"type": "header", "text": "Welcome Guest"},
                {"type": "carousel", "items": ["promo1.jpg", "promo2.jpg"]},
                {"type": "button", "text": "Sign Up", "action": "navigate", "target": "/signup"}
            ]
        }
    else:
        return {
            "type": "screen",
            "components": [
                {"type": "header", "text": "User Home"},
                {"type": "feed", "items": ["post1", "post2"]},
                {"type": "button", "text": "Profile", "action": "navigate", "target": "/profile"}
            ]
        }

@app.get("/ui-schema")
def get_ui(user_role: str = Query("user")):
    return get_ui_schema(user_role)
