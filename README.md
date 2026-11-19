# Aplicación Cliente-Servidor con RMI: Producción Promedio

Proyecto de **Sistemas Distribuidos** que implementa una arquitectura cliente-servidor utilizando **RMI (Remote Method Invocation)** en Python con la librería **Pyro5**, aplicado al cálculo de producción promedio por trabajador con validación de restricciones.

## 1. Guía de RMI (Remote Method Invocation)

**RMI** es un modelo de comunicación distribuida en el que un programa cliente puede invocar métodos de un objeto que se encuentra en otro proceso o máquina (el servidor), de forma similar a una llamada a método local.

### Conceptos clave
* **Objeto remoto (`@Pyro5.api.expose`):** Clase en el servidor cuyos métodos quedan expuestos para ser llamados de forma remota.
* **Daemon (`Pyro5.api.Daemon`):** Proceso del servidor que escucha peticiones remotas y despacha las llamadas al objeto expuesto.
* **URI (Uniform Resource Identifier):** Dirección única que identifica el objeto remoto registrado en el servidor (por ejemplo: `PYRO:obj_...@localhost:puerto`).
* **Proxy (`Pyro5.api.Proxy`):** Representación local del objeto remoto en el cliente que oculta los detalles de red y serialización.

## 2. Estructura del proyecto

* `servidor_rmi.py`: Expone la clase `CalculadoraProduccion` y mantiene el `Daemon` escuchando llamadas remotas.
* `cliente_rmi.py`: Se conecta mediante `Proxy` usando el URI del servidor y envía los datos de producción y número de trabajadores.
* `README.md`: Guía teórica y práctica del proyecto.

## 3. Requisitos e instalación

1. Tener instalado **Python 3.x**.
2. Instalar `Pyro5` en la terminal:

```bash
pip install Pyro5