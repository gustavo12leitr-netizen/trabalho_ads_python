import psutil

# COMENTÁRIO DIDÁTICO:
# Dispositivos de E/S (Entrada e Saída) incluem Teclado, Mouse (Entrada),
# Monitor, Impressora (Saída). Via psutil, focamos em armazenamento (E/S de dados).

print("=== DISPOSITIVOS DE ARMAZENAMENTO DETECTADOS ===")
particoes = psutil.disk_partitions()

for p in particoes:
    print(f"\nDispositivo: {p.device}")
    print(f"Ponto de Montagem: {p.mountpoint}")
    print(f"Tipo de Arquivo: {p.fstype}")
    
    try:
        uso = psutil.disk_usage(p.mountpoint)
        print(f"Espaço Total: {uso.total / (1024**3):.2f} GB")
    except:
        print("Status: Dispositivo não pronto.")
