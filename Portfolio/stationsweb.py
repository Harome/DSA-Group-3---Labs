class Graph:
    def __init__(self):
        self.nodes = {}

    def add_station(self, station, category):
        if station not in self.nodes:
            self.nodes[station] = {'category': category, 'connections': {}}

    def add_connection(self, station1, station2, weight=1):
        if station1 in self.nodes and station2 in self.nodes:
            self.nodes[station1]['connections'][station2] = weight
            self.nodes[station2]['connections'][station1] = weight

    def get_category(self, station):
        return self.nodes[station]['category']

    def shortest_path(self, start, end):
        return self._shortest_path(start, end, set())

    def _shortest_path(self, start, end, visited):
        if start not in self.nodes or end not in self.nodes:
            return float('inf'), []

        if start == end:
            return 0, [start]

        if start in visited:
            return float('inf'), []

        visited.add(start)
        min_distance = float('inf')
        min_path = []

        for neighbor, weight in self.nodes[start]['connections'].items():
            distance, path = self._shortest_path(neighbor, end, visited.copy())
            distance += weight

            if distance < min_distance:
                min_distance = distance
                min_path = [start] + path

        visited.remove(start)
        return min_distance, min_path
    
    def display_stations(self):
        lrt1_stations_str = "LRT-1 Stations:\n" + ", ".join(lrt1_stations)
        lrt2_stations_str = "LRT-2 Stations:\n" + ", ".join(lrt2_stations)
        mrt3_stations_str = "MRT-3 Stations:\n" + ", ".join(mrt3_stations)

        return f"{lrt1_stations_str}\n<br><br>\n{lrt2_stations_str}\n<br><br>\n{mrt3_stations_str}"

# Create a graph for MRT lines
mrt_graph = Graph()

lrt1_stations = [
    "Baclaran", "Edsa", "Libertad", "Gil Puyat", "Vito Cruz", "Quirino Avenue",
    "Pedro Gil", "UN Avenue", "Central Terminal", "Carriedo", "Doroteo Jose",
    "Bambang", "Tayuman", "Blumentritt", "Abad Santos", "R. Papa", "5th Avenue",
    "Monumento", "Balintawak", "Roosevelt"
]

for station in lrt1_stations:
    mrt_graph.add_station(station, 'LRT-1')

lrt2_stations = [
    "Recto", "Legarda", "Pureza", "V. Mapa", "J. Ruiz", "Gilmore",
    "Betty Go-Belmonte", "Araneta Center-Cubao:LRT-2", "Anonas", "Katipunan", "Santolan"
]

for station in lrt2_stations:
    mrt_graph.add_station(station, 'LRT-2')

mrt3_stations = [
    "North Avenue", "Quezon Avenue", "GMA-Kamuning", "Araneta Center-Cubao:MRT-3",
    "Santolan-Annapolis", "Ortigas Avenue", "Shaw Boulevard", "Boni Avenue",
    "Guadalupe", "Buendia", "Ayala", "Magallanes", "Taft Avenue"
]

for station in mrt3_stations:
    mrt_graph.add_station(station, 'MRT-3')

lrt1_connections = [
    ("Baclaran", "Edsa"), ("Edsa", "Libertad"), ("Libertad", "Gil Puyat"),
    ("Gil Puyat", "Vito Cruz"), ("Vito Cruz", "Quirino Avenue"),
    ("Quirino Avenue", "Pedro Gil"), ("Pedro Gil", "UN Avenue"),
    ("UN Avenue", "Central Terminal"), ("Central Terminal", "Carriedo"),
    ("Carriedo", "Doroteo Jose"), ("Doroteo Jose", "Bambang"),
    ("Bambang", "Tayuman"), ("Tayuman", "Blumentritt"), ("Blumentritt", "Abad Santos"),
    ("Abad Santos", "R. Papa"), ("R. Papa", "5th Avenue"), ("5th Avenue", "Monumento"),
    ("Monumento", "Balintawak"), ("Balintawak", "Roosevelt")
]

lrt2_connections = [
    ("Recto", "Legarda"), ("Legarda", "Pureza"), ("Pureza", "V. Mapa"),
    ("V. Mapa", "J. Ruiz"), ("J. Ruiz", "Gilmore"), ("Gilmore", "Betty Go-Belmonte"),
    ("Betty Go-Belmonte", "Araneta Center-Cubao:LRT-2"), ("Araneta Center-Cubao:LRT-2", "Anonas"),
    ("Anonas", "Katipunan"), ("Katipunan", "Santolan")
]

mrt3_connections = [
    ("North Avenue", "Quezon Avenue"), ("Quezon Avenue", "GMA-Kamuning"),
    ("GMA-Kamuning", "Araneta Center-Cubao:MRT-3"), ("Araneta Center-Cubao:MRT-3", "Santolan-Annapolis"),
    ("Santolan-Annapolis", "Ortigas Avenue"), ("Ortigas Avenue", "Shaw Boulevard"),
    ("Shaw Boulevard", "Boni Avenue"), ("Boni Avenue", "Guadalupe"),
    ("Guadalupe", "Buendia"), ("Buendia", "Ayala"), ("Ayala", "Magallanes"),
    ("Magallanes", "Taft Avenue")
]

mrt_graph.add_connection("Doroteo Jose", "Recto", weight=1)  
mrt_graph.add_connection("Araneta Center-Cubao:LRT-2", "Araneta Center-Cubao:MRT-3", weight=1) 

for connection in lrt1_connections + lrt2_connections + mrt3_connections:
    mrt_graph.add_connection(connection[0], connection[1])

