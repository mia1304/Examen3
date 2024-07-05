class HotelReservation:
    def __init__(self):
        self.rooms = [True] * 10  # 10 habitaciones, True significa disponible

    def check_availability(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            return self.rooms[room_number - 1]
        else:
            raise ValueError("Número de habitación inválido")

    def book_room(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            if self.rooms[room_number - 1]:
                self.rooms[room_number - 1] = False
                return f"Hab. {room_number} reservada con éxito."
            else:
                return f"La hab. {room_number} ya está reservada."
        else:
            raise ValueError("Número de habitación inválido")

    def cancel_booking(self, room_number):
        if 1 <= room_number <= len(self.rooms):
            if not self.rooms[room_number - 1]:
                self.rooms[room_number - 1] = True
                return f"Reserva de la hab. {room_number} cancelada."
            else:
                return f"La hab. {room_number} no estaba reservada."
        else:
            raise ValueError("Número de habitación inválido")
