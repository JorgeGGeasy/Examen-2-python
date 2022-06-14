import csv


class Stop:

    def __init__(id, name, description, lat, lon):
        self.__id = id




def read_data(stops, data):
    datos = {}
    with open(stops, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            datos[row[1]] = {
                'description': row[3],
                'id': row[1],
                'lat': row[4],
                'lon': row[5],
                'name': row[2]
                }
            

    with open(data, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                datos[row[1]].keys()
                datos[row[1]]['lat'] = float(row[4])
                datos[row[1]]['lon'] = float(row[5])
            except:
                print()
    return datos

def get_name_description(datos, id):

    print("Para la clave " + str(id) + ":")
    print("---------------------------")
    try:
        print(datos[str(id)]["description"])
        print(datos[str(id)]["name"])
    except:
        print("Ha saltado error")

def search_by_lon(datos, longitud):
    
    print("Para la longitud " + str(longitud) + ":")
    print("---------------------------")

    if str(type(longitud)) != "<class 'float'>":
        print("Error de tipo")
        return

    for row in datos:
        if datos[row]["lon"] == longitud:
            print(row)
            return
    print("Error de clave")

def get_min(id, datos):
    lista = []
    print("Para el valor " + str(id) + ":")
    print("---------------------------")
    seguir = True

    while seguir:

        for row in datos:
            if float(row) <= float(id):
                lista.append({datos[str(row)]["description"], datos[str(row)]["name"]})
            else:
                seguir = False
    if len(lista) == 0:
        print("Ha saltado el error")
    print(lista)
        
if __name__ == "__main__":
    stops = 'stops.csv'
    data = 'stops_data.csv'
    datos = read_data(stops, data)
    get_name_description(datos, 1020)
    get_name_description(datos, 2020)
    search_by_lon(datos, 726668.229)
    search_by_lon(datos, 7.0)
    search_by_lon(datos, "hola")
    get_min(1023, datos)
    get_min(100, datos)
