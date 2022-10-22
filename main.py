from geopy.distance import geodesic
from db import db_cursor
from distance_calculation import get_distance
from flask import Flask
import folium
from distance_calculation import get_inprint


def get_coordinates_by_port_name(port_name):
    return db_cursor.execute(
        """
        SELECT latitude, longitude 
        FROM seaport 
        WHERE name = ?
        """,
        [port_name],
    ).fetchall()[0]


def port_coordinate_formatting(coordinates):
    return str(coordinates[0]) + ", " + str(coordinates[1])


mass = int(input("Введите массу коробля в килограммах: "))
print("Пример: Имеретинский морской порт")
start_port = input("Введите порт отправления: ")
print("Пример: Морской Торговый Порт Советская Гавань")
end_port = input("Введите порт прибытия: ")

coordinates_start_port = get_coordinates_by_port_name(start_port)
coordinates_end_port = get_coordinates_by_port_name(end_port)

coordinates_start_port = port_coordinate_formatting(coordinates_start_port)
coordinates_end_port = port_coordinate_formatting(coordinates_end_port)

distance_km = get_distance(coordinates_start_port, coordinates_end_port)

CO2 = get_inprint(distance_km, mass)

print(
    f"Координаты отправления: {coordinates_start_port}",
    f"Координты прибытия: {coordinates_end_port}",
    sep="\n",
)

print(f"Расстояние {start_port} - {end_port} составляет: {distance_km:.2f} км")

print("Углеродный след составляет:", CO2, "килограмм")
