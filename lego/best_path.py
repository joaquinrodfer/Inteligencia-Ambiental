from road import Road

def get_neighbors(map):
    for row in map:
        for road in row:
            road.neighbors = []
            if 'U' in road.directions and road.coordinates[0] > 0:
                neighbor = map[road.coordinates[0] - 1][road.coordinates[1]]
                if neighbor.code != '00':
                    road.neighbors.append(neighbor)
            if 'D' in road.directions and road.coordinates[0] < 6:
                neighbor = map[road.coordinates[0] + 1][road.coordinates[1]]
                if neighbor.code != '00':
                    road.neighbors.append(neighbor)
            if 'L' in road.directions and road.coordinates[1] > 0:
                neighbor = map[road.coordinates[0]][road.coordinates[1] - 1]
                if neighbor.code != '00':
                    road.neighbors.append(neighbor)
            if 'R' in road.directions and road.coordinates[1] < 4:
                neighbor = map[road.coordinates[0]][road.coordinates[1] + 1]
                if neighbor.code != '00':
                    road.neighbors.append(neighbor)
    
    return road.neighbors

    