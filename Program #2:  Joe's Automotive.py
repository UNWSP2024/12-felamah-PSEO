# Joe's Automotive performs the following routine maintenance service:

# Oil Change - $30.00
# Lube Job - $20.00
# Radiator Flush - $40.00
# Transmission Fluid - $100.00
# Inspection - $35.00
# Muffler replacement - $200.00
# Tire Rotation - $20.00
# Write a GUI with check buttons that allows the user to select any or all of these services.
# When the user clicks a button, the total charges should be displayed.


# --- Program 2: Joe's Automotive ---
import tkinter as tk

def calculate_total():

    total = 0

    if oil_change_var.get() == 1:
        total += 30.00
    if lube_job_var.get() == 1:
        total += 20.00
    if radiator_flush_var.get() == 1:
        total += 40.00
    # ... Add checks for all other services ...
    if transmission_fluid_var.get() == 1:
        total += 100.00
    if inspection_var.get() == 1:
        total += 35.00
    if muffler_var.get() == 1:
        total += 200.00
    if tire_rotation_var.get() == 1:
        total += 20.00

    total_label.config(text=f"Total Charges: ${total:.2f}")

root = tk.Tk()
root.title("Joe's Automotive")

oil_change_var = tk.IntVar()
lube_job_var = tk.IntVar()
radiator_flush_var = tk.IntVar()
transmission_fluid_var = tk.IntVar()
inspection_var = tk.IntVar()
muffler_var = tk.IntVar()
tire_rotation_var = tk.IntVar()

tk.Checkbutton(root, text="Oil Change - $30.00", variable=oil_change_var, command=calculate_total).pack(anchor='w')
tk.Checkbutton(root, text="Lube Job - $20.00", variable=lube_job_var, command=calculate_total).pack(anchor='w')
tk.Checkbutton(root, text="Radiator Flush - $40.00", variable=radiator_flush_var, command=calculate_total).pack(
    anchor='w')
tk.Checkbutton(root, text="Transmission Fluid - $100.00", variable=transmission_fluid_var,
               command=calculate_total).pack(anchor='w')
tk.Checkbutton(root, text="Inspection - $35.00", variable=inspection_var, command=calculate_total).pack(anchor='w')
tk.Checkbutton(root, text="Muffler replacement - $200.00", variable=muffler_var, command=calculate_total).pack(
    anchor='w')
tk.Checkbutton(root, text="Tire Rotation - $20.00", variable=tire_rotation_var, command=calculate_total).pack(
    anchor='w')

total_label = tk.Label(root, text="Total Charges: $0.00", font=("Helvetica", 14, "bold"))
total_label.pack(pady=20)

root.mainloop()