class Radio:
    c = 3 * 10**8
    fc = 850 * 10**6
    def __init__(self,  snr, b, B, N_0, nf, d, n, gr, gt):
        self.snr = snr
        self.b = b
        self.B = B
        self.N_0 = N_0 
        self.nf = nf 
        self.prx = snr * b * B * (N_0/2) * nf 
        self.ptx = (((4 * 3.141592 * self.fc) / self.c) ** 2) * (d ** n) * (self.prx / (gr * gt))

    def calculate_radio_energy(self, mu, gamma, lamda, data):
        t_tx = mu * lamda * data/ (2 * self.B)
        t_rx = mu * gamma * lamda * data/ (2 * self.B)
        energy = (self.ptx * t_tx + self.prx * t_rx)/ data

        return energy