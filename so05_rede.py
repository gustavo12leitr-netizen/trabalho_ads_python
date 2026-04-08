import psutil
import time
import os

print("Monitorando rede... (Aguarde 1 segundo para a primeira leitura)")

def pegar_dados():
    io = psutil.net_io_counters()
    return io.bytes_recv, io.bytes_sent

try:
    while True:
        # Pega a primeira leitura
        rec1, env1 = pegar_dados()
        time.sleep(1)
        # Pega a segunda leitura após 1 segundo
        rec2, env2 = pegar_dados()
        
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Calcula a diferença para saber a velocidade por segundo
        download = (rec2 - rec1) / 1024
        upload = (env2 - env1) / 1024
        
        print("=== TRÁFEGO DE REDE EM TEMPO REAL ===")
        print(f"Download: {download:.2f} kB/s")
        print(f"Upload: {upload:.2f} kB/s")
        print("\n(Ctrl+C para parar)")
except KeyboardInterrupt:
    print("\nMonitoramento de rede encerrado.")
