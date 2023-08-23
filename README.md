# Tarea 2: Edmonds-Karp

Este programa implementa el algoritmo de Edmonds-Karp para encontrar el flujo máximo en una red de flujo. La entrada consiste en un grafo dirigido con capacidades en las aristas, y el objetivo es encontrar la cantidad máxima de flujo que puede enviarse desde un nodo fuente hasta un nodo sumidero respetando las capacidades de las aristas.

## Integrantes
- Juan Fernando - 201623311
- Juan Camilo Bonet - 202022466
- Laura Rodriguez - 201816069

## Instalación

Asegúrate de tener Python instalado en tu sistema. Luego, puedes instalar las dependencias utilizando el siguiente comando:

```bash
pip install matplotlib numpy networkx
```

## Uso

El programa puede ejecutarse desde la línea de comandos proporcionando un archivo de texto que contenga la información de la red de flujo como entrada.

```bash
python "$Path_archivo_python/maximum_flow.py" "$Path_archivo_datos"
```

## Formato de Entrada
El archivo de entrada debe seguir el siguiente formato:

La primera línea contiene un número entero N, que es la cantidad de nodos en el grafo.
Las líneas subsiguientes contienen tres enteros u, v y capacidad, que representan una arista desde el nodo u hasta el nodo v con una capacidad de capacidad.
Ejemplo de archivo de entrada:

```
6
0 1 4
0 2 3
1 4 3
1 2 2
2 3 2
3 5 5
4 3 4
4 2 5
```

## Salida
El programa muestra en pantalla el valor del flujo máximo y guarda la matriz de flujo en un archivo de salida llamado output.txt. También visualiza la red de flujo utilizando NetworkX y Matplotlib.

## Visualización
La visualización muestra la red de flujo con nodos, aristas, capacidades y flujos. El nodo fuente se posiciona a la izquierda, el nodo sumidero a la derecha y los demás nodos se distribuyen uniformemente entre ellos.

