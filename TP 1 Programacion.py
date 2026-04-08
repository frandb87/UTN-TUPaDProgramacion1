# EJERCICIO 1 "Caja del Kiosco"

#Pido el nombre al cliente
nombre = input("Ingrese su nombre a continuación: ").strip()   

#Valido que el nombre del cleinte no este vacio y contenga solo letras
while not nombre.isalpha() or nombre == "":  
 nombre = input("Por favor, ingrese un nombre que contenga solo letras: ")

#Pido la cantidad de productos en formato de string
productos = input("Ingrese la cantidad de productos: ").strip() 

#Valido que la cantidad ingresada un entero positivo
while not productos.isdigit() or int(productos) == 0:  
 productos = input("Por favor, ingrese un número entero y positivo mayor a 0: ")

#Convierto la cantidad a entero
productos = int(productos)

#Defino las variables
total_sin_descuento = 0
total_con_descuento = 0.0

#Creo un bucle for para ver cada producto
for i in range (1, productos+1):
    #Pedimos precio como string
    precio = input(f"Producto {i} - Precio: ").strip()

    while not precio.isdigit() or int(precio) == 0:
      precio = input("Por favor ingrese un número entero positivo mayor a 0: ")

    #Convierto el precio a entero
    precio = int(precio)

    #Consulto el descuento
    descuento = input("Tiene descuento (S/N): ").strip().lower()

    #Valido si se ingresa solo S o N
    while descuento != "s" and descuento != "n":
      descuento = input("Por favor ingrese solo S o N: ")

    total_sin_descuento += precio

    if descuento == "s":
      precio_total = precio * 0.9
    else:
      precio_total = precio

    total_con_descuento += precio_total

ahorro_total = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / productos

print()
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: {promedio:.2f}")


# EJERCICIO 2 "IAcceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta= "python123"
#Creamos la variable for para solicitar el usuario y clave un maximo de 3 veces
for i in range (3):
    usuario = input("Ingrese el nombre de usuario: ").strip()
    clave= input("Ingrese la clave: ").strip()
    #Verificamos si es correcto y permitimos el acceso
    if usuario == usuario_correcto and clave == clave_correcta:
     print("Acceso concedido")
     print("")
     #Creamos el menu con un bucle while
     while True:
       print("Menu:")
       print("1) Ver estado de inscripcion")
       print("2) Cambiar clave" )
       print("3) Mostrar mensaje motivacional")
       print("4) Salir") 

       opcion = input("Ingrese una opción: ").strip()
       #Verificamos que elija una opcion valida
       if not opcion.isdigit():
         print("Debe ingresar un número")
         print("")
         continue
       
       opcion = int(opcion)

       if opcion <1 or opcion >4:
         print("Debe ingresar un número entre 1 y 4")
         print("")
         continue
       
       if opcion == 1:
         print("Inscripto")
         print("")

       elif opcion == 2:
         while True:
          nueva_clave1 = input("Ingrese su nueva clave: ").strip()
          if len(nueva_clave1) < 6:
            print("La nueva clave debe tener al menos 6 caracteres")
            continue
          nueva_clave2 = input("Confirme su nueva clave: ").strip()

          if nueva_clave1 == nueva_clave2:
           clave = nueva_clave1
           print("Clave cambiada con exito")
           print("")
           break
          else:
           print("Las claves deben coincidir, intente nuevamente")
       
       elif opcion == 3:
         print("Vas por buen camino, no bajes los brazos!!!")
         print("")
       
       else:
         print("Saliendo del programa")
         print("")
         break
         
     break

    else:
     if i <2:
      print("Usuario o clave incorrecta, intente nuevamente")

else:
  print("Cuenta bloqueada")


# EJERCICIO 3 “Agenda de Turnos con Nombres (sin listas)”

while True:
    nombre = input("Ingrese el nombre del operador: ").strip()
    
    if nombre.isalpha():
        break
    else:
        print("El nombre debe contener solo letras")

