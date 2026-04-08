import psutil
import time
import os

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        total = psutil.cpu_percent(interval=1)
        nucleos = psutil.cpu_percent(percpu=True)
        
        print(f"Uso Total da CPU: {total}%")
        print("-" * 30)
        for i, uso in enumerate(nucleos):
            print(f"Núcleo {i}: {uso}%")
        
        print("\n(Ctrl+C para parar)")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nFim do monitoramento.")
