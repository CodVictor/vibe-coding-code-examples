# permissions.py - Lógica aislada y extensible
from enum import Enum
from dataclasses import dataclass

class Role(Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    VIEWER = "viewer"

class Action(Enum):
    CREATE = "create"
    EDIT = "edit"
    DELETE = "delete"
    VIEW = "view"

# Definición de políticas clara y centralizada
ROLE_PERMISSIONS = {
    Role.ADMIN: {Action.CREATE, Action.EDIT, Action.DELETE, Action.VIEW},
    Role.EDITOR: {Action.EDIT, Action.VIEW},
    Role.VIEWER: {Action.VIEW},
}

class PermissionManager:
    @staticmethod
    def has_permission(role: Role, action: Action) -> bool:
        return action in ROLE_PERMISSIONS.get(role, set())

# main.py - Implementación limpia (ejemplo de uso en un endpoint)
@app.get("/post/{post_id}/edit")
async def edit_post(post_id: int, role: Role):
    if not PermissionManager.has_permission(role, Action.EDIT):
        raise HTTPException(status_code=403, detail="Acceso Denegado")
    return {"status": "Acción permitida"}