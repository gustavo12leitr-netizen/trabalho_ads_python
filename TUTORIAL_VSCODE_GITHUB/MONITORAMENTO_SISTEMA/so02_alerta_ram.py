import psutil
import time

# Requisito: Ler o limite do usuário
limite = float(input("Defina o limite crítico de uso de RAM (em %): "))

print(f"\nMonitorando... O alerta soará acima de {limite}%")
print("Pressione Ctrl+C para encerrar.\n")

try:
    while True:
        memoria = psutil.virtual_memory()
        uso_atual = memoria.percent
        
        status = "OK"
        if uso_atual > limite:
            status = "⚠️ PERIGO: LIMITE ULTRAPASSADO!"
            
        print(f"Uso de RAM: {uso_atual}% | Status: {status}")
        
        time.sleep(2)
except KeyboardInterrupt:
    print("\nMonitoramento interrompido pelo usuário.")