turnos_lunes = 0
turnos_martes = 0

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:

    print("1) Reservar turno")
    print("2) Cancelar turno (por nombre)")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Ingrese una opción: ").strip()
    print("")

    if not opcion.isdigit():
     print("Debe ingresar un número")
     print("")
     continue

    opcion = int(opcion)

    if opcion <1 or opcion >5:
       print("Debe ingresar un número entre el 1 y el 5")

    if opcion == 1:
       
       while True:
          
          print("1) Lunes")
          print("2) Martes")
          print("3) Regresar al menú principal")

          dia = input("Seleccione el día del turno: ").strip()

          if not dia.isdigit():
             print("Debe ingresar 1 para día Lunes o 2 para día Martes o 3 para regresar")
             print("")
             continue
          
          dia = int(dia)

          if dia == 3:
             break

          if dia != 1 and dia !=2:
             print("Debe ingresar 1 para día Lunes, 2 para día Martes o 3 para regresar")
             print("")
             continue   

          while True:
            paciente = input("Ingrese el nombre del paciente: ").strip()

            if paciente.isalpha():
                break
            else:
                print("El nombre debe contener solo letras")

          if dia == 1:
             if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno asignado")
             else:
                if lunes1 == "":
                   lunes1 = paciente
                   turnos_lunes += 1
                   print("Turno asignado")
                   
                elif lunes2 == "":
                   lunes2 = paciente
                   turnos_lunes += 1
                   print("Turno asignado")
                   
                elif lunes3 == "":
                   lunes3 = paciente
                   turnos_lunes += 1
                   print("Turno asignado")
                   
                elif lunes4 == "":
                   lunes4 = paciente
                   turnos_lunes += 1
                   print("Turno asignado")
                   
                else:
                   print("No hay turnos disponibles para el día Lunes")

          if dia == 2:
             if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno asignado")
             else:
                if martes1 == "":
                   martes1 = paciente
                   turnos_martes += 1
                   print("Turno asignado")
                   
                elif martes2 == "":
                   martes2 = paciente
                   turnos_martes += 1
                   print("Turno asignado")
                   
                elif martes3 == "":
                   martes3 = paciente
                   turnos_martes += 1
                   print("Turno asignado")
                   
                else:
                   print("No hay turnos disponibles para el día Martes")
                   print("")

    if opcion == 2:

       while True:
          
          print("1) Lunes")
          print("2) Martes")

          dia = input("Seleccione el día del turno: ").strip()

          if not dia.isdigit():
             print("Debe ingresar 1 para día Lunes o 2 para día Martes")
             print("")
             continue
          
          dia = int(dia)
          
          if dia != 1 and dia !=2:
             print("Debe ingresar 1 para día Lunes o 2 para día Martes")
             print("")
             continue

          while True:
             paciente = input("Ingrese el nombre del paciente: ").strip()

             if paciente.isalpha():
                break
             else:
                print("El nombre debe contener solo letras")

          if dia == 1:
             if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("Turno cancelado")
                if lunes1 == paciente:
                   lunes1 = ""
                   turnos_lunes -= 1
                elif lunes2 == paciente:
                   lunes2 = ""
                   turnos_lunes -= 1
                elif lunes3 == paciente:
                   lunes3 = ""
                   turnos_lunes -= 1
                elif lunes4 == paciente:
                   lunes4 = ""
                   turnos_lunes -= 1
             else:
                print("El paciente no tiene un turno asignado")

          elif dia == 2:
             if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Turno cancelado")
                if martes1 == paciente:
                   martes1 = ""
                   turnos_martes -= 1
                elif martes2 == paciente:
                   martes2 = ""
                   turnos_martes -= 1
                elif martes3 == paciente:
                   martes3 = ""
                   turnos_martes -= 1
             else:
                print("El paciente no tiene un turno asignado")
          break
       print("")


    if opcion == 3:

       print("Agenda de turnos")
       print("")
       print("Día Lunes:")
       print(f"Turno 1: {lunes1 if lunes1 != "" else "(libre)"}")
       print(f"Turno 2: {lunes2 if lunes2 != "" else "(libre)"}")
       print(f"Turno 3: {lunes3 if lunes3 != "" else "(libre)"}")
       print(f"Turno 4: {lunes4 if lunes4 != "" else "(libre)"}")
       print("")
       print("Día Martes:")
       print(f"Turno 1: {martes1 if martes1 != "" else "(libre)"}")
       print(f"Turno 2: {martes2 if martes2 != "" else "(libre)"}")
       print(f"Turno 3: {martes3 if martes3 != "" else "(libre)"}")
       print("")
       print("")

    if opcion == 4:

       print ("Resumen general")
       print("")
       print(f"Turnos ocupados día Lunes : {turnos_lunes}")
       print(f"Turnos disponibles día Lunes: {4 - turnos_lunes}")
       print("")
       print(f"Turnos ocupados día Martes : {turnos_martes}")
       print(f"Turnos disponibles día Martes: {3 - turnos_martes}")

       if turnos_lunes > turnos_martes:
          print("El día lunes hay mas turnos ocupados")
       elif turnos_martes > turnos_lunes:
          print("El día Martes hay mas turnos ocupados")
       else:
          print("Hay empate de turnos ocupados en ambos dias")
          print("")

    if opcion == 5:
       print("Cerrando el sistema...")
       break
    

