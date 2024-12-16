## ------------------------------------------------ Gooey GUI ------------------------------------------------ ##

from argparse import ArgumentParser
from gooey import Gooey, GooeyParser
from pyswip import Prolog

# Initialize Prolog instance
swipl = Prolog()
swipl.consult("File1.pl")  # Ensure the file path is correct

@Gooey
def check_travel():
    # Gooey UI parser
    parser = GooeyParser(description="Check Travel Options")
    parser.add_argument(
        "-s", "--start", required=True,
        help="Starting location\n(Please capitalize the first letter)"
    )
    parser.add_argument(
        "-e", "--end", required=True,
        help="Destination location\n(Please capitalize the first letter)"
    )
    parser.add_argument(
        "-t", "--transport", 
        choices=["train", "plane", "car", "any"], 
        default="any", 
        help="Select transport type (Optional)"
    )

    args = parser.parse_args()

    start_location = args.start
    end_location = args.end
    selected_transport = args.transport

    # Determine travel options
    if selected_transport == "any":
        print(f"\nChecking all transport options from {start_location} to {end_location}...")
        direct_travel = check_direct_travel_prolog(start_location, end_location)
        if direct_travel:
            print("\nDirect travel options:")
            for travel in direct_travel:
                print(f"- {travel}")
        else:
            print(f"\nNo direct travel from {start_location} to {end_location}.")

        print("\nChecking indirect travel options...")
        indirect_travel = check_indirect_travel_prolog(start_location, end_location)
        if indirect_travel:
            for travel in indirect_travel:
                print(f"- {travel}")
        else:
            print(f"No indirect travel options found from {start_location} to {end_location}.")
    else:
        print(f"\nChecking {selected_transport} transport from {start_location} to {end_location}...")
        direct_travel = check_direct_travel_prolog_with_transport(start_location, end_location, selected_transport)
        if not direct_travel:
            print("\nChecking indirect travel options...")
            indirect_travel = check_indirect_travel_prolog(start_location, end_location)
            if indirect_travel:
                for travel in indirect_travel:
                    print(f"- {travel}")
            else:
                print(f"No indirect travel options found from {start_location} to {end_location}.")

def check_direct_travel_prolog(start, end):
    query = f"can_travel_directly('{start}', '{end}', Transport)."
    results = list(swipl.query(query))
    return [f"{start} to {end} by {result['Transport']}" for result in results]

def check_direct_travel_prolog_with_transport(start, end, transport):
    query = f"can_travel_directly('{start}', '{end}', '{transport}')."
    results = list(swipl.query(query))
    if results:
        for result in results:
            print(f"Direct travel available: {start} to {end} by {transport}")
        return results
    else:
        print(f"No direct travel available from {start} to {end} by {transport}.")
        return None

def check_indirect_travel_prolog(start, end):
    query = f"can_travel_indirectly('{start}', '{end}', Transports)."
    results = list(swipl.query(query))
    indirect_travels = []
    for result in results:
        transports = result["Transports"]
        if len(transports) == 3:  # Ensure result includes intermediate stop
            transport1, intermediate, transport2 = transports
            indirect_travels.append(
                f"{start} to {intermediate} by {transport1}, then {intermediate} to {end} by {transport2}"
            )
    return indirect_travels

if __name__ == "__main__":
    check_travel()


## ------------------------------------------------ TKInter GUI ------------------------------------------------ ##


# import tkinter as tk
# from tkinter import ttk, messagebox
# from pyswip import Prolog

# # Initialize Prolog instance
# swipl = Prolog()
# swipl.consult("File1.pl")  # Ensure the Prolog file is available

# def check_travel():
#     """Function to handle travel queries based on user input."""
#     start_location = start_var.get()
#     end_location = end_var.get()
#     selected_transport = transport_var.get()

#     if not start_location or not end_location:
#         messagebox.showerror("Input Error", "Please provide both start and end locations.")
#         return

#     result_box.delete("1.0", tk.END)  # Clear previous results

#     # Query Prolog for travel options
#     if selected_transport == "Any":
#         direct_travel = check_direct_travel_prolog(start_location, end_location)
#         if direct_travel:
#             result_box.insert(tk.END, "Direct travel options:\n")
#             for travel in direct_travel:
#                 result_box.insert(tk.END, f"- {travel}\n")
#         else:
#             result_box.insert(tk.END, f"No direct travel from {start_location} to {end_location}.\n")

#         indirect_travel = check_indirect_travel_prolog(start_location, end_location)
#         if indirect_travel:
#             result_box.insert(tk.END, "\nIndirect travel options:\n")
#             for travel in indirect_travel:
#                 result_box.insert(tk.END, f"- {travel}\n")
#         else:
#             result_box.insert(tk.END, "No indirect travel options found.\n")
#     else:
#         direct_travel = check_direct_travel_prolog_with_transport(start_location, end_location, selected_transport)
#         if direct_travel:
#             result_box.insert(tk.END, f"Direct travel by {selected_transport}:\n")
#             for travel in direct_travel:
#                 result_box.insert(tk.END, f"- {travel}\n")
#         else:
#             result_box.insert(tk.END, f"No direct travel by {selected_transport}.\n")

