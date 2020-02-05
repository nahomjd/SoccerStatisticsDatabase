

def format(date):
    count = 0
    if date == "":
        return ""
    day = date.split("/")[0]
    
    if len(day) == 1:
        day = "0" + day
    

    month = date.split("/")[1]
    
    if len(month) == 1:
        month = "0" + month
    

    year = date.split("/")[2]
    
    if len(year) == 2:
        if int(year) > 50:
            year = "19" + year
        else:
            year = "20" + year
    

    formatted = year + "-" + month + "-" + day
    count += 1
    
    return formatted

    


