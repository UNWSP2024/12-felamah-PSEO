# Write a GUI program that calculates a car's gas mileage.
# The program's window should have Entry widgets that let the user enter the number of
# gallons of gas the car holds, and the number of miles it can be driven on a full tank.
# When a Calculate MPG button is clicked, the program should display the number of miles that
# the car may be driven per gallon of gas.
# Use the following formula to calculate miles per gallon:  MPG = miles / gallons.

import tkinter

class CalculateMilage:
    def __init__(self):
        self.window = tkinter.Tk()
        self.first_frame = tkinter.Frame(self.window)
        self.second_frame  = tkinter.Frame(self.window)
        self.third_frame = tkinter.Frame(self.window)
        self.fourth_frame = tkinter.Frame(self.window)

        self.numGallons_label = tkinter.Label(self.first_frame, text = 'Number of gallons the car holds:')
        self.numGallons_entry = tkinter.Entry(self.first_frame, width = 10)
        self.numGallons_label.pack(side = 'left')
        self.numGallons_entry.pack(side = 'left')

        self.numMiles_label = tkinter.Label(self.second_frame, text = 'Number of miles driven on a full tank:')
        self.numMiles_entry = tkinter.Entry(self.second_frame, width = 10)
        self.numMiles_label.pack(side = 'left')
        self.numMiles_entry.pack(side = 'left')

        self.MPG_label = tkinter.Label(self.third_frame, text = 'MPG:' )
        self.value = tkinter.StringVar()
        self.MPG = tkinter.Label(self.third_frame, textvariable = self.value)
        self.MPG_label.pack(side = 'left')
        self.MPG.pack(side = 'left')

        self.calc_button = tkinter.Button(self.fourth_frame, text = 'Calculate MPG', command = self.calculate)
        self.quit_button = tkinter.Button(self.fourth_frame, text = 'Quit', command = self.window.destroy)
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')

        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.fourth_frame.pack()

        tkinter.mainloop()

    def calculate(self):
        try:
            miles = float(self.numMiles_entry.get())
            gallons = float(self.numGallons_entry.get())
            if gallons == 0:
                self.value.set('Error: Cannot divide by zero')
            else:
                mileGallon = miles / gallons
        except ValueError:
            self.value.set('Error: Cannot calculate MPG')

        self.value.set(mileGallon)

if __name__ == '__main__':
    calculator = CalculateMilage()
