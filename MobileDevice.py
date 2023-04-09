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
        compress_off_e = compression_off.calc_compression_energy(time = 1, processor = 2.4 * 10**9)
        compressed_off_d = compression_off.get_compressed_data_size()

        # local data compute energy
        local = LocalCompute(local_data, k = 2)
        compress_local = Compression(d = local_data, gamma = self.gamma, mu = self.mu)
        local_e = local.calc_local_energy(compressed_e=compress_local.calc_compression_energy(time = 1, processor = 2.4 * 10**9))

        # offloaded data radio transmission/recieve energy
        radio = Radio()
        radio_e = radio.calculate_radio_energy(self.mu, compressed_off_d)

        total_e = radio_e + compress_off_e + local_e


        return total_e




data = Data(s = 1280 * 720, f = 600, b = 12)

for i in range(999):
    lamda = (i + 1)/1000
    device = MobileDevice(lamda, 1.4, 0.6, data)
    print("%.4f %f" % (lamda, device.total_energy()))

