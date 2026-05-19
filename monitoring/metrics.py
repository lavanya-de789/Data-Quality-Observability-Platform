from prometheus_client import *

records=Gauge(
'processed_records',
'total records'
)

validation=Gauge(
'validation_success',
'validation status'
)

records.set(100)

validation.set(1)

start_http_server(8000)

while True:
    pass
