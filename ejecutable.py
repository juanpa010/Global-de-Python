from clases import Detector, Radiacion, Virus, Sanador

def validar_posicion(fila, columna):
    """
    Valida si una posición está dentro de la matriz 6x6
    """
    return 0 <= fila <= 5 and 0 <= columna <= 5

def solicitar_posicion():
    """
    Solicita y valida la posición inicial para una mutación.
    """
    while True:
        try:
            print("\nPosición inicial:")
            print("- Fila puede ser de 0 a 5")
            print("- Columna puede ser de 0 a 5")
            
            fila = int(input("\nFila de inicio (0-5): "))
            columna = int(input("Columna de inicio (0-5): "))
            
            if validar_posicion(fila, columna):
                return fila, columna
            else:
                print("Error: La posición debe estar dentro de la matriz 6x6")
        except ValueError:
            print("Error: Ingrese números enteros válidos")

def solicitar_matriz():
    print("Ingrese el ADN (A, T, C, G)(6 filas de 6 caracteres cada una)")
    matriz = []
    for i in range(6):
        while True:
            fila = input(f"Fila {i+1}: ").upper()
            if len(fila) == 6 and all(base in ['A', 'T', 'C', 'G'] for base in fila):
                matriz.append(fila)
                break
            else:
                print("Error: Ingrese 6 caracteres válidos (A, T, C, G)")
    return matriz

def mostrar_matriz(matriz, titulo="Matriz actual"):
    print(f"\n{titulo}:")
    for fila in matriz:
        print(fila)

def main():
    print("Programa de Análisis de ADN")
    
    matriz = solicitar_matriz()
    mostrar_matriz(matriz, "ADN inicial")
    
    detector = Detector()
    
    while True:
        print("\nOpciones:")
        print("1. Detectar mutaciones")
        print("2. Mutar ADN")
        print("3. Sanar ADN")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            es_mutante = detector.detectar_mutantes(matriz)
            print(f"Resultado: {'Mutante' if es_mutante else 'No mutante'}")
        
        elif opcion == '2':
            print("\nTipos de mutación:")
            print("1. Mutación por Radiación (Horizontal/Vertical)")
            print("2. Mutación por Virus (Diagonal)")
            
            tipo_mutacion = input("Seleccione el tipo de mutación: ")
            
            while True:
                base = input("Ingrese la base nitrogenada a mutar (A, T, C, G): ").upper()
                if base in ['A', 'T', 'C', 'G']:
                    break
                print("Error: Base nitrogenada no válida")
            
            try:

                if tipo_mutacion == '1':
                    while True:
                        orientacion = input("Orientación (H/V): ").upper()
                        if orientacion in ['H', 'V']:
                            break
                        print("Error: Orientación no válida")

                    fila, columna = solicitar_posicion()
                    radiacion = Radiacion(base)
                    nueva_matriz = radiacion.crear_mutante(base, matriz, (fila, columna), orientacion)
                    matriz = nueva_matriz  

                elif tipo_mutacion == '2':
                    print("\nDirección de la diagonal:")
                    print("1. Hacia abajo-derecha (↘)")
                    print("2. Hacia abajo-izquierda (↙)")
                    while True:
                        direccion = input("Seleccione la dirección (1/2): ")
                        if direccion in ['1', '2']:
                            break
                        print("Error: Dirección no válida")

                    direccion = "SE" if direccion == '1' else "SW"
                    fila, columna = solicitar_posicion()
                    virus = Virus(base)
                    nueva_matriz = virus.crear_mutante(base, matriz, (fila, columna), direccion)
                    matriz = nueva_matriz  

                    detector = Detector(umbral_mutaciones=2)
                    mutantes_detectados = detector.detectar_mutantes(matriz)
                    print(f"Mutantes detectados: {mutantes_detectados}")

                


                else:
                    print("Opcion inválida")
                
                mostrar_matriz(matriz, "Nuevo ADN")

                
                es_mutante = detector.detectar_mutantes(matriz)
                print(f"Resultado de la detección de mutantes: {'Mutante' if es_mutante else 'No mutante'}")
                
            except ValueError as e:
                print(f"Error: {str(e)}")
        
        elif opcion == '3':
            sanador = Sanador()
            matriz = sanador.sanar_mutantes(matriz)
            mostrar_matriz(matriz, "ADN sanado")
        
        elif opcion == '4':
            print("¡Gracias por usar el Programa de Análisis de ADN!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
