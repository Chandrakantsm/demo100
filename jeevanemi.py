import tkinter as tk

def calculate_emi():
    principle = float(principle_entry.get())
    rate = float(rate_entry.get()) / (12 * 100)  # Monthly interest rate
    time = float(time_entry.get()) * 12  # Monthly time period

    emi = (principle * rate * (1 + rate) ** time) / ((1 + rate) ** time - 1)

     inemi_label.config(text=f"EMI: {round(emi, 2)}")

root = tk.Tk()
root.title("EMI Calculator")

                    
principle_label = tk.Label(root, text="Principle amount:")
principle_label.grid(row=0, column=0, padx=10, pady=10)

principle_entry = tk.Entry(root)
principle_entry.grid(row=0, column=1, padx=10, pady=10)

rate_label = tk.Label(root, text="Interest rate:")
rate_label.grid(row=1, column=0, padx=10, pady=10)

rate_entry = tk.Entry(root)
rate_entry.grid(row=1, column=1, padx=10, pady=10)

time_label = tk.Label(root, text="Time (in years):")
time_label.grid(row=2, column=0, padx=10, pady=10)

time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_emi)
calculate_button.grid(row=3, column=0, padx=10, pady=10)

emi_label = tk.Label(root, text="EMI: ")
emi_label.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()