import unittest
import subprocess
import sys
from main import saludo, submensaje

class TestMain(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo(), "hola")

    def test_submensaje(self):
        self.assertEqual(submensaje(), "bb")

    def test_ejecucion_script(self):
        resultado = subprocess.run(
            [sys.executable, "main.py"],
            capture_output=True,
            text=True,
            check=True
        )
        salida = [linea.strip() for linea in resultado.stdout.strip().splitlines() if linea.strip()]
        self.assertEqual(salida, ["hola", "bb"])

if __name__ == "__main__":
    unittest.main()
