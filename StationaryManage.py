import tkinter as tk
from tkinter import ttk, messagebox



class StationaryStore:


    def __init__(self, root):
        self.root = root
        root.title("Stationary Store Management")
        root.geometry("650x550")

        self.menu = {
            "Pencils": 2, "Colored pencils": 4, "Pens": 2, "Paper": 1, "Colored paper": 2, "Erasers": 3, "Sharpeners": 3, "Scissors": 7, "Pins": 1}
        self.rate = 82
        self.entries = {}

        frame = ttk.Frame(root, padding = 20)
        frame.pack(expand = True)

        ttk.Label(frame, text = "Stationary Order", font = ("Arial", 18, "bold")).grid(row = 0, columnspan = 3)

        for i, (item, price) in enumerate(self.menu.items(), 1):
            ttk.Label(frame, text=f"{item} ($ {price})").grid(row = i, column = 0)
            e = ttk.Entry(frame, width = 5)
            e.grid(row = i, column = 1)
            self.entries[item] = e

        self.currency = tk.StringVar(value = "USD")
        ttk.Combobox(frame, textvariable = self.currency, values = ("USD", "INR"), state = "readonly", width = 10).grid(row = len(self.menu)+1, column = 1)

        ttk.Button(frame, text = "Place Order", command = self.place_order).grid(row =len(self.menu)+2, columnspan = 3, pady = 10)


    def denomination(self, amount):

       denoms = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
       result = ""

       for d in denoms:
           count = amount // d
           if count:
               result += f"{d} x {count}\n"
               amount %= d
       return result


    def place_order(self):

        total = 0
        rate = self.rate if self.currency.get() == "INR" else 1
        symbol = "₹" if rate != 1 else "$"

        for item, e in self.entries.items():
            if e.get().isdigit():
                total += int(e.get()) * self.menu[item] * rate

        if total == 0:
            messagebox.showerror("ERROR", "No Items Selected")
            return

        msg = f"Total Amount: {symbol}{int(total)}\n\nDenomination:\n"
        msg += self.denomination(int(total))
        messagebox.showinfo("Bill", msg)



if __name__ == "__main__":

    tk.Tk().after(0, lambda: StationaryStore(tk._default_root))
    tk.mainloop()