# EJERCICIO 4 “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_cerradura = 0

while True:

 nombre = input("Ingrese su nombre: ").strip()
 if nombre.isalpha():
  print("")
  print(f"Buen día agente {nombre}!")
  print("")
  break
 else:
  print("ERROR!!! Por favor, ingrese un nombre valido (solo letras)")

while True:

 if alarma == True and tiempo <= 3 and cerraduras_abiertas <3:
   print("Alarma activada y te queda poco tiempo.. El sistema se ha bloqueado")
   print("GAME OVER")
   print("")
   break

 if cerraduras_abiertas == 3:
   print("Lo has logrado! Todas las cerraduras estan desbloquedas!!!")
   print("VICTORIA!!!")
   print("")
   break
 
 if energia <= 0 or tiempo <= 0:
   print("Tu tiempo o energia no son suficientes")
   print("GAME OVER")
   print("")
   break
 
   print (f"Tu energia actual es {energia} %")
   print (f"Tiempo: {tiempo}")
   print (f"Cerraduras abiertas : {cerraduras_abiertas}")

 print("Elige tu siguiente accion:")
 print("")
 print("1- Forzar cerradura")
 print("2- Hackear panel")
 print("3- Descansar")
 print("")

 opcion = input("Ingrese una opción: ").strip()
 print("")

 if not opcion.isdigit():
  print("ERROR!!! Debe ingresar un número")
  print("")
  continue

 opcion = int(opcion)

 if opcion <1 or opcion >3:
  print("ERROR!!! debe ingresar un número entre el 1 y el 3")
  print("")
  continue

 if opcion == 1:
    
    forzar_cerradura += 1
    energia -= 20
    tiempo -= 2

    if forzar_cerradura == 3:
     alarma = True
     print("ALARMA ACTIVADA!!! Cerradura bloqueada")
     print("")
     continue

    elif energia <40:
     print("Riego de Alarma!!!")
     
     while True:
       
       print ("Elije un número: 1 - 2 - 3")

       numero = input("El número es: ").strip()

       if not numero.isdigit():
        print("ERROR!!! Debes elegir un número")
        print("")
        continue
    
       numero = int(numero)

       if numero <1 or numero >3:
         print("ERROR!!! debe ingresar un número entre el 1 y el 3")
         print("")
         continue

       if numero == 3:
        alarma = True
        print("ALARMA ACTIVADA!!! Cerradura bloqueada")
        print("")

       else:
        print ("Cerradura abierta")
        cerraduras_abiertas += 1
        print("")

       break

    else:
        print ("Cerradura abierta")
        cerraduras_abiertas += 1
        print("")

    print (f"Tu energia actual es {energia} %")
    print (f"Tiempo: {tiempo}")
    print (f"Cerraduras abiertas : {cerraduras_abiertas}")

 if opcion == 2:

    forzar_cerradura = 0
    energia -= 10
    tiempo -= 3

    for i in range (4):
      codigo_parcial += "A"
      print (f"Hackeando sistema... Paso {i+1} de 4 - Codigo actual: {codigo_parcial}")
      print("")

    if len(codigo_parcial) >= 8:
      if cerraduras_abiertas <3:
        cerraduras_abiertas +=1
        print("Sistenma hackeado!! Cerradura abierta")
        print("")
      else:
        print("Sistenma hackeado!! Todas las cerraduras se encuentran abiertas")
        print("")

    print (f"Tu energia actual es {energia} %")
    print (f"Tiempo: {tiempo}")
    print (f"Cerraduras abiertas : {cerraduras_abiertas}")

 if opcion == 3:

    forzar_cerradura = 0
    tiempo -= 1

    if alarma == True:
      energia += 5
      print("ALARMA ACTIVADA!!! Solo recuperas 5 de energia")
      print("")

    else:
      energia += 15
      print("Recuperaste 15 de energia")
      print("")
    
    if energia > 100:
      energia = 100

    print (f"Tu energia actual es {energia} %")
    print (f"Tiempo: {tiempo}")
    print (f"Cerraduras abiertas : {cerraduras_abiertas}")


