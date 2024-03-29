from data import people, plants_list, plants_dict

if all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grasses in this pack")

if any(plant.plant_type == "Cactus" for plant in plants_dict.values()):
    print("This pack contains cactii")
else:
    print("No cactii in this dict")
