from sedlar import Sedlar

class ChangeCalculation:
    @staticmethod
    def calculate_change(pris, betalt):
        total = betalt - pris
        växel = {}

        sedel = Sedlar.get_valörer()

        for sedel, värde in sedel.items():
            count = int(total / värde)
            if count > 0:
                växel[sedel] = count
                total %= värde

        return växel
