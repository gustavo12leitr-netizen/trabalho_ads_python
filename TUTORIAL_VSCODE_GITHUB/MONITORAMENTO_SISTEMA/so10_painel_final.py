import psutil
import time
import os

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Dados de RAM
        ram = psutil.virtual_memory()
        # Dados de CPU
        cpu = psutil.cpu_percent()
        # Dados de Disco (Partição C: ou /)
        disco = psutil.disk_usage('/')
        
        print("==========================================")
        print("   PAINEL INTEGRADO DE MONITORAMENTO     ")
        print("==========================================")
        print(f"CPU: {cpu}%")
        print(f"RAM: {ram.percent}% ({ram.used/(1024**2):.0f}MB / {ram.total/(1024**2):.0f}MB)")
        print(f"DISCO: {disco.percent}% livre ({disco.free/(1024**3):.1f}GB)")
        print("------------------------------------------")
        print("Pressione Ctrl+C para encerrar o painel.")
        
        time.sleep(2)
except KeyboardInterrupt:
    print("\nPainel encerrado com sucesso.")
