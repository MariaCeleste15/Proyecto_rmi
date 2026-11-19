import Pyro5.api

def ejecutar_cliente_rmi():
    uri = input("Pegue el URI del servidor RMI (ej. PYRO:obj_...@localhost:...): ").strip()
    servicio = Pyro5.api.Proxy(uri)

    try:
        produccion = float(input("Ingrese la produccion total: ").strip())
        trabajadores = int(input("Ingrese el numero de trabajadores: ").strip())
        resultado = servicio.calcular_promedio(produccion, trabajadores)
        print("[RESPUESTA REMOTA RMI]:", resultado)
    except ValueError:
        print("[ERROR]: Debe ingresar valores numericos validos.")

if __name__ == "__main__":
    ejecutar_cliente_rmi()