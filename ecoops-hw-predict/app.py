import streamlit as st
import sqlite3
import pandas as pd
import os

st.set_page_config(
    page_title="EcoOps - Hardware & FinOps Analytics",
    page_icon="💻",
    layout="wide"
)

st.title("💻 EcoOps: Gestão de Ativos, Telemetria e Governança")
st.markdown("---")

# Função para conectar e buscar dados do banco relacional
def load_data_from_db():
    db_path = "ecoops.db"
    if not os.path.exists(db_path):
        return pd.DataFrame()
    
    conn = sqlite3.connect(db_path)
    query = """
        SELECT d.hostname, t.design_capacity, t.full_charge_capacity, 
               t.cycle_count, t.health_percentage, t.rul_estimated_cycles, t.captured_at
        FROM battery_telemetry t
        JOIN devices d ON t.device_id = d.device_id
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df

df_telemetry = load_data_from_db()

if df_telemetry.empty:
    st.warning("Nenhum dado encontrado no banco de dados. Execute o script de carga (database_loader.py) primeiro.")
else:
    st.sidebar.header("Painel de Controle")
    selected_host = st.sidebar.selectbox("Selecione o Dispositivo", df_telemetry["hostname"].unique())
    
    # Filtrar dados do dispositivo selecionado
    device_data = df_telemetry[df_telemetry["hostname"] == selected_host].iloc[-1]
    
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("Capacidade de Projeto", f"{device_data['design_capacity']} mWh")
    col2.metric("Capacidade Atual", f"{device_data['full_charge_capacity']} mWh")
    col3.metric("Saúde da Bateria", f"{device_data['health_percentage']}%")
    col4.metric("Ciclos de Carga", int(device_data['cycle_count']))
    
    st.markdown("---")
    st.subheader("📊 Histórico de Telemetria Consolidado no Banco Relacional")
    st.dataframe(df_telemetry, use_container_width=True)
