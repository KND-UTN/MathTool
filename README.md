# MathTool
Software especializado en 3 tareas matematicas:

 - Aproximación de Funciones mediante el metodo de Mínimos Cuadrados
 - Aproximación a raices de ecuaciones no lineales mediante el método iterativo de Newton - Raphson
 - Resolución de ecuaciones diferenciales ordinarias con condiciones iniciales
 
Escrito en **Python**. Librerías necesarias:
- pandas
- numpy
- sympy
- python-docx
- matplotlib

## Consideraciones
- Usar puntos, **NO** comas
- Para simbolizar los exponentes, se puede utilizar " ^ " o " ** ", por ejemplo: 2^3, que es lo mismo que escribir 2**3
- Es posible que en las salidas aparezca 2.718281 en vez de la letra "e", recordar que son **equivalentes**
- **No obviar multiplicaciones:** si en papel tenemos 2x + 3ln(5x+4e), se deben colocar los asteriscos que demarcan la multiplicación, es decir
       ```
        2*x + 3 * ln(5 * x + 4 * e)
        ```
- En la unidad 6, se puede utilizar la función **derivada(x)** para obtener la derivada de una función (ejemplos mas abajo).
- Formas de escribir los siguientes simbolos (reemplazar **"x"** por el correspondiente contenido en la ecuación):
    - **euler:** e
    - **logaritmo natural:** ln(x)
    - **seno:** sin(x)
    - **coseno:** cos(x)


## Ejemplos Unidad 5 - Aproximación de Funciones


## Unidad 6 - Aproximación de Raíces
Todo se muestra por consola.

**Consideración:** 

- Encontrar la raíz de la siguiente ecuación no lineal: e^(1/(x-6)) - 0,5x + 1,5
    - Lo que se debe introducir es
         ```
        e^(1/(x-6)) - 0.5*x + 1.5
        ```
    
- Dada la siguiente función: f(x) = 0,2x^2 – 2ln(x – 2) +e^0,2x<br/>Encontrar el valor de x que corresponda a un mínimo local de la función
    - Lo que se debe introducir es
         ```
        derivada(0.2*x^2 – 2*ln(x – 2) +e^((0.2*x)))
        ```
  





