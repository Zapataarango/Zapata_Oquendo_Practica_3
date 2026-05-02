from .usuario import crear_usuario, obtener_usuario_por_correo, obtener_usuario_por_id, listar_usuarios, eliminar_usuario
from .laboratorio import crear_laboratorio, obtener_laboratorios, obtener_laboratorio_por_id, eliminar_laboratorio
from .servicio import crear_servicio, obtener_servicios, eliminar_servicio, obtener_servicio_por_id
from .ticket import crear_ticket, obtener_tickets, obtener_ticket_por_id, cambiar_estado_ticket, eliminar_ticket, asignar_ticket_tecnico, obtener_todos_los_tickets