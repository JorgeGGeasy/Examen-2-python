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
            datos[row[1]] = {
                'lat': row[4],
                'long': row[5],
                }
            print(row[1])
            print(row[2])
            print(row[3])
            print(row[4])
            print(datos)

            


    return 

if __name__ == "__main__":
    stops = 'stops.csv'
    data = 'stops_data.csv'
    read_data(stops, data)