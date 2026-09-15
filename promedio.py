# Programa para calcular el promedio, nota mayor, nota menor y resultado final

# 1. Pedimos al usuario cuántas notas quiere calcular
cantidad = int(input("¿Cuántas notas vas a ingresar?: "))

# Creamos una lista vacía para ir guardando las notas
notas = []

# 2. Usamos un ciclo 'for' para pedir cada una de las notas
for i in range(cantidad):
    # Usamos float() para que acepte números con decimales (como 3.5 o 4.2)
    nota = float(input(f"Ingresa la nota {i + 1}: "))
    notas.append(nota)

# Verificamos que la cantidad sea mayor a 0 para no tener errores matemáticos
if cantidad > 0:
    
    # 3. Hacemos los cálculos
    promedio = sum(notas) / cantidad
    nota_mayor = max(notas)
    nota_menor = min(notas)

    # 4. Determinamos el resultado final
    # Asumimos que se aprueba con 3.0 o más (escala de 1 a 5)
    if promedio >= 3.0:
        resultado_final = "Aprobado 🥳"
    else:
        resultado_final = "Reprobado 😔"

    # 5. Mostramos los resultados en pantalla
    print("\n--- RESULTADOS DEL ESTUDIANTE ---")
    
    # El :.2f sirve para redondear el promedio a solo dos decimales
    print(f"Promedio: {promedio:.2f}") 
    print(f"Nota mayor: {nota_mayor}")
    print(f"Nota menor: {nota_menor}")
    print(f"Resultado final: {resultado_final}")

else:
    print("No ingresaste ninguna nota para calcular.")
