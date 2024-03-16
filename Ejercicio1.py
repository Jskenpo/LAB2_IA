class GrafoAustralia:
    def __init__(self, regiones):
        self.regiones = regiones
        self.soluciones = []

    def es_seguro(self, region, color, colores_asignados):
        for vecino in self.regiones[region]:
            if vecino in colores_asignados and colores_asignados[vecino] == color:
                return False
        return True

    def encontrar_soluciones_util(self, regiones, colores_asignados, idx):
        if idx == len(regiones):
            self.soluciones.append(colores_asignados.copy())
            return

        region = regiones[idx]
        for color in ['rojo', 'azul', 'verde']:
            if self.es_seguro(region, color, colores_asignados):
                colores_asignados[region] = color
                self.encontrar_soluciones_util(regiones, colores_asignados, idx + 1)
                colores_asignados.pop(region)

    def encontrar_soluciones(self):
        regiones_list = list(self.regiones.keys())
        colores_asignados = {}
        self.soluciones = []
        self.encontrar_soluciones_util(regiones_list, colores_asignados, 0)

    def imprimir_soluciones(self):
        if not self.soluciones:
            print("No se encontraron soluciones.")
            return

        for i, solucion in enumerate(self.soluciones, 1):
            print("Solución", i, ":")
            for region, color in solucion.items():
                print(region, ":", color)
            print()

# Definir las regiones de Australia y sus vecinos
regiones_australia = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'QLD'],
    'SA': ['WA', 'QLD', 'NT', 'NSW', 'VIC'],
    'NSW': ['QLD', 'SA', 'VIC'],
    'VIC': ['SA', 'NSW'],
    'QLD': ['NT', 'SA', 'NSW'],
    'TAS': []
}

# Crear el grafo de Australia
grafo_australia = GrafoAustralia(regiones_australia)

# Encontrar todas las soluciones posibles
grafo_australia.encontrar_soluciones()

# Imprimir las soluciones encontradas
grafo_australia.imprimir_soluciones()
