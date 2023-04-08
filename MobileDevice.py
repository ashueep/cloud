from Data import Data
from LocalCompute import LocalCompute
from Compression import Compression
from Transmission import Radio

class MobileDevice:
    def __init__(self, lamda, mu, gamma, data: Data):
        self.lamda = lamda
        self.mu = mu
        self.gamma = gamma
        self.data = data
        self.energy = 0

    def total_energy(self):
        total_data = self.data.get_data()
        local_data = (1 - self.lamda) * total_data
        offload_data = self.lamda * total_data

        # offloaded data compression/decompression energy
        compression_off = Compression(d = offload_data, gamma = self.gamma, mu = self.mu)
        compress_off_e = compression_off.calc_compression_energy(time = 3, processor = 100)
        # compressed_off_d = compression.get_compressed_data_size()

        # local data compute energy
        local = LocalCompute(local_data, k = 2)
        compress_local = Compression(d = local_data, gamma = self.gamma, mu = self.mu)
        local_e = local.calc_local_energy(compressed_e=compress_local.calc_compression_energy(3, 100))

        # offloaded data radio transmission/recieve energy
        radio = Radio(0.1, 0.2, 0.3, 4, 0.3, 20, 3, 0.4, 0.5)
        radio_e = radio.calculate_radio_energy(self.mu, compress_off_e)

        total_e = radio_e + compress_off_e + local_e


        return total_e




data = Data(1000, 500, 40)

for i in range(10):
    lamda = (i + 1)/10
    device = MobileDevice(lamda, 1.4, 0.6, data)
    print(device.total_energy())

