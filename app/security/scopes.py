SCOPES_BY_ROLE = {
    "admin": {

        "tickets:create",     
        "tickets:read",       
        "tickets:update",     
        "tickets:delete",     
        
        "usuarios:create",
        "usuarios:read",
        "usuarios:update",
    
        "laboratorios:read",
        "laboratorios:create",
        
        "servicios:read",
        "servicios:create"
    },
    "solicitante": {
        "tickets:create",   
        "tickets:read",      
    },
    "responsable_tecnico": {
        "tickets:read",       
        "tickets:update",     
    },
    "auxiliar": {
        "tickets:read",        
        "tickets:update",      
    },
    "tecnico_especializado": {
        "tickets:read",        
        "tickets:update",      
    },
}

def get_scopes_for_role(role: str) -> set[str]:
    """
    Retorna el conjunto de permisos (scopes) asociados a un rol específico.
    Si el rol no existe, retorna un conjunto vacío.
    """
    return SCOPES_BY_ROLE.get(role, set())