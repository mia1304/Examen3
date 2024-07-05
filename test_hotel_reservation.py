import unittest
from hotel_reservation import HotelReservation

class TestHotelReservation(unittest.TestCase):

    def setUp(self):
        self.hotel = HotelReservation()

    # Pruebas de Equivalencia de Clases
    def test_check_availability_valid(self):
        # Prueba de clase de equivalencia válida (1-10)
        self.assertTrue(self.hotel.check_availability(5))

    def test_check_availability_invalid_low(self):
        # Prueba de clase de equivalencia inválida (<1)
        with self.assertRaises(ValueError):
            self.hotel.check_availability(0)

    def test_check_availability_invalid_high(self):
        # Prueba de clase de equivalencia inválida (>10)
        with self.assertRaises(ValueError):
            self.hotel.check_availability(11)

    # Análisis de Valores Límite
    def test_check_availability_boundary_low(self):
        # Prueba de límite inferior (1)
        self.assertTrue(self.hotel.check_availability(1))

    def test_check_availability_boundary_high(self):
        # Prueba de límite superior (10)
        self.assertTrue(self.hotel.check_availability(10))

    # Pruebas de Tabla de Decisión
    def test_book_room_available_valid(self):
        # Prueba con habitación disponible y número válido
        self.assertEqual(self.hotel.book_room(1), "Hab. 1 reservada con éxito.")
        self.assertFalse(self.hotel.check_availability(1))

    def test_book_room_unavailable_valid(self):
        # Prueba con habitación no disponible y número válido
        self.hotel.book_room(1)
        self.assertEqual(self.hotel.book_room(1), "La hab. 1 ya está reservada.")

    def test_book_room_invalid(self):
        # Prueba con número de habitación inválido
        with self.assertRaises(ValueError):
            self.hotel.book_room(0)

    # Pruebas de Transición de Estado
    def test_state_transition_book_and_cancel(self):
        # Prueba de transición de estado: reservar y cancelar
        self.hotel.book_room(1)
        self.assertEqual(self.hotel.cancel_booking(1), "Reserva de la hab. 1 cancelada.")
        self.assertTrue(self.hotel.check_availability(1))

if __name__ == "__main__":
    unittest.main()
