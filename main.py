saludos = []
print("Introduce nombres (escribe 'fin' para terminar):")

while True:
    nombre = input("¿Cuál es tu nombre? ")
    if nombre.lower() == 'fin':
        break
    saludos.append(nombre)

print("\nSaludos generados:")
for n in saludos:
    print(f"Hola, {n}! Bienvenido a tu primer proyecto.")