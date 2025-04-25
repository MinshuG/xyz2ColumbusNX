# xyz2ColumbusNX

A Python-based graphical tool for converting between molecular geometry file formats:
- XYZ format (standard molecular geometry format) 
- [Columbus](https://gitlab.com/columbus-program-system/columbus)/[NewtonX](https://gitlab.com/light-and-molecules/newtonx) geom format/ SHARC (uses same format I think)

## Screenshot
<img src="screenshot.png" alt="Screenshot of the application" width="600"/>

## Features

- Clean graphical interface with side-by-side editors
- Bidirectional conversion between XYZ and Columbus formats
- Support for both Angstrom and Atomic Units (Bohr) coordinate systems
- Smart parsing of XYZ files with various format variations
- File operations (open, save) via GUI or menu

## Installation

### Prerequisites

- Python 3 (tested with 3.12)
- Tkinter (usually bundled with Python)

### Setup

Clone this repository or download the source files [here]([https://github.com/MinshuG/xyz2ColumbusNX/releases]):

```bash
git clone https://github.com/MinshuG/xyz2ColumbusNX.git
cd xyz2nx
```

Make the script executable (Linux/Mac):

```bash
chmod +x xyz2col.py
```

## Usage

### Starting the Application

Run the application:

```bash
./xyz2col.py
```

Or:

```bash
python3 xyz2col.py
```

### Application Interface

The application window is divided into three main sections:
- **Left panel**: XYZ format editor with unit selection (Angstrom or Atomic Units)
- **Right panel**: Columbus format editor
- **Middle panel**: Conversion buttons

### Converting from XYZ to Columbus Format

1. **Input XYZ data** using one of these methods:
   - Type or paste XYZ data directly into the left text area
   - Use "File > Open XYZ File" to load a file
   
2. **Select the appropriate units** for your XYZ data:
   - Angstrom (default)
   - Atomic Units (Bohr)
   
3. **Click the "→ XYZ to Columbus" button** in the center panel

4. **View or save the Columbus format**:
   - The conversion result appears in the right text area
   - Use "File > Save Columbus File" to save the result

### Converting from Columbus to XYZ Format

1. **Input Columbus data** using one of these methods:
   - Type or paste Columbus data directly into the right text area
   - Use "File > Open Columbus File" to load a file
   
2. **Select the desired output units** for the XYZ data:
   - Angstrom (default)
   - Atomic Units (Bohr)
   
3. **Click the "← Columbus to XYZ" button** in the center panel

4. **View or save the XYZ format**:
   - The conversion result appears in the left text area
   - Use "File > Save XYZ File" to save the result

### File Format Details

#### XYZ Format
```
[number of atoms]
[comment line]
[element symbol] [x coord] [y coord] [z coord]
[element symbol] [x coord] [y coord] [z coord]
...
```

Example:
```
3
Water molecule
O    0.000000    0.000000    0.000000
H    0.757000    0.586000    0.000000
H   -0.757000    0.586000    0.000000
```

#### Columbus Format
```
[element symbol] [atomic number] [x coord] [y coord] [z coord] [atomic mass]
[element symbol] [atomic number] [x coord] [y coord] [z coord] [atomic mass]
...
```

Example:
```
O  8      0.0000000000      0.0000000000      0.0000000000 15.9949146400
H  1      1.4304876113      1.1073540364      0.0000000000  1.0078250370
H  1     -1.4304876113      1.1073540364      0.0000000000  1.0078250370
```

## Troubleshooting

### Common Issues

1. **"Unknown atom symbol" error**:
   - Ensure atomic symbols are valid chemical element symbols
   - The application supports all standard elements (H through Lr)
   
2. **"No valid atom coordinate lines found" error**:
   - Check that your XYZ format includes proper coordinate lines
   - Each line should have an element symbol followed by three numeric coordinates

3. **Format conversion problems**:
   - Verify that input data follows the expected format
   - The application tries to be flexible with XYZ format variations

## License

See the LICENSE file for details.
