import Pyro5.api

@Pyro5.api.expose
class CalculadoraProduccion:
    def calcular_promedio(self, produccion: float, trabajadores: int) -> str:
        if trabajadores <= 0:
            return "ERROR: El numero de trabajadores debe ser mayor que 0."
        promedio = produccion / trabajadores
        return f"OK: Produccion promedio por trabajador = {promedio:.2f}"

def iniciar_servidor_rmi():
    daemon = Pyro5.api.Daemon()
    uri = daemon.register(CalculadoraProduccion)
    print("[SERVIDOR RMI] Objeto registrado correctamente.")
    print("Copia este URI para el cliente:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    iniciar_servidor_rmi()