from matcher import find_nearest_neighbor

list_a = [(31.2304, 121.4737), (39.9042, 116.4074)] 
list_b = [(31.2222, 121.4581), (34.2658, 108.9422), (39.9165, 116.3972)] 

results = find_nearest_neighbor(list_a, list_b)

for r in results:
    print(f"Original array {r['target']} matched {r['matched_to']}，distance is {r['distance_km']} km")
