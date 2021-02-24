def event_time(date):
    #sample: 10/05/2020%2019:45:51:833000
    from datetime import datetime
    FORMAT_DATE_MILLISECONDS = "%m/%d/%Y %H:%M:%S:%f"
    return datetime.strptime(date,FORMAT_DATE_MILLISECONDS)

event_time.__schema__ = { 'type': 'string', 'format': "mm/dd/YYYY HH:MM:SS:Ms"}