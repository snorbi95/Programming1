

def convert_date(datum):
    datum_dict = {}
    list = ['JAN','FEB','MAR','APR','MAY','JUN'\
            ,'JUL','AUG','SEP','OCT','NOV','DEC']
    num = 1
    for month in list:
        datum_dict[month] = num
        num += 1
    datum_list = datum.split('-')
    day = int(datum_list[0])
    month = datum_dict[datum_list[1]]
    if int(datum_list[2]) > 20:
        year = 1900 + int(datum_list[2])
    else:
        year = 2000 + int(datum_list[2])
    return (year, month, day)

datum = input("Kerem a datumot: ")
converted_date = convert_date(datum)
print(converted_date)
