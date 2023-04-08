class Compression:
    def __init__(self, d, gamma, mu):
        # calculates compressed data
        self.d = d
        self.gamma = gamma
        self.mu = mu

    def get_compressed_data_size(self):
        return self.d * self.gamma
    
    def get_decompression_data_size(self):
        return self.d * self.gamma * self.mu

    def calc_compression_energy(self, time, processor):

        # formula on paper
        energy = time * processor / self.d

        return energy
    
    