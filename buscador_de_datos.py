import unittest

def buscar_datos(*args, **kwargs):
    arg_set = set(args)
    listado_personas = []

    for persona, datos in kwargs.items(): 
        datos_set = set(datos.values())

        if arg_set.issubset(datos_set): 
            listado_personas.append(persona)

    if listado_personas:
        return listado_personas                
    
    else:
        return "La persona que se está buscando no se encuentran dentro de la base de datos"

database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Lionel",
        "segundo_nombre": "Andres",
        "primer_apellido": "Messi",
        "segundo_apellido": "Cuccittini"
    },
    "persona3": {
        "primer_nombre": "Santiago",
        "segundo_nombre": "Daniel",
        "primer_apellido": "Baron",
        "segundo_apellido": "Reyes"
    },
    "persona4": {
        "primer_nombre": "Lionel",
        "segundo_nombre": "Sebastian",
        "primer_apellido": "Scaloni",
        "segundo_apellido": "Fernandez"
    },               
}

class TestInDatabase(unittest.TestCase):

    def test_persona1(self):
        resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
        self.assertEqual(resultado, ["persona1"])
    
    def test_persona2(self):
        resultado = buscar_datos("Lionel", "Andres", "Messi", "Cuccittini", **database)
        self.assertEqual(resultado, ["persona2"])
    
    def test_persona3(self):
        resultado = buscar_datos("Santiago", "Daniel","Baron","Reyes", **database)
        self.assertEqual(resultado, ["persona3"])
    
    def test_persona4(self):
        resultado = buscar_datos("Lionel", "Sebastian", "Scaloni", "Fernandez", **database)
        self.assertEqual(resultado, ["persona4"])
    
    def test_personas_iguales(self):
        resultado = buscar_datos("Lionel", **database)
        self.assertEqual(resultado, ["persona2","persona4"])

    def  test_datos_mezclados(self):      
        resultado = buscar_datos("Ruiz", "Pablo", "Picasso", "Diego", **database)
        self.assertEqual(resultado, ["persona1"])

    def  test_persona_no_existe(self):      
        resultado = buscar_datos("Ignacio", "Julian", "Soria", "Lopez", **database)
        self.assertEqual(resultado, "La persona que se está buscando no se encuentran dentro de la base de datos")

unittest.main()