def duplicate_city(cities):
     result_city = list()
     s = set()
 def inters(l1, l2):
     l3 = list()
     for v in l1:
         if v in l2:
             l3.append(v)
     return l3
 
     for city in cities:
         l1 = len(s)
         s.add(city)
         l2 = len(s)
         if l1 == l2:
             result_city.append(city)
     return result_city
 
 
 cities = ['Suwon', 'Hwasung', 'Incheon', 'Incheon', 'Bucheon', 'Incheon', 'Seoul']
 cities.append('Seoul')
 cities.append('Anyang')
 print(cities)
 print(set(duplicate_city(cities)))
 l1 = [45, 5, 22, 31, 7, 19]
 l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
 print(inters(l1, l2))
