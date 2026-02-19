class TransportExpress(StrategieTransport):
    def calculeaza_cost(self,comanda:Comanda) -> float:
        return 20 + 0.8*comanda.distanta_km + 1.8* comanda.greutate_kg