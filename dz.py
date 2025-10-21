temperature = input("Температура выше 20 градусов и меньше 30? (да/нет): ")

if temperature == "да":
    is_rainy = input("Есть осадки? (да/нет): ")
    
    if is_rainy == "да":
        print("Футболку, шорты и дождевик")
    else:
        print("Футболку и шорты")
        
else:
    temperature = input("Температура выше 0? (да/нет): ")
    
    if temperature == "нет":
        print("Пуховик")
    else:
        is_rainy = input("Есть осадки? (да/нет): ")
        
        if is_rainy == "да":
            is_raining_heavily = input("Осадки сильные? (да/нет): ")
            
            if is_raining_heavily == "да":
                print("Пальто, резиновые сапоги и зонт")
            else:
                print("Пальто и дождевик")
        else:
            print("Пальто")