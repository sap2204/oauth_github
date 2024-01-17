from fastapi import Request, HTTPException, status


# Получение токена из кукиз
def get_token(request:Request):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return token

