
# Mensaje de bienvenida
print("Bienvenido al programa de información de integrantes de grupo")
    
#Preguntar al usuario si desea ejecutar el programa
while True:
    
        respuesta = input("¿Desea ejecutar el programa? (si/no): ")
        if respuesta.lower() == "si":
            print("INICIO DEL PROGRAMA")
    
            #Mostrar el menú de integrantes
            print("Seleccione un integrante del grupo: ")
            lisT = [1,2,3,4,5,6]
            integrantes = ["Alicia", "Ana", "Juan", "Jonathan", "Mauricio", "Nestor"]
            for l1, l2 in zip(lisT,integrantes):
                print(l1,l2)   
                    #Pedir al usuario que ingrese el nombre del integrante
            intentos = 4
            while intentos > 0:
                seleccion = input("Ingrese el nombre del integrante: ").upper()
                if seleccion == "Alicia".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"--- Información de {seleccion} ---")
                    print("Nombres: Alicia Estefany ")
                    print("Apellidos: Gúzman López")
                    print("Sexo: Femenino")
                    print("Edad: 17")
                    print("Departamento: Chalatenango")
                    print("Municipio: El Paraiso")
                    print("Dirección: La Angostura")
                elif seleccion == "Ana".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"--- Información de {seleccion} ---")
                    print("Nombres: Ana Yancy ")
                    print("Apellidos: Azúcar Mejía")
                    print("Sexo: Femenino")
                    print("Edad: 18")
                    print("Departamento: Chalatenango")
                    print("Municipio: El Paraiso")
                    print("Dirección: Roble 1")
                elif seleccion == "Juan".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"--- Información de {seleccion} ---")
                    print("Nombres: Juan Elias ")
                    print("Apellidos: Alas Artiga")
                    print("Sexo: Masculino")
                    print("Edad: 19")
                    print("Departamento: Cuscatlan")
                    print("Municipio: Suchitoto")
                    print("Dirección: Avenida 5 noviembre")
                elif seleccion == "Jonathan".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"--- Información de {seleccion} ---")
                    print("Nombres: Jonathan Alexander ")
                    print("Apellidos: Tejada Jiménez")
                    print("Sexo: Masculino")
                    print("Edad: 20")
                    print("Departamento: San Salvador")
                    print("Municipio: El Paisnal")
                    print("Dirección: Barrio San Jose")
                elif seleccion == "Mauricio".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"--- Información de {seleccion} ---")
                    print("Nombres: Mauricio Orlando ")
                    print("Apellidos: Vaquero Alas")
                    print("Sexo: Masculino")
                    print("Edad: 22")
                    print("Departamento: San Salvador")
                    print("Municipio: El Paisnal")
                    print("Dirección: Caserío El Capulín Av. Aguilares El Paisnal")
                elif seleccion == "Nestor".upper():
                    #Mostrar información del integrante seleccionado
                    print(f"--- Información de {seleccion} ---")
                    print("Nombres: Nestor Eduardo ")
                    print("Apellidos: Gomez Franco")
                    print("Sexo: Masculino")
                    print("Edad: 18")
                    print("Departamento: Chalatenango")
                    print("Municipio: Chalatenango")
                    print("Dirección: Reubicación 3")
                else:
                    intentos -= 1
                    if intentos > 0:
                        print(f"Nombre no encontrado. Le quedan {intentos} intentos.")
                        continue
                    else:
                        print("Número máximo de intentos finalizados.")
                            
                            #Preguntar si desea consultar otro dato
                
                respuesta = input("¿Desea consultar los datos de otro integrante? (si/no): ")
                if respuesta.lower() == "si":
                    continue
                elif respuesta.lower() == "no":
                    print("Programa finalizado.")
                    break
                else:
                    print("Dato invalido")    
                print("Fin del programa")
                break   
        else:            
            print("Fin del programa")
        break