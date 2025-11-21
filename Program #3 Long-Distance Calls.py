# A long-distance provider charges the following rates for telephone calls:

# Rate Category	Rate per Minute
# Daytime (6:00 A.M. through 5:59 P.M.) 	$0.02
# Evening (6:00 P.M.  through 11:59 P.M.) 	$0.12
# Off-Peak (midnight through 5:59 P.M.) 	$0.05

# Write a GUI application that allows the user to select a rate category
# (from a set of radio buttons), and enter the number of minutes of the call into an Entry widget.
# An info dialog box  should display the charge for the call.

import tkinter as tk
from tkinter import messagebox

class LongDistanceApp:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Long-Distance Calls")

        self.selected_rate_value = tk.DoubleVar()
        self.selected_rate_value.set(0.02)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.main_window, text="Select Rate Category:").pack(anchor='w', padx=10, pady=(10, 0))
        tk.Radiobutton(self.main_window, text="Daytime (6 AM - 5:59 PM) $0.02/min", variable=self.selected_rate_value,
                       value=0.02).pack(anchor='w', padx=20)
        tk.Radiobutton(self.main_window, text="Evening (6 PM - 11:59 PM) $0.12/min", variable=self.selected_rate_value,
                       value=0.12).pack(anchor='w', padx=20)
        tk.Radiobutton(self.main_window, text="Off-Peak (Midnight - 5:59 AM) $0.05/min",
                       variable=self.selected_rate_value, value=0.05).pack(anchor='w', padx=20)

        tk.Label(self.main_window, text="Enter Minutes of Call:").pack(anchor='w', padx=10, pady=(15, 0))
        self.minutes_entry = tk.Entry(self.main_window)
        self.minutes_entry.pack(anchor='w', padx=10)

        self.calculate_button = tk.Button(self.main_window, text="Calculate Charge", command=self.calculate_charge)
        self.calculate_button.pack(pady=20)

    def calculate_charge(self):
        try:
            minutes = float(self.minutes_entry.get())
            if minutes < 0:
                raise ValueError
            rate = self.selected_rate_value.get()
            charge = minutes * rate
            messagebox.showinfo("Call Charge", f"The total charge for the call is: ${charge:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid, positive number for minutes.")

    def run(self):
        self.main_window.mainloop()

if __name__ == '__main__':
    LongDistanceApp().run()