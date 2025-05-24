from datetime import datetime

def is_adult(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    if age < 0:
        raise ValueError("出生年份不可以在未來")
    return age >= 18
# ooooo