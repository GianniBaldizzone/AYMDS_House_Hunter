
import sqlite3


class Conexion:

  def __init__(self, nombreBD):
    self.conexion = sqlite3.connect(nombreBD)
    self.cursor = self.conexion.cursor()

  def CrearTablaHabitacion(self):
    self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS HABITACION(
      id INTEGER PRIMARY KEY,
      numero INT,
      precio FLOAT,
      piso INT,
      estado_de_limpieza TEXT,
      capacidad_actual INT,
      capacidad_maxima INT,
      tipo_de_habitacion TEXT
      )
    ''')
    self.conexion.commit()

  def IngresarHabitacion(self, numero, precio, piso,capacidadMaxima, tipoDeHabitacion):
    self.cursor.execute(
      "INSERT INTO HABITACION (numero, precio, piso, estado_de_limpieza, capacidad_actual, capacidad_maxima, tipo_de_habitacion) VALUES (?, ?, ?,'Limpio', 0, ?, ?)",
      (numero, precio, piso, capacidadMaxima, tipoDeHabitacion))
    self.conexion.commit()
    print("Habitacion creada con exito!!!")

  def MostrarHabitaciones(self):
    self.cursor.execute("SELECT *FROM HABITACION")
    habitaciones = self.cursor.fetchall()
    return habitaciones

  def ModificarHabitacion(self, nombre, apellido, dni, id):
    self.cursor.execute(
        " UPDATE CLIENTE SET nombre=?,apellido=?,dni=? WHERE id = ? ",
        (nombre, apellido, dni, id))
    self.conexion.commit()

  def ModificarEliminar(self, id):
    self.cursor.execute(" DELETE FROM HABITACION WHERE id = ?", (id))
    self.conexion.commit()

  def CerrarBD(self):
    self.conexion.close()
    self.cursor.close()