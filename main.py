from consultas import *

def main():
    consulta = ConsultasBD("localhost","root","xymn2232","gastos")
    consulta.obtener_resultados_por_dia()
    while True:
        print("\n=== Menú Gastos Personales ===")
        print("1. Agregar Gasto")
        print("2. contar gastos")
        print("3. Salir")
        
        opcion = input("Seleccione una opcion (1-3):")
        if opcion == "1":
            consulta.agregar_gasto() 
        elif opcion == "2":
            opcion2 = input("Como desea calcular los gastos(fecha/total):")
            if opcion2 == "fecha":
                consulta.suma_por_fecha()
            elif opcion2 == "total":
                consulta.suma_total_gastos()
            else:
                print("Opción no válida. Por favor, ingrese una opción válida (fecha/total).")


        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingrese una opción válida (1-3).")
    



main()