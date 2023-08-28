class ATM:
    def __init__(self):
        self.notes = [500, 50, 200]

    def calculate_notes(self, amount):
        values = {}
        notes_copy = list(self.notes)
        while amount > 0:
            max_note = max(notes_copy)
            if amount >= max_note:
                values[max_note] = amount // max_note
                amount %= max_note
            else:
                notes_copy.remove(max_note)
        return values

    def run(self):
        while True:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if not (amount > 0 and amount % 50 == 0):
                    print("Invalid amount. Please enter a valid amount (multiple of 50).")
                    continue
                notes_count = self.calculate_notes(amount)
                for note, count in notes_count.items():
                    print(f"{note} notes : {count}")

                choice = input("Do you want to continue (C) or cancel (X)? ").strip().lower()
                if choice == 'x':
                    print("Transaction canceled.")
                    break
            except ValueError as e:
                print(f"{e}")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
