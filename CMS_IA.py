# main.py
from fastapi import FastAPI, HTTPException, Depends

app = FastAPI()

def check_permissions(user_role: str, action: str):
    # La IA tiende a usar lógica anidada y "hardcoded"
    if user_role == "admin":
        return True
    elif user_role == "editor":
        if action in ["edit", "view"]:
            return True
        else:
            return False
    elif user_role == "viewer":
        if action == "view":
            return True
        else:
            return False
    return False

# ejemplo de uso en un endpoint
@app.get("/post/{post_id}/edit")
async def edit_post(post_id: int, role: str):
    if not check_permissions(role, "edit"):
        raise HTTPException(status_code=403, detail="No tienes permiso")
    return {"status": "Editando el post"}