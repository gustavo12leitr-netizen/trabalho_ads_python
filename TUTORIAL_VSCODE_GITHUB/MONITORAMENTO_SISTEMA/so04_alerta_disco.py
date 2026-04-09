import psutil

# Limite definido como constante (10%)
LIMITE_CRITICO = 10.0

print(f"--- VERIFICANDO PARTIÇÕES CRÍTICAS (Espaço Livre < {LIMITE_CRITICO}%) ---")
print("-" * 60)

particoes = psutil.disk_partitions()
encontrou_critico = False

for p in particoes:
    try:
        uso = psutil.disk_usage(p.mountpoint)
        # Calcula a porcentagem de espaço LIVRE
        porcentagem_livre = 100 - uso.percent
        
        if porcentagem_livre < LIMITE_CRITICO:
            encontrou_critico = True
            print(f"⚠️ ALERTA NA PARTIÇÃO [{p.mountpoint}]")
            print(f"   Espaço Livre: {porcentagem_livre:.1f}%")
            print(f"   Espaço Total: {uso.total / (1024**3):.2f} GB")
            print("-" * 30)
    except:
        continue

if not encontrou_critico:
    print("Tudo certo! Todas as partições possuem espaço seguro.")
