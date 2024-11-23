import random

class Detector:
    def __init__(self, umbral_mutaciones=2):
        self.umbral_mutaciones = umbral_mutaciones
    
    def _buscar_horizontal(self, matriz):
        for fila in matriz:
            for base in ['A', 'T', 'C', 'G']:
                if fila.count(base) >= 4:
                    return True
        return False
    
    def _buscar_vertical(self, matriz):
        for columna in range(len(matriz[0])):
            columna_actual = ''.join(fila[columna] for fila in matriz)
            for base in ['A', 'T', 'C', 'G']:
                if columna_actual.count(base) >= 4:
                    return True
        return False
    
    def _buscar_diagonal(self, matriz):
        n = len(matriz)
        # Diagonales principales (↘)
        for i in range(n):
            for j in range(n):
                # Verificar si hay espacio para una diagonal desde (i,j)
                diagonal = []
                fila, col = i, j
                while fila < n and col < n:
                    diagonal.append(matriz[fila][col])
                    fila += 1
                    col += 1
                diagonal_str = ''.join(diagonal)
                for base in ['A', 'T', 'C', 'G']:
                    if diagonal_str.count(base) >= 4:
                        return True
                        
        # Diagonales secundarias (↙)
        for i in range(n):
            for j in range(n-1, -1, -1):
                diagonal = []
                fila, col = i, j
                while fila < n and col >= 0:
                    diagonal.append(matriz[fila][col])
                    fila += 1
                    col -= 1
                diagonal_str = ''.join(diagonal)
                for base in ['A', 'T', 'C', 'G']:
                    if diagonal_str.count(base) >= 4:
                        return True
                        
        return False
    
    def detectar_mutantes(self, matriz):
        mutaciones = (
            self._buscar_horizontal(matriz) +
            self._buscar_vertical(matriz) +
            self._buscar_diagonal(matriz)
        )
        return mutaciones >= self.umbral_mutaciones

class Mutador:
    def __init__(self, base_nitrogenada=None):
        self.base_nitrogenada = base_nitrogenada
    
    def validar_posicion(self, matriz, posicion_inicial, tipo_mutacion=None):
        filas = len(matriz)
        columnas = len(matriz[0]) if matriz else 0
        fila, columna = posicion_inicial
        
        if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
            return False
            
        return True

class Radiacion(Mutador):
    def __init__(self, base_nitrogenada, intensidad=1):
        super().__init__(base_nitrogenada)
        self.intensidad = intensidad
    
    def crear_mutante(self, base_nitrogenada, matriz, posicion_inicial, orientacion_de_la_mutacion):
        if not isinstance(matriz, list) or not matriz:
            raise ValueError("Matriz inválida")
            
        matriz_mutada = [list(fila) for fila in matriz]
        fila, columna = posicion_inicial
        longitud = min(4, len(matriz) - max(fila, columna))
        
        if not self.validar_posicion(matriz, posicion_inicial):
            raise ValueError(f"Posición inicial {posicion_inicial} inválida")
        
        try:
            if orientacion_de_la_mutacion == "H":
                for i in range(min(4, len(matriz[0]) - columna)):
                    matriz_mutada[fila][columna + i] = base_nitrogenada
            
            elif orientacion_de_la_mutacion == "V":
                for i in range(min(4, len(matriz) - fila)):
                    matriz_mutada[fila + i][columna] = base_nitrogenada
            
            return [''.join(fila) for fila in matriz_mutada]
            
        except Exception as e:
            raise ValueError(f"Error al crear mutante: {str(e)}")

class Virus(Mutador):
    def __init__(self, base_nitrogenada, virulencia=1):
        super().__init__(base_nitrogenada)
        self.virulencia = virulencia
    
    def crear_mutante(self, base_nitrogenada, matriz, posicion_inicial, direccion="SE"):
        """
        Crea una mutación diagonal.
        direccion puede ser:
        - "SE" (↘): diagonal hacia abajo-derecha
        - "SW" (↙): diagonal hacia abajo-izquierda
        """
        if not isinstance(matriz, list) or not matriz:
            raise ValueError("Matriz inválida")
            
        matriz_mutada = [list(fila) for fila in matriz]
        fila, columna = posicion_inicial
        
        if not self.validar_posicion(matriz, posicion_inicial):
            raise ValueError(f"Posición inicial {posicion_inicial} inválida")
        
        try:
            if direccion == "SE":  # Diagonal hacia abajo-derecha ↘
                i = 0
                while (fila + i < len(matriz) and 
                       columna + i < len(matriz[0])):
                    matriz_mutada[fila + i][columna + i] = base_nitrogenada
                    i += 1
            
            else:  # Diagonal hacia abajo-izquierda ↙
                i = 0
                while (fila + i < len(matriz) and 
                       columna - i >= 0):
                    matriz_mutada[fila + i][columna - i] = base_nitrogenada
                    i += 1
            
            return [''.join(fila) for fila in matriz_mutada]
            
        except Exception as e:
            raise ValueError(f"Error al crear mutante: {str(e)}")

class Sanador:
    def __init__(self, detector=None):
        self.detector = detector or Detector()
    
    def sanar_mutantes(self, matriz):
        intentos_maximos = 10
        
        for _ in range(intentos_maximos):
            nueva_matriz = [
                ''.join(random.choice(['A', 'T', 'C', 'G']) for _ in range(6))
                for _ in range(6)
            ]
            
            if not self.detector.detectar_mutantes(nueva_matriz):
                return nueva_matriz
        
        return matriz  # Si no logra encontrar una matriz sana
