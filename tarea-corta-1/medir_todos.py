import subprocess

algoritmos = ["algoritmo-1.py", "algoritmo-2.py", "algoritmo-3.py", "algoritmo-4.py"]
valores_n = [100, 1000, 10000, 100000, 1000000]

for algo in algoritmos:
    for n in valores_n:
        try:
            result = subprocess.run(
                ["python3", algo],
                input=str(n),
                capture_output=True,
                text=True,
                timeout=60
            )
            print(result.stdout)
        except subprocess.TimeoutExpired:
            print(f"\n{algo} con n={n} Este supera 1 minuto, lo aborte, saltando...\n")
            break