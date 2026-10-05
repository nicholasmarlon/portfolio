import logging
import os
from datetime import datetime

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "security_audit.log")

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [SECURITY_AUDIT] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_event(event_type, user, status, description):
    """Registra um evento de auditoria de segurança e governança no sistema."""
    log_message = f"EVENT: {event_type} | USER: {user} | STATUS: {status} | DESC: {description}"
    if status == "SUCCESS":
        logging.info(log_message)
    elif status == "WARNING":
        logging.warning(log_message)
    elif status == "ERROR":
        logging.error(log_message)
    print(f"[AUDIT LOG] {status}: {event_type} registrado com sucesso.")

if __name__ == "__main__":
    log_event("DB_LOAD", "system_etl_bot", "SUCCESS", "Telemetria carregada com integridade verificada.")
    log_event("UNAUTHORIZED_ACCESS_ATTEMPT", "unknown_ip", "WARNING", "Tentativa de acesso restrito bloqueada.")
