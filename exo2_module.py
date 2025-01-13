
def addition(n, max=10):
  result = 0
  print(f"Table d'addition de {n}")
  for i in range(max):
    result = n + (i + 1)
    print(f"{n:>4} + {(i + 1):>4}  = {result:>4}")

def multiplication(n, max=10):
  result = 0
  print(f"Table de multiplication de {n}")
  for i in range(max):
    result = n * (i + 1)
    print(f"{n:>4} x {(i + 1):>4}  = {result:>4}")

# Execute le code si le module est exécuté directement
if __name__ == "__main__":
  a = 6
  b = 12
  addition(a)
  multiplication(b)

  input("Press Enter to continue from module...")