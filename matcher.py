import math

def calculate_distance(point1, point2):

    lat1, lon1 = point1
    lat2, lon2 = point2

    R = 6371.0 
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2)**2 + \
        math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

def find_nearest_neighbor(array1, array2):
   
    results = []
    for p1 in array1:
        closest_point = None
        min_dist = float('inf') 
        
        for p2 in array2:
            dist = calculate_distance(p1, p2)
            if dist < min_dist:
                min_dist = dist
                closest_point = p2
        
        results.append({
            "target": p1,
            "matched_to": closest_point,
            "distance_km": round(min_dist, 2)
        })
    return results
