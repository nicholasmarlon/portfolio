-- Criação do Schema para Gerenciamento de Ativos e Telemetria de Hardware (EcoOps)
-- Focado em performance (DBA) e rastreabilidade

CREATE TABLE IF NOT EXISTS devices (
    device_id SERIAL PRIMARY KEY,
    hostname VARCHAR(100) UNIQUE NOT NULL,
    os_version VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS battery_telemetry (
    telemetry_id SERIAL PRIMARY KEY,
    device_id INT REFERENCES devices(device_id) ON DELETE CASCADE,
    design_capacity INT NOT NULL,
    full_charge_capacity INT NOT NULL,
    cycle_count INT,
    health_percentage DECIMAL(5,2),
    rul_estimated_cycles INT,
    captured_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Índices otimizados para DBA (acelerar buscas por dispositivo e histórico de saúde)
CREATE INDEX idx_telemetry_device ON battery_telemetry(device_id);
CREATE INDEX idx_telemetry_date ON battery_telemetry(captured_at);
