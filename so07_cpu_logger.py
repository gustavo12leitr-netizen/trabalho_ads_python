import psutil
import time
from datetime import datetime

print("Registrando uso da CPU em 'cpu_log.txt'... (Ctrl+C para parar)")

try:
    while True:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        uso = psutil.cpu_percent(interval=1)
        
        with open("cpu_log.txt", "a") as arquivo:
            arquivo.write(f"{agora} - CPU: {uso}%\n")
            
        time.sleep(5) # Registra a cada 5 segundos
except KeyboardInterrupt:
    print("\nLog finalizado.")
