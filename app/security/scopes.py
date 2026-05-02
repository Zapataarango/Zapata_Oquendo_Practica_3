SCOPES_BY_ROLE = {
    "admin": {
        "tickets:crear",
        "tickets:ver_propios",
        "tickets:recibir",
        "tickets:asignar",
        "tickets:atender",
        "tickets:finalizar",
        "tickets:ver_todos",     
        
        "usuarios:create",
        "usuarios:read",
        "usuarios:update",
    
        "laboratorios:read",
        "laboratorios:create",
        
        "servicios:read",
        "servicios:create"

    },
    "solicitante": {
        "tickets:crear",
        "tickets:ver_propios"
    },
    "responsable_tecnico": {
        "tickets:ver_propios",
        "tickets:recibir",
        "tickets:asignar",
        "tickets:finalizar"
    },
    "auxiliar": {
        "tickets:ver_propios",
        "tickets:atender"
    },
    "tecnico_especializado": {
        "tickets:ver_propios",
        "tickets:atender"
    }
}

def get_scopes_for_role(role: str) -> set[str]:
    return SCOPES_BY_ROLE.get(role, set())