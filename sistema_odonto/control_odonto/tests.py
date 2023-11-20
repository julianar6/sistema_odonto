from django.test import TestCase

from control_odonto.models import Odontologo


class OdontologoTests(TestCase):
    """En esta clase van todas las pruebas del modelo Curso."""

    def test_creacion_odontologo(self):
        # caso uso esperado
        odontologo = Odontologo(nombre="julian", identidicacion=1036933588)
        odontologo.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Odontologo.objects.count(), 1)
        self.assertEqual(odontologo.nombre, "julian")
        self.assertEqual(odontologo.identidicacion, 1036933588 )

    def test_odontologo_str(self):
        odontologo = Odontologo(nombre="julian", identidicacion=39440890)
        odontologo.save()

        # Compruebo el str funciona como se desea
        self.assertEqual(odontologo.__str__(), "julian (39440890)")
