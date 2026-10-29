# 💻 EcoOps: Multi-Disciplinary Hardware & Governance Analytics Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)
[![SQLite/SQL](https://img.shields.io/badge/Database-Relational-green.svg)](https://www.sqlite.org/)
[![Security Audit](https://img.shields.io/badge/Governance-Audit%20Logging-orange.svg)](https://github.com/)

**EcoOps** é uma plataforma avançada desenvolvida para monitoramento preditivo de ativos de hardware (focada em FinOps e ESG), unindo pilares essenciais de **Ciência de Dados**, **Administração de Bancos de Dados (DBA)** e **Cibersegurança/Governança**.

---

## 🏗️ Arquitetura do Projeto

1. **Camada de Dados & DBA (database/ & src/database_loader.py)**:
   - Modelagem relacional normalizada (devices e attery_telemetry).
   - Integridade referencial com chaves estrangeiras (FOREIGN KEY) e restrições de unicidade.
   - Índices otimizados (CREATE INDEX) para alta performance de consultas analíticas.
   
2. **Camada de Governança e Segurança (src/audit_logger.py)**:
   - Sistema estruturado de logs de auditoria (security_audit.log).
   - Rastreabilidade de eventos de sistema, tentativas de acesso e status de carregamento ETL.

3. **Camada de Análise Preditiva e BI (model.py & pp.py)**:
   - Algoritmo de estimativa de vida útil remanescente (RUL).
   - Dashboard interativo corporativo desenvolvido em Streamlit consumindo dados persistidos.

---

## 🚀 Como Executar o Projekte Localmente

### 1. Clonar o repositório
\\\ash
git clone https://github.com/nicholasmarlon/portfolio.git
cd portfolio/ecoops-hw-predict
\\\

### 2. Instalar as dependências
\\\ash
pip install -r requirements.txt
\\\

### 3. Executar o carregador de dados (ETL & DBA)
\\\ash
py src/database_loader.py
\\\

### 4. Iniciar o Dashboard Interativo
\\\ash
py -m streamlit run app.py
\\\

---

## 👤 Autor

Desenvolvido por **Nicholas Marlon Barbosa de Souza**  
- [LinkedIn](https://www.linkedin.com/in/nicholas-marlon-barbosa-de-souza-169b598b/)  
- [GitHub](https://github.com/nicholasmarlon)
