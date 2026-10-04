import os
from bs4 import BeautifulSoup

def parse_battery_report(filepath):
    if not os.path.exists(filepath):
        print(f"[ERRO] Arquivo não encontrado em: {filepath}")
        print("Certifique-se de gerar o relatório com 'powercfg /batteryreport' e salvá-lo em data/raw/battery-report.html")
        return None

    print(f"[INFO] Lendo o relatório de bateria de: {filepath}")
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Exemplo de extração básica de tabelas do relatório do Windows
    tables = soup.find_all('table')
    print(f"[SUCESSO] Relatório carregado com sucesso! Total de tabelas encontradas: {len(tables)}")
    return soup

if __name__ == '__main__':
    report_path = os.path.join('data', 'raw', 'battery-report.html')
    parse_battery_report(report_path)
