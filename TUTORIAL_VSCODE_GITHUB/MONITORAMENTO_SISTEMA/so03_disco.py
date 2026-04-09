import psutil

print(f"{'Partição':<10} | {'Total':<10} | {'Usado':<10} | {'Livre':<10} | {'%':<5}")
print("-" * 60)

for particao in psutil.disk_partitions():
    try:
        uso = psutil.disk_usage(particao.mountpoint)
        print(f"{particao.mountpoint:<10} | {uso.total/(1024**3):.1f} GB | {uso.used/(1024**3):.1f} GB | {uso.free/(1024**3):.1f} GB | {uso.percent}%")
    except:
        continue # Ignora unidades de CD ou pendrives vazios
