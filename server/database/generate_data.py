"""Generate sample dealership and review data for the Best Cars Dealership API.

Run from server/database:  python generate_data.py
Writes data/dealerships.json (50 dealers) and data/reviews.json.
The output is deterministic, so re-running it gives identical files.
"""
import json
import os
import random

# (city, state, state code, latitude, longitude)
CITIES = [
    ("Topeka", "Kansas", "KS", 39.05, -95.68),
    ("Wichita", "Kansas", "KS", 37.69, -97.34),
    ("Kansas City", "Kansas", "KS", 39.11, -94.63),
    ("Overland Park", "Kansas", "KS", 38.98, -94.67),
    ("Lawrence", "Kansas", "KS", 38.97, -95.24),
    ("Denver", "Colorado", "CO", 39.74, -104.99),
    ("Colorado Springs", "Colorado", "CO", 38.83, -104.82),
    ("Dallas", "Texas", "TX", 32.78, -96.80),
    ("Houston", "Texas", "TX", 29.76, -95.37),
    ("Austin", "Texas", "TX", 30.27, -97.74),
    ("San Antonio", "Texas", "TX", 29.42, -98.49),
    ("Oklahoma City", "Oklahoma", "OK", 35.47, -97.52),
    ("Tulsa", "Oklahoma", "OK", 36.15, -95.99),
    ("Omaha", "Nebraska", "NE", 41.26, -95.93),
    ("Lincoln", "Nebraska", "NE", 40.81, -96.70),
    ("Kansas City", "Missouri", "MO", 39.10, -94.58),
    ("St. Louis", "Missouri", "MO", 38.63, -90.20),
    ("Chicago", "Illinois", "IL", 41.88, -87.63),
    ("Springfield", "Illinois", "IL", 39.78, -89.65),
    ("Indianapolis", "Indiana", "IN", 39.77, -86.16),
    ("Columbus", "Ohio", "OH", 39.96, -83.00),
    ("Cleveland", "Ohio", "OH", 41.50, -81.69),
    ("Detroit", "Michigan", "MI", 42.33, -83.05),
    ("Minneapolis", "Minnesota", "MN", 44.98, -93.27),
    ("Milwaukee", "Wisconsin", "WI", 43.04, -87.91),
    ("Des Moines", "Iowa", "IA", 41.59, -93.62),
    ("Nashville", "Tennessee", "TN", 36.16, -86.78),
    ("Memphis", "Tennessee", "TN", 35.15, -90.05),
    ("Atlanta", "Georgia", "GA", 33.75, -84.39),
    ("Miami", "Florida", "FL", 25.76, -80.19),
    ("Orlando", "Florida", "FL", 28.54, -81.38),
    ("Charlotte", "North Carolina", "NC", 35.23, -80.84),
    ("Richmond", "Virginia", "VA", 37.54, -77.44),
    ("Philadelphia", "Pennsylvania", "PA", 39.95, -75.17),
    ("Pittsburgh", "Pennsylvania", "PA", 40.44, -79.99),
    ("New York", "New York", "NY", 40.71, -74.01),
    ("Boston", "Massachusetts", "MA", 42.36, -71.06),
    ("Phoenix", "Arizona", "AZ", 33.45, -112.07),
    ("Las Vegas", "Nevada", "NV", 36.17, -115.14),
    ("Salt Lake City", "Utah", "UT", 40.76, -111.89),
    ("Albuquerque", "New Mexico", "NM", 35.08, -106.65),
    ("Los Angeles", "California", "CA", 34.05, -118.24),
    ("San Diego", "California", "CA", 32.72, -117.16),
    ("San Francisco", "California", "CA", 37.77, -122.42),
    ("Sacramento", "California", "CA", 38.58, -121.49),
    ("Portland", "Oregon", "OR", 45.52, -122.68),
    ("Seattle", "Washington", "WA", 47.61, -122.33),
    ("Boise", "Idaho", "ID", 43.62, -116.20),
    ("Louisville", "Kentucky", "KY", 38.25, -85.76),
    ("New Orleans", "Louisiana", "LA", 29.95, -90.07),
]

