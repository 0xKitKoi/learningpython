place_1, place_2, place_3, place_4, place_5, place_6, place_7, place_8 = 0, 0, 0, 0, 0, 0, 0, 0

while True:
    place_1 += 1
    
    if place_1 == 2:
        place_1 = 0
        place_2 += 1
    if place_2 == 2:
        place_2 = 0
        place_3 += 1
    if place_3 == 2:
        place_3 = 0
        place_4 += 1
    if place_4 == 2:
        place_4 = 0
        place_5 += 1
    if place_5 == 2:
        place_5 = 0
        place_6 += 1
    if place_6 == 2:
        place_6 = 0
        place_7 += 1
    if place_7 == 2:
        place_7 = 0
        place_8 += 1
    if place_8 == 2:
        place_8 = 1
        break

    print(f"{place_8} {place_7} {place_6} {place_5} {place_4} {place_3} {place_2} {place_1}")

