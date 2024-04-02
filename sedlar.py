class Sedlar:
    valörer = {
        "1000 Sedel": 1000,
        "500 Sedel": 500,
        "100 Sedel": 100,
        "50 Sedel": 50,
        "20 Sedel": 20,
        "10 Kronor": 10,
        "5 Kronor": 5,
        "1 Krona": 1,
        "50 öre": 0.50,
    }

    @classmethod
    def get_valörer(valuta):
        return valuta.valörer