SUFFIXES = ["Motors", "Auto Center", "Car World", "Auto Group", "Automotive"]
STREETS = ["Main Street", "Central Avenue", "Market Street", "Commerce Street",
           "Oak Boulevard", "Highway 40", "Lakeview Drive", "Broadway"]

FIRST_NAMES = ["Aisha", "Ben", "Carlos", "Dana", "Elena", "Frank", "Grace", "Hiro",
               "Isla", "Jamal", "Kavya", "Liam", "Maya", "Noah", "Olivia", "Pedro"]
LAST_NAMES = ["Anderson", "Brooks", "Chen", "Diaz", "Evans", "Foster", "Gupta", "Hughes",
              "Ito", "Johnson", "Khan", "Lopez", "Miller", "Nguyen", "Owens", "Patel"]

CARS = [
    ("Nissan", "Pathfinder"), ("Nissan", "Qashqai"), ("Mercedes", "C-Class"),
    ("Audi", "A4"), ("Kia", "Sorrento"), ("Toyota", "Camry"), ("Toyota", "Corolla"),
]

POSITIVE = [
    "Fantastic service! The staff were friendly and helped me find the right car.",
    "Great experience from start to finish. The price was fair and there was no pressure.",
    "Excellent dealership. My car was ready on time and everything was explained clearly.",
    "Wonderful team and a very clean showroom. I would happily buy here again.",
]
NEUTRAL = [
    "The process was fine. Paperwork took a while but the car matches the listing.",
    "Average visit. The salesperson was polite and the car was as described.",
]
NEGATIVE = [
    "Disappointing. The wait was long and the follow-up after the sale was poor.",
    "Not a great experience. The final price was higher than the one quoted.",
]


def build_dealers():
    random.seed(2026)
    dealers = []
    for i, (city, state, st, lat, lng) in enumerate(CITIES, start=1):
        short = f"{city} {SUFFIXES[i % len(SUFFIXES)].split()[0]}"
        dealers.append({
            "id": i,
            "city": city,
            "state": state,
            "st": st,
            "address": f"{random.randint(100, 9900)} {random.choice(STREETS)}",
            "zip": f"{random.randint(10000, 99999)}",
            "lat": str(lat),
            "long": str(lng),
            "short_name": short,
            "full_name": f"{city} {SUFFIXES[i % len(SUFFIXES)]}",
        })
    return dealers


def build_reviews(dealers):
    random.seed(7)
    reviews = []
    review_id = 1
    for dealer in dealers:
        for _ in range(random.randint(2, 4)):
            make, model = random.choice(CARS)
            text = random.choice(POSITIVE * 3 + NEUTRAL + NEGATIVE)
            month, day = random.randint(1, 12), random.randint(1, 28)
            year = random.randint(2021, 2025)
            reviews.append({
                "id": review_id,
                "name": f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}",
                "dealership": dealer["id"],
                "review": text,
                "purchase": True,
                "purchase_date": f"{month:02d}/{day:02d}/{year}",
                "car_make": make,
                "car_model": model,
                "car_year": random.randint(2019, 2025),
            })
            review_id += 1
    return reviews


def main():
    dealers = build_dealers()
    assert len(dealers) == 50, "expected exactly 50 dealers"
    reviews = build_reviews(dealers)
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "dealerships.json"), "w", encoding="utf-8") as f:
        json.dump({"dealerships": dealers}, f, indent=2)
    with open(os.path.join(out_dir, "reviews.json"), "w", encoding="utf-8") as f:
        json.dump({"reviews": reviews}, f, indent=2)
    print(f"Wrote {len(dealers)} dealers and {len(reviews)} reviews")


if __name__ == "__main__":
    main()
