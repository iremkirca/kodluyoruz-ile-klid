#points adında bir liste oluşturduk
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

#euclideanDistance öklid hesaplayan bir fonksiyon
def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return distance

#distances adında boş bir liste oluşturduk
distances = []

#points listesinden pointler almalıyız
for point1 in points:
    for point2 in points:
        if point1 != point2:
            distance = euclideanDistance(point1, point2)
            distances.append(distance)

#aynı sonuçlar gelmesin diye listeyi sete çeviriyorum
new_distances = list(set(distances))

min_distance = min(new_distances)

print("All distances:", new_distances)
print("Min distance:", min_distance)