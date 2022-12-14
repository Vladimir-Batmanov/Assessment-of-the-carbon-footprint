import sqlite3

db_connect = sqlite3.connect("server.db")

db_cursor = db_connect.cursor()

db_cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS seaport (
    name TEXT, 
    latitude INTEGER, 
    longitude INTEGER)
    """
)

db_cursor.execute(
    """
    INSERT INTO seaport (name, latitude, longitude) 
    VALUES ("порт Сухум", 42.996360, 41.021638),
    ("Морской вокзал", 43.580713, 39.710392),
    ("Поти", 42.155735, 41.653508),
    ("Морской вокзал Сочи", 43.580764, 39.718618),
    ("Батумский морской порт", 41.652155, 41.643801),
    ("порт Очамчыра", 42.743205, 41.427058),
    ("Имеретинский морской порт", 43.413337, 39.931460),
    ("порт Фароз", 41.010800, 39.705257),
    ("Батумский морской порт", 41.646575, 41.650570),
    ("Rize Limanı", 41.038116, 40.512742),
    ("Рыхтым", 40.997267, 37.879252),
    ("порт Сюрмене", 40.922736, 40.199488),
    ("порт Унье", 41.116684, 37.347944),
    ("порт Гёреле", 41.036751, 39.007990),
    ("порт Пазар", 41.181518, 40.907785),
    ("порт Фатса", 41.045014, 37.491285),
    ("Морские прогулки в Анапе", 44.897187, 37.302192),
    ("порт Хопа", 41.411229, 41.429952),
    ("Речной Терминал", 56.566817, 84.916594),
    ("Морской Торговый Порт Советская Гавань", 49.001837, 140.307925),
    ("Петропавловск-Камчатский морской торговый порт", 53.005735, 158.657452),
    ("Рыбный Порт", 53.018512, 158.645767),
    ("Морской ордена Знак Почёта торговый порт Певек", 69.703472, 170.264721),
    ("Ванинский морской торговый порт", 49.088633, 140.266269),
    ("Якутский речной порт", 62.047367, 129.772030),
    ("Углегорский Морской Торговый Порт", 49.072157, 142.030662),
    ("Николаевский морской торговый порт", 53.135379, 140.717258),
    ("Восточный Порт", 42.733815, 133.066221),
    ("Морской порт Владивосток", 43.097467, 131.865812),
    ("Свободный Торговый Порт", 51.346140, 128.169414),
    ("Ванинский морской торговый порт", 49.088299, 140.266423),
    ("Порт Бронка", 59.929308, 29.691717),
    ("Морской порт Санкт-Петербург", 59.911109, 30.250565),
    ("Приморский торговый порт", 60.335666, 28.716487)
    """
)

