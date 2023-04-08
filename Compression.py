class Compression:
    def __init__(self, s: int, f: int, b: int):
        self.s = s
        self.f = f
        self.b = b

        # calculates compressed data
        self.d = s * f * b

    def get_compressed_data_size(self):
        return self.d

    def calc_compression_energy(self, time, processor):

        # formula on paper
        energy = time * processor / self.d

        return energy
    
    