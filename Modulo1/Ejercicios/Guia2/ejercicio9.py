date = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
day = date[:date.find('/')]
year_moth = date[date.find('/') + 1:]
month = year_moth[:year_moth.find('/')]
year = year_moth[year_moth.find('/') + 1:]
print('Día', day)
print('Mes', month)
print('Año', year)

# JANUARY = 1
# MARCH = 3
#
# date = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
# date_parts = date.split('/')  # [dia, mes, anio]
# month = 'ningún mes'
# day = date_parts[0]
# year = date_parts[2]
#
# if int(date_parts[1]) == JANUARY:
#     month = 'Enero'
# if int(date_parts[1]) == MARCH:
#     month = 'Marzo'
#
# print(f'Naciste el día {day} del mes {month} y el año {year}')
