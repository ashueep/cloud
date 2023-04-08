import Compression

class LocalCompute:
    def __init__(self, data, k):
        self.data = data
        self.k = k

    def calc_local_energy(self, compressed_e):
        return self.k * compressed_e