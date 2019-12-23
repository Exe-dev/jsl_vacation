def fiscal_year(datetime):
    if 0 < datetime.month < 4:
        year = datetime.year - 1
        return year
    else:
        return datetime.year
