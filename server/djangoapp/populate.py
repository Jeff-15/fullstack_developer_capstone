from .models import CarMake, CarModel

def initiate():
    car_make_data = [
        {"name":"NISSAN", "description":"Great cars. Japanese technology"},
        {"name":"Mercedes", "description":"Great cars. German technology"},
        {"name":"Audi", "description":"Great cars. German technology"},
        {"name":"Kia", "description":"Great cars. Korean technology"},
        {"name":"Toyota", "description":"Great cars. Japanese technology"},
    ]

    car_make_instances = []
    for data in car_make_data:
            car_make_instances.append(CarMake.objects.create(name=data['name'], description=data['description']))


    # Create CarModel instances with the corresponding CarMake instances
    car_model_data = [
      {"name":"Pathfinder", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[0]},
      {"name":"Qashqai", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[0]},
      {"name":"XTRAIL", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[0]},
      {"name":"A-Class", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[1]},
      {"name":"C-Class", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[1]},
      {"name":"E-Class", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[1]},
      {"name":"A4", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[2]},
      {"name":"A5", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[2]},
      {"name":"A6", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[2]},
      {"name":"Sorrento", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[3]},
      {"name":"Carnival", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[3]},
      {"name":"Cerato", "type":CarModel.SEDAN, "year": 2023, "make":car_make_instances[3]},
      {"name":"Corolla", "type":CarModel.SEDAN, "year": 2023, "make":car_make_instances[4]},
      {"name":"Camry", "type":CarModel.SEDAN, "year": 2023, "make":car_make_instances[4]},
      {"name":"Kluger", "type":CarModel.SUV, "year": 2023, "make":car_make_instances[4]},
        # Add more CarModel instances as needed
    ]

    for data in car_model_data:
            CarModel.objects.create(name=data['name'], make=data['make'], type=data['type'], year=data['year'])
