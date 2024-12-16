# Planning a Travel Journey - Prolog Travel Planning Application

Welcome to the **Planning a Travel Journey** project! This application helps you plan your travel journey by providing different travel options between various locations. It uses Prolog for logic-based travel options, a Gooey-based GUI for user interaction, and Python for the implementation.

## Project Overview

This project allows users to input a starting location, destination, and preferred mode of transport (optional) to check travel options. The travel options can be **direct** or **indirect** routes, depending on the selected criteria. The logic for determining travel options is handled by Prolog, and the user interface is built using the **Gooey** library for ease of use.

### Features:
- Check **direct** and **indirect** travel routes.
- Optionally, filter by **transport type** (train, plane, car, or any).
- User-friendly **Gooey** GUI for easy input.
- **Prolog**-based knowledge base for travel logic.

## Requirements

To run this application, you'll need the following dependencies:

- Python 3.x
- [Gooey](https://github.com/chriskiehl/Gooey)
- [PySWIP](https://github.com/yuce/pyswip) (Python wrapper for SWI-Prolog)
- SWI-Prolog (installed and set up in your environment)

### Install the required Python packages:
```bash
pip install gooey pyswip
```

### Install SWI-Prolog:
1. Download SWI-Prolog from [here](https://www.swi-prolog.org/Download.html).
2. Install and make sure it's available in your system's PATH.

## How to Use

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Osama-Abo-Bakr/Planning-a-Travel-Journey.git
   ```

2. **Run the program**:
   After setting up the project, navigate to the project directory and run the main Python script:
   ```bash
   python main.py
   ```

3. **Use the GUI**:
   The application will open a Gooey-based GUI where you can:
   - Enter the **starting location**.
   - Enter the **destination**.
   - Choose a transport mode (optional):
     - `train`
     - `plane`
     - `car`
     - `any` (default, checks all transport modes).

4. **View the results**:
   The program will check for:
   - **Direct travel options** between the specified locations.
   - **Indirect travel options** with intermediate stops (if no direct option is available).

## Code Explanation

- **Gooey GUI**: The `Gooey` decorator is used to create a user-friendly interface for the program. The user inputs the `start`, `end`, and optional `transport` preferences, which are parsed using the `GooeyParser`.
  
- **Prolog Queries**: The logic for travel options is based on Prolog rules. We load a Prolog file (`File1.pl`) containing the rules for travel and query it to find direct or indirect travel options. The `PySWIP` library is used to interface with Prolog from Python.

### Key Functions:

- `check_travel()`: Main function to handle user input and print travel options.
- `check_direct_travel_prolog(start, end)`: Queries Prolog for direct travel options.
- `check_direct_travel_prolog_with_transport(start, end, transport)`: Queries Prolog for direct travel based on the selected transport type.
- `check_indirect_travel_prolog(start, end)`: Queries Prolog for indirect travel options (with intermediate stops).

## Prolog Knowledge Base

The travel logic is implemented in the Prolog file `File1.pl`, which contains rules like:
```prolog
can_travel_directly('New York', 'Los Angeles', 'plane').
can_travel_directly('Los Angeles', 'San Francisco', 'car').
can_travel_indirectly('New York', 'San Francisco', ['plane', 'Chicago', 'car']).
```

This file needs to be consulted by the Prolog engine (`swipl.consult("File1.pl")`).

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make improvements or suggestions, and create a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support regarding the project, feel free to open an issue on the [GitHub repository](https://github.com/Osama-Abo-Bakr/Planning-a-Travel-Journey.git).