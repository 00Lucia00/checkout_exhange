from changeCalculation import ChangeCalculation

class Application:
    def run(self):
        print("..Välkommen..")
        print("Här kan du se vad du ska få tillbaka i växel. Mata även in ören.")

        pris = float(input("Vad blev summan av dina varor?: "))
        betalt = float(input("Och vad betalade du?: "))

        change = ChangeCalculation.calculate_change(pris, betalt)

        print()
        print("Du ska få tillbaka:")
        for denomination, count in change.items():
            print(f"{count} x {denomination}")

        input("Press Enter to exit")

if __name__ == "__main__":
    app = Application()
    app.run()
