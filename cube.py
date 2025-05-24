from cube10 import encode, decode

x, y, z = encode(lat=52.2297, lon=21.0122, alt=130.0)
lat, lon, alt = decode(x, y, z)
