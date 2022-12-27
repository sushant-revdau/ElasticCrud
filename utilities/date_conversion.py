from datetime import datetime,timezone

def convert_date():
    date_convert =  datetime.now(timezone.utc).isoformat().replace("+00:00",'')
    converted_date = str(date_convert).split('.')[0]
    return converted_date
