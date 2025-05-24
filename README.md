# Cube10 — Specification for 3D Earth Grid with 10 cm Resolution

**Version:** 0.1 (draft)

---

## 📖 1. Purpose

Cube10 is a 3D spatial indexing system that divides the Earth (including surface and atmosphere) into uniform cubes of **0.1 × 0.1 × 0.1 meters (10 cm)**. 

### Intended Use Cases:
- High-resolution sensor data registration
- Real-time monitoring
- Autonomous drone/robot navigation
- Environmental modeling

---

## 🛆 2. Cube Structure

Each cube is identified by a 3D index:
```text
Cube10(x, y, z)
```

### 2.1 Origin (0, 0, 0):
```text
Latitude:  -90.000000°
Longitude: -180.000000°
Altitude:   0.000 m (mean sea level or WGS84 ellipsoid)
```

### 2.2 Cube Size:
```text
X (longitude): 0.1 m
Y (latitude):  0.1 m
Z (altitude):  0.1 m
```

---

## 📉 3. Indexing

### 3.1 Coordinate Conversion:
Convert geographic coordinates (WGS84) to meters using a projection (e.g., ECEF or UTM).

### 3.2 Grid Index Calculation:
```python
x = floor((x_meters - origin_x) / 0.1)
y = floor((y_meters - origin_y) / 0.1)
z = floor((z_meters - origin_z) / 0.1)
```

---

## 🧹 4. Storage Format

### JSON Example:
```json
{
  "x": 12512340,
  "y": 87881022,
  "z": 3040,
  "data": {
    "temperature": 22.4,
    "humidity": 0.65,
    "source": "sensor_218",
    "timestamp": "2025-05-24T13:15:00Z"
  }
}
```

### Binary (Proposed):
```binary
[int32 x][int32 y][int32 z][payload]
```

---

## 🌐 5. Coordinate Ranges

| Parameter | Range Description |
|----------|--------------------|
| Max X    | Depends on Earth's length (~400 million cubes) |
| Max Y    | Depends on Earth's width |
| Max Z    | 0 to 100000 (for up to 10 km altitude) |

---

## 🛠️ 6. Libraries & Implementation

**Languages:** Python, Rust, C++

### Core Modules:
- WGS84 to Cube10 Encoder/Decoder
- JSON/Binary storage format
- Optional 3D viewer (WebGL/Cesium/Potree)

---

## 🧪 7. Example Usage

```python
from cube10 import encode, decode

x, y, z = encode(lat=52.2297, lon=21.0122, alt=130.0)
lat, lon, alt = decode(x, y, z)
```

---

## ⚖️ 8. License

Open standard under **MIT License** or **CC-BY 4.0**.
