from fake.points import Points


# ----------------------------------
# синтетические данные

n = 100  # количество человек

# Places().demo()
# Moves().demo()

# Track().demo()
# Location().demo()

points = Points()
points.save(n)  # создаем несколько человек

# ----------------------------------
# обработка и сохранения данных

# print('process')
# process = Process(n)
# data.load(process.make)  # получаем точки и обрабатываем их
#
# # ----------------------------------
# # поиск точек притяжения
#
# print('attract')
# i = 23  # человек
#
# points = []  # берем все точки человека
# for q in point_collection.get({'i': i}):
#     points.append(Position(q['i'], q['x'], q['y'], q['t'], q['e']))
#
# attract = Attract()  # вычисляем точки притяжения
# p = attract.make(points)
#
# place_collection.delete({'i': i})
# place_collection.insert_many(p)
#
# # ----------------------------------
# # присутствие в области
#
# print('present')
#
# circle = Circle(MAP_CX, MAP_CY, 123)  # задаем окружность
# present = Present()
#
# persons = present.make(circle, None)  # находим людей внутри области
