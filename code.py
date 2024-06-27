palabras_desconocidas = {
            "Bacano":"en Colombia, cuando algo es bacano, significa que es muy bueno y recomendable",
            "Melo": "estar bien",
            "Mecato": " se refiere a un refrigerio",
            "Fresco": "Estar relajado, tranquilo, sin preocupaciones",
            "Locha": "Hacer pereza o nada en particular",
            "Achantado":"Estar sin ánimo, triste o sin ganas de hacer cosas",
            }
print("hola bienvenido a el diccionario de colombia")  
for i in range(5):  
    word = input("Escribe  palabras que no entiendas con mayuscula inicial: ")
    if word in palabras_desconocidas.keys():
        print(palabras_desconocidas[word])
    else:
        print("esta palabra no se encuentra")
