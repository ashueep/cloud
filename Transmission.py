class Radio:
    c = 3 * 10**8
    fc = 850 * 10**6
    def __init__(self,  
                 snr = 20, 
                 b = 2, 
                 B = 5*10**6, 
                 N_0 = 4 * 10 ** -12, 
                 nf = 10, 
                 d = 250, 
                 n = 3.5, 
                 gr = 1, 
                 gt = 1):
        self.snr = snr
        self.b = b
        self.B = B
        self.N_0 = N_0 
        self.nf = nf 
        self.prx = snr * b * B * (N_0/2) * nf 
        self.ptx = (((4 * 3.141592 * self.fc) / self.c) ** 2) * (d ** n) * (self.prx / (gr * gt))

    def calculate_radio_energy(self, mu, data, eeta = 0.33, pckt = 100):
        t_tx = data/ (2 * self.B)
        t_rx = mu * data/ (2 * self.B)
        energy = ((self.ptx / eeta + pckt) * t_tx + (self.prx + pckt) * t_rx)/ data

        return energy