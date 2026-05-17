import numpy as np
from scipy.spatial.transform import Rotation

class MockSerial:
    def __init__(self, data_type):
        self.data_type = data_type
        self.index = 0

    def readline(self):
        if self.data_type == 'imu':
            vals = [f"{np.random.uniform(-10,10):.2f}" for _ in range(3)]
            self.index += 1
            prefix = 'A' if self.index % 2 == 0 else 'G'
            return f"{prefix}:{','.join(vals)}".encode()
        elif self.data_type == 'gps':
            return b"$GNGGA,5109.026,N,10002.368,W,1,08,0.9,100.0,M,47.0,M,,*4A"
        elif self.data_type == 'flir':
            return b"THERMAL:640x480"

imu_serial = MockSerial('imu')
gps_serial = MockSerial('gps')
flir_serial = MockSerial('flir')

imu_data = {'accel': [0,0,0], 'gyro': [0,0,0]}
gps_data = {'lat': 0, 'lon': 0, 'alt': 0}
flir_data = {'thermal': None}

def read_imu():
    line = imu_serial.readline().decode().strip()
    vals = list(map(float, line[2:].split(',')))
    if line.startswith('A'): imu_data['accel'] = vals
    elif line.startswith('G'): imu_data['gyro'] = vals

def read_flir():
    line = flir_serial.readline().decode().strip()
    if line.startswith('THERMAL:'):
        w, h = map(int, line.split(':')[1].split('x'))
        flir_data['thermal'] = np.random.rand(h, w)

def fuse_sensors():
    rot = Rotation.from_euler('xyz', imu_data['gyro'], degrees=True)
    accel = rot.apply(imu_data['accel'])
    uap = bool(np.max(flir_data['thermal']) > 0.8) if flir_data['thermal'] is not None else False
    return {'accel': accel.tolist(), 'uap_detected': uap}

for _ in range(5):
    read_imu()
    read_flir()
    print(fuse_sensors())
