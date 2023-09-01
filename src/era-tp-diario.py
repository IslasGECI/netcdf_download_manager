#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()

server.retrieve({
    "class": "ei",
    "dataset": "interim",
    "expver": "1",
    "grid": "0.75/0.75",
    "levtype": "sfc",
    "param": "228.128",
    "step": "3",
    "stream": "oper",
    "time": "00:00:00",
    "type": "fc",
    'date'      : "2003-01-01/to/2018-01-31",
    'area'      : "51/-153/17/-104",
    'format'    : "netcdf",
    'target'    : "era-tp-concatenado-diario-2003-2018.nc"
 })
