class Reserva:
    def __init__(self, id: int, empleado: Empleado, fechaChekin: Date, fechaCheckout: Date,
                 habitacion: Habitacion, estado: str, huesped: Huesped, tipoReserva: TipoReserva):
        self.id = id
        self.empleado = empleado
        self.fechaChekin = fechaChekin
        self.fechaCheckout = fechaCheckout
        self.habitacion = habitacion
        self.estado = estado
        self.huesped = huesped
        self.tipoReserva = tipoReserva