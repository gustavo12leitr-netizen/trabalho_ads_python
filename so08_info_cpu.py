import psutil
import platform

print("=== INFORMAÇÕES DO PROCESSADOR ===")
print(f"Processador: {platform.processor()}")
print(f"Núcleos Físicos: {psutil.cpu_count(logical=False)}")
print(f"Núcleos Lógicos: {psutil.cpu_count(logical=True)}")

freq = psutil.cpu_freq()
if freq:
    print(f"Frequência Atual: {freq.current:.2f} MHz")
    print(f"Frequência Máxima: {freq.max:.2f} MHz")

# Nota: O número de série costuma exigir permissão de Administrador/Root 
# e varia por SO, por isso muitos sistemas não permitem via código simples.
print("\nNúmero de Série: Não foi possível obter (Limitação de Permissão do SO)")
