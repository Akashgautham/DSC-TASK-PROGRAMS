def cartons_size(bottles):
    carton_sizes = {'xl': 48,'large': 24,'medium': 12,'small': 6}
    cartons_used = {'xl': 0,'large': 0,'medium': 0,'small': 0}
    for carton, capacity in carton_sizes.items():
        if bottles >= capacity:
            cartons_used[carton] = bottles // capacity  
            bottles = bottles % capacity  
    cartons_number = []
    for carton in ['xl', 'large', 'medium', 'small']:
        if cartons_used[carton] > 0:
            cartons_number.append(f"{cartons_used[carton]} {carton}")
    
    print(', '.join(cartons_number))
bottles=int(input("enter the number of bottles:"))
cartons_size(bottles)
