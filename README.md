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


## Unidad 5 - Aproximación de Funciones
   ```
  python u5.py
  ```
El resultado se guarda en un archivo llamado ***`aproximacion.docx`***, ubicado en el mismo directorio que `u5.py`

Supongamos que nos dan la siguiente tabla:

|  X  |   Y  |
|:---:|:----:|
|  0  |   0  |
|  1  |   2  |
|  1  |   3  |
|  2  |   5  |
|  3  |   8  |
| 4.5 |  12  |
|  5  | 12.5 |

Y también nos dan las siguientes funciones:
**f1(x)** = c1.x + c2  
**f2(x)** = c1.x^2 + c2.x + c3  
**f3(x)** = c1.e^x + c2  
**f4(x)** = c1.ln(x+1) + c2.x  

-----
***Desarrollo:***

Vemos que en la tabla de valores, se tiene 7 columnas, por lo que:  

>***Cuantos valores desea ingresar?:*** `7`  

Luego tenemos que ir colocando uno por uno los valores de cada columna, de la siguiente manera:  
>***Ingrese el valor 0 en y:*** `0`  
***Ingrese el valor 1 en y:*** `2`  
***Ingrese el valor 2 en y:*** `3`  
***Ingrese el valor 3 en y:*** `5`  
***Ingrese el valor 4 en y:*** `8`  
***Ingrese el valor 5 en y:*** `12`  
***Ingrese el valor 6 en y:*** `12.5`  
----------
>***Ingrese el valor 0 en x:*** `0`  
***Ingrese el valor 1 en x:*** `1`  
***Ingrese el valor 2 en x:*** `1`  
***Ingrese el valor 3 en x:*** `2`  
***Ingrese el valor 4 en x:*** `3`  
***Ingrese el valor 5 en x:*** `4.5`  
***Ingrese el valor 6 en x:*** `5`  

Nos dieron 4 funciones, por lo que:  
>***Cuantas funciones desea ingresar?:*** `4`  
***Ingrese la funcion 1:*** `c*x+c`  
***Ingrese la funcion 2:*** `c*(x^2)+c*x+c`  
***Ingrese la funcion 3:*** `c*(e^x)+c`  
***Ingrese la funcion 4:*** `c*ln(x+1)+c*x`  
Y automáticamente se genera el archivo de salida ***`aproximacion.docx`***



## Unidad 6 - Aproximación de Raíces
   ```
  python u6.py
  ```
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
  





