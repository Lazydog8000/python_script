from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "date": "1979-03-01/to/2018-12-31",
    "expver": "1",
    "format":"netcdf",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": "230.140/232.140",
    "step": "0",
    "stream": "wave",
    "time": "00:00:00/06:00:00/12:00:00/18:00:00",
    "type": "an",
    "target": "D:/ecmwf_data_download",
})