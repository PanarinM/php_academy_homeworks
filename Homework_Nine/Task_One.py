# import time
#
# def leap_year(year):
#     """This function determines either the year is leap year or not
#     takes integer value of year
#     return True or False"""
#     try:
#         year = int(year)
#     except ValueError:
#         return False
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False


def leap_year(year):
    """This function determines either the year is leap year or not

        takes integer value of year
        return True or False"""
    try:
        year = int(year)
    except ValueError:
        return False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        else:
            return True
    return False

leap_years = []
for year in range(0, 2017):
    if leap_year(year):
        leap_years.append(year)

counter = len(leap_years)
print(leap_years)
print(counter)