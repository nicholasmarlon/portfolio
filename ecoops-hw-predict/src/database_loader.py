import sqlite3
import os
from datetime import datetime

def init_db(db_path="ecoops.db"):
    """Inicializa o banco de dados relacional e cria as tabelas."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Criação das tabelas
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS devices (
            device_id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostname TEXT UNIQUE NOT NULL,
            os_version TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS battery_telemetry (
            telemetry_id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id INTEGER,
            design_capacity INTEGER NOT NULL,
            full_charge_capacity INTEGER NOT NULL,
            cycle_count INTEGER,
            health_percentage REAL,
            rul_estimated_cycles INTEGER,
            captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (device_id) REFERENCES devices(device_id)
        )
    """)
    
    conn.commit()
    conn.close()
    print("[DBA] Banco de dados inicializado com sucesso!")

def save_telemetry_to_db(hostname, design_cap, full_cap, cycles, health, rul, db_path="ecoops.db"):
    """Insere os dados de telemetria aplicando conceitos de integridade referencial."""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Garante que o dispositivo existe na tabela de dimensão
    cursor.execute("INSERT OR IGNORE INTO devices (hostname) VALUES (?)", (hostname,))
    cursor.execute("SELECT device_id FROM devices WHERE hostname = ?", (hostname,))
    device_id = cursor.fetchone()[0]
    
    # Insere os dados de telemetria e fatos
    cursor.execute("""
        INSERT INTO battery_telemetry 
        (device_id, design_capacity, full_charge_capacity, cycle_count, health_percentage, rul_estimated_cycles)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (device_id, design_cap, full_cap, cycles, health, rul))
    
    conn.commit()
    conn.close()
    print(f"[DBA] Telemetria salva no banco para o host: {hostname}")

if __name__ == "__main__":
    init_db()
    # Teste de carga simulada
    save_telemetry_to_db("LAPTOP-NICHOLAS", 45000, 38000, 350, 84.4, 420)
