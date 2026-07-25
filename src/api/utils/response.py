from typing import Any


def success(data: Any = None, message: str = "Success") -> dict:
    return {"success": True, "message": message, "data": data}


def error(message: str = "An error occurred", code: int = 400) -> dict:
    return {"success": False, "message": message, "code": code}