# EJERCICIO 5 “Escape Room:"La Arena del Gladiador"

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base = 15
daño_base_enemigo = 12
turno_gladiador = True
daño_final = 0

while True:

 nombre = input("Ingrese el nombre del gladiador: ").strip()
 if nombre.isalpha():
  print("")
  print(f"Bienvenido a la arena Gladiador {nombre}!!!")
  print("")
  break
 else:
  print("ERROR!!! Solo se permiten letras")

while vida_gladiador > 0 and vida_enemigo > 0:

 print(f"Vida gladiador \3 {vida_gladiador}")
 print(f"Vida enemigo   \3 {vida_enemigo}")
 print(f"Posiciones       {pociones}")
 print("")

 while True:
  
  print("Proximo movimiento: ")
  print("1. Ataque pesado")
  print("2. Rafaga Veloz")
  print("3. Curar")

  opcion = input("Eilje una opcion: ")
  print("")

  if not opcion.isdigit():
   print("ERROR!!! Debe ingresar un número")
   print("")
   continue

  opcion = int(opcion)

  if opcion <1 or opcion >3:
   print("ERROR!!! debe ingresar un número entre el 1 y el 3")
   print("")
   continue

  if opcion == 1:

   print("Ataque pesado!!")

   if vida_enemigo < 20:

     print("Golpe critico")
     daño_critico = daño_base * 1.5
     vida_enemigo -= daño_critico
     print (f"¡Atacaste al enemigo por {daño_critico} puntos de daño!")

   
   else:
     vida_enemigo -= daño_base
     print (f"¡Atacaste al enemigo por {daño_base} puntos de daño!")
   break

  if opcion == 2:

   print("Rafaga veloz!!")

   for i in range(3):
       vida_enemigo -= 5
       print (f"{i+1} golpe conectado por 5 de daño")

   break

  if opcion == 3:

   print("Curar!!")

   if pociones > 0:

    vida_gladiador += 30
    pociones -= 1

    print("Has recuperado 30 puntos de vida")
    break


   else:
 
    print("No te quedan posiones, pierdes tu turno")
    break


 vida_gladiador -= daño_base_enemigo
 print("¡El enemigo te atacó por 12 puntos de daño!")
 print("")

if vida_gladiador > 0:
 print(f"¡VICTORIA! {nombre} ha ganado la batalla!!!")

else:
  print(f"¡DERROTA!. Has caído en combate")