# def check_direct_travel_prolog(start, end):
#     query = f"can_travel_directly('{start}', '{end}', Transport)."
#     results = list(swipl.query(query))
#     return [f"{start} to {end} by {result['Transport']}" for result in results]

# def check_direct_travel_prolog_with_transport(start, end, transport):
#     query = f"can_travel_directly('{start}', '{end}', '{transport}')."
#     results = list(swipl.query(query))
#     return [f"{start} to {end} by {transport}"] if results else []

# def check_indirect_travel_prolog(start, end):
#     query = f"can_travel_indirectly('{start}', '{end}', Transports)."
#     results = list(swipl.query(query))
#     indirect_travels = []
#     for result in results:
#         transports = result["Transports"]
#         if len(transports) == 3:
#             transport1, intermediate, transport2 = transports
#             indirect_travels.append(
#                 f"{start} to {intermediate} by {transport1}, then {intermediate} to {end} by {transport2}"
#             )
#     return indirect_travels

# # Create main Tkinter window
# root = tk.Tk()
# root.title("Travel Checker - Dark Theme")
# root.geometry("600x500")
# root.configure(bg="#2e2e2e")  # Dark background color

# # Define dark theme colors
# bg_color = "#2e2e2e"  # Background
# fg_color = "#ffffff"  # Text color
# entry_bg = "#3b3b3b"  # Entry field background
# entry_fg = "#2e2e2e"  # Entry field text color
# button_bg = "#555555"  # Button background
# button_fg = "#ffffff"  # Button text color
# result_bg = "#1e1e1e"  # Result box background
# result_fg = "#ffffff"  # Result box text color

# # Title Label
# title_label = tk.Label(root, text="Travel Checker", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color)
# title_label.pack(pady=10)

# # Input Frame
# input_frame = tk.Frame(root, bg=bg_color)
# input_frame.pack(pady=10)

# # Start Location
# tk.Label(input_frame, text="Start Location:", font=("Helvetica", 12), bg=bg_color, fg=fg_color).grid(row=0, column=0, padx=10, pady=5)
# start_var = tk.StringVar()
# start_entry = ttk.Entry(input_frame, textvariable=start_var, font=("Helvetica", 12), width=20)
# start_entry.grid(row=0, column=1, padx=10, pady=5)
# start_entry.configure(background=entry_bg, foreground=entry_fg)

# # End Location
# tk.Label(input_frame, text="End Location:", font=("Helvetica", 12), bg=bg_color, fg=fg_color).grid(row=1, column=0, padx=10, pady=5)
# end_var = tk.StringVar()
# end_entry = ttk.Entry(input_frame, textvariable=end_var, font=("Helvetica", 12), width=20)
# end_entry.grid(row=1, column=1, padx=10, pady=5)
# end_entry.configure(background=entry_bg, foreground=entry_fg)

# # Transport Dropdown
# tk.Label(input_frame, text="Transport Type:", font=("Helvetica", 12), bg=bg_color, fg=fg_color).grid(row=2, column=0, padx=10, pady=5)
# transport_var = tk.StringVar(value="Any")
# transport_dropdown = ttk.Combobox(input_frame, textvariable=transport_var, font=("Helvetica", 12), width=18, state="readonly")
# transport_dropdown["values"] = ["Any", "Train", "Plane", "Car"]
# transport_dropdown.grid(row=2, column=1, padx=10, pady=5)

# # Submit Button
# submit_button = tk.Button(root, text="Check Travel Options", command=check_travel, bg=button_bg, fg=button_fg, font=("Helvetica", 12), bd=0, relief="flat")
# submit_button.pack(pady=10)

# # Result Box
# result_frame = tk.Frame(root, bg=bg_color)
# result_frame.pack(pady=10, fill="both", expand=True)

# result_label = tk.Label(result_frame, text="Results:", font=("Helvetica", 12, "bold"), bg=bg_color, fg=fg_color)
# result_label.pack(anchor="w", padx=10)

# result_box = tk.Text(result_frame, wrap="word", font=("Helvetica", 12), height=15, width=70, bg=result_bg, fg=result_fg, bd=1, relief="solid")
# result_box.pack(padx=10, pady=5, fill="both", expand=True)

# # Scrollbar
# scrollbar = ttk.Scrollbar(result_frame, command=result_box.yview)
# result_box.config(yscrollcommand=scrollbar.set)
# scrollbar.pack(side="right", fill="y")

# # Run the Tkinter main loop
# root.mainloop()
