from geopy.distance import geodesic


def get_distance(start_point, end_point):
    return geodesic(
        f"{start_point}",
        f"{end_point}",
    ).kilometers


def get_inprint(distance, mass_kg):
    km_tons = distance * (mass_kg / 10 ** 6)
    return round(
        km_tons * (3.581 / 4) * 0.18 + km_tons * (1.603 / 10) * 0.46 + km_tons * 2.172
    )
