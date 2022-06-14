import csv

def read_data(stops, data):
    datos = {}
    with open(stops, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            datos[row[1]] = {
                'description': row[3],
                'id': row[1],
                'lat': row[4],
                'long': row[5],
                'name': row[2]
                }
            

    with open(data, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            try:
                datos[row[1]].keys()
                datos[row[1]]['lat'] = row[4]
                datos[row[1]]['long'] = row[5]
            except:
                print()
    return datos

def get_name_description(datos, id):

    print("Para la clave " + str(id) + " :")
    print("---------------------------")
    try:
        print(datos[str(id)]["description"])
        print(datos[str(id)]["name"])
    except:
        print("Ha saltado error")

def search_by_lon(datos, longitud):

    print(str(type(longitud)))
    if str(type(longitud)) == "<class 'float'>":
        print("pillada")
    """
    print("Para la clave " + str(id) + " :")
    print("---------------------------")
    try:
        print(datos[str(id)]["description"])
        print(datos[str(id)]["name"])
    except:
        print("Ha saltado error")
        """
        
if __name__ == "__main__":
    stops = 'stops.csv'
    data = 'stops_data.csv'
    datos = read_data(stops, data)
    get_name_description(datos, 1020)
    get_name_description(datos, 2020)
    search_by_lon(datos, 726668.229)
    search_by_lon(datos, 7.0)
    search_by_lon(datos, "hola")
