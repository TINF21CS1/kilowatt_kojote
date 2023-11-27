

def month_add(x: (int, int), y: int) -> int:
    month_length = [31,28,31,30,31,30,31,31,30,31,30,31]
    days = x[1] + y
    month = x[0] + days//month_length[x[0]-1]
    days = days%30
    return (month, days)