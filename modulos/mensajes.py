def asegurar_rango(min, max):
    retornar = False
    while (retornar < min) or (retornar > max) or (retornar == False):
        try:
            retornar = int(input('Ingrese la opcion elegida (numero): '))
        except:
            print('Error, tiene que ser un numero.')
        if ((retornar < min) or (retornar > max)) and (retornar != False):
            print('Recuerde que tiene que estar dentro de las opciones establecidas')
    return retornar


def opciones_principales():
    msg = 'Seleccione que tipo de calculo desea efectuar\n' \
          '1- Una Ec. Diferencial de Primer Orden\n' \
          '2- Varias Ecs. Diferenciales de Primer Orden\n' \
          '3- Una Ec. Diferencial de Orden Superior (2do orden)\n' \
          '4- Una Ec. Diferencial de Orden Superior (3er orden)\n'
    print(msg)
    return asegurar_rango(1, 4)


def opciones_tipo_a():
    msg = 'Ha seleccionado Ecuacion Diferencial Ordinaria de primer orden con condiciones iniciales\n' \
          'Seleccione el metodo de resolucion\n' \
          '1- Metodo de Euler\n' \
          '2- Metodo de Euler Mejorado\n' \
          '3- Runge Kutta de Cuarto Orden\n'
    print(msg)
    return asegurar_rango(1, 3)


def opciones_tipo_b():
    msg = 'Ha seleccionado Sistema de Ecuaciones Diferenciales Ordinarias de primer orden con condiciones iniciales\n' \
          'Seleccione el metodo de resolucion\n' \
          '1- Metodo de Euler\n' \
          '2- Metodo de Euler Mejorado\n' \
          '3- Runge Kutta de Cuarto Orden\n'
    print(msg)
    return asegurar_rango(1, 3)


def opciones_tipo_c():
    msg = 'Ha seleccionado Ecuacion Diferencial Ordinaria de Orden Superior (2do orden) con condiciones iniciales\n' \
          'Seleccione el metodo de resolucion\n' \
          '1- Metodo de Euler\n' \
          '2- Metodo de Euler Mejorado\n' \
          '3- Runge Kutta de Cuarto Orden\n'
    print(msg)
    return asegurar_rango(1, 3)

def opciones_tipo_d():
    msg = 'Ha seleccionado Ecuacion Diferencial Ordinaria de Orden Superior (3er orden) con condiciones iniciales\n' \
          'Seleccione el metodo de resolucion\n' \
          '1- Metodo de Euler\n' \
          '2- Metodo de Euler Mejorado\n' \
          '3- Runge Kutta de Cuarto Orden\n'
    print(msg)
    return asegurar_rango(1, 3)
