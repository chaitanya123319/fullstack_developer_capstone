from .models import CarMake, CarModel

CARS = {
    "Nissan": ("Japan", "Reliable cars with Japanese engineering.", [
        ("Pathfinder", "SUV", 2023), ("Qashqai", "SUV", 2023), ("X-Trail", "SUV", 2023)]),
    "Mercedes": ("Germany", "Luxury cars with German engineering.", [
        ("A-Class", "Sedan", 2023), ("C-Class", "Sedan", 2023), ("E-Class", "Sedan", 2023)]),
    "Audi": ("Germany", "Premium cars with advanced technology.", [
        ("A4", "Sedan", 2023), ("A5", "Sedan", 2023), ("A6", "Wagon", 2023)]),
    "Kia": ("South Korea", "Affordable, well-equipped family cars.", [
        ("Sorento", "SUV", 2023), ("Carnival", "Wagon", 2023), ("Cerato", "Sedan", 2023)]),
    "Toyota": ("Japan", "Dependable cars known for long life.", [
        ("Corolla", "Sedan", 2023), ("Camry", "Sedan", 2023), ("Kluger", "SUV", 2023)]),
}


def initiate():
    """Create the sample car makes and models. Safe to call more than once."""
    for make_name, (country, description, models) in CARS.items():
        make, _ = CarMake.objects.get_or_create(
            name=make_name,
            defaults={"country": country, "description": description},
        )
        for model_name, car_type, year in models:
            CarModel.objects.get_or_create(
                car_make=make,
                name=model_name,
                defaults={"type": car_type, "year": year},
            )
