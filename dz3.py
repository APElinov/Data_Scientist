len_mkad_km = 109
speed = int(input("С какой скоростью едет машина? "))
time = int(input("Сколько часов машина уже едет? "))
km_in_time = (time * speed) % len_mkad_km
print("Машина сейчас на %d км. по МКАД." %km_in_time)