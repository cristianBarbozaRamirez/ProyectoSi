import mysql.connector
from datetime import datetime
class ConsultasBD:
    def __init__(self, host, usuario, contraseña, base_datos):
        self.conexion = mysql.connector.connect(
            host=host,
            user=usuario,
            password=contraseña,
            database=base_datos
        )
        self.cursor = self.conexion.cursor()

    def agregar_gasto(self):

        # Solicita información sobre el gasto
        cantidad = float(input("Ingrese la cantidad gastada: "))
        descripcion = input("Ingrese una descripción del gasto: ")

        # Obtén la fecha y hora actual
        fecha_actual = datetime.now()

        # Formatea la fecha en "año-mes-día"
        fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

        # Inserta el gasto en la base de datos
        consulta = "INSERT INTO registros_gastos (cantidad, descripcion, fecha) VALUES (%s, %s, %s)"
        datos = (cantidad, descripcion, fecha_formateada)
        self.cursor.execute(consulta, datos)
        self.conexion.commit()
        print("Gasto agregado con éxito.")


    def obtener_resultados_por_dia(self):
        dias=["","domingos","lunes","martes","miercoles","jueves","viernes","sabados"]
        for i in range(1,len(dias)):

            consulta = "SELECT * FROM registros_gastos WHERE DAYOFWEEK(fecha) = %s"
            self.cursor.execute(consulta, (i,))
            resultados = self.cursor.fetchall()
            print(f"\nHistorial de Gastos de los {dias[i]}")
            if resultados:
                
                print("{:<5} {:<15} {:<20} {:<15}".format("ID", "Cantidad", "Descripción", "Fecha"))

                for i, resultado in enumerate(resultados):
                    fecha_formateada = resultado[3].strftime("%Y-%m-%d")
                    print("{:<5} {:<15} {:<20} {:<15}".format(resultado[0], resultado[1], resultado[2], fecha_formateada))

                    if i < len(resultados) - 1 and resultado[3] != resultados[i + 1][3]:
                        print("----------------")
            else:
                print("\nNo hay gastos registrados.")
    


    def suma_por_fecha(self):
        print("-----------------")
        fecha =input("Ingrese la fecha para obtener el gasto total de ese dia:")
        consulta = "SELECT SUM(cantidad) FROM registros_gastos WHERE fecha = %s"
        self.cursor.execute(consulta, (fecha,))
        suma = self.cursor.fetchone()
        if suma[0] is not None:
                print(f"El gasto total para la fecha {fecha} es: {suma[0]:.2f}")
        else:
             print(f"No hay registros para la fecha {fecha}.")

    def suma_total_gastos(self):
        pass
        consulta_primera_fila = "SELECT fecha FROM registros_gastos ORDER BY id ASC LIMIT 1"
        consulta_ultima_fila = "SELECT fecha FROM registros_gastos ORDER BY id DESC LIMIT 1"
        self.cursor.execute(consulta_primera_fila)
        ob_fecha_inicio = self.cursor.fetchone()

        self.cursor.execute(consulta_ultima_fila)
        ob_fecha_fin = self.cursor.fetchone()

        fecha_inicio = ob_fecha_inicio[0].strftime("%Y-%m-%d")
        fecha_fin = ob_fecha_fin[0].strftime("%Y-%m-%d")
        print(f" {fecha_inicio} - {fecha_fin}")
        consulta_suma = "SELECT SUM(cantidad) FROM registros_gastos"
        self.cursor.execute(consulta_suma)
        suma_total = self.cursor.fetchone()
# Imprime el resultado
        if suma_total[0] is not None:
            print(f"La suma total de la columna 'cantidad' es: {suma_total[0]:.2f}")
        else:
            print("La tabla está vacía.")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()