from daty import Dates

date = Dates("13-12-2026")
date_format_db = "13/12/2026"

date_with_dash = Dates.to_dash_date(date_format_db)

d1 = date.get_date()
d2 = date_with_dash

if d1 == d2:
    print("Takie same daty")
    print(f"{d1} = {d2}")
else:
    print("Rózne daty")
    print(f"{d1} != {d2}")
# Takie same daty
# 13-12-2026 = 13-12-2026
