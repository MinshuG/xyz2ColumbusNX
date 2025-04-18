#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# https://gitlab.com/columbus-program-system/columbus/-/blob/master/Columbus/source/utils/xyz2col.f90

atomic_data = {"x":{"name":0,"symbol":0},"h":{"name":1,"symbol":1.007825037},"he":{"name":2,"symbol":4.00260325},"li":{"name":3,"symbol":7.0160045},"be":{"name":4,"symbol":9.0121825},"b":{"name":5,"symbol":11.0093053},"c":{"name":6,"symbol":12},"n":{"name":7,"symbol":14.003074008},"o":{"name":8,"symbol":15.99491464},"f":{"name":9,"symbol":18.99840325},"ne":{"name":10,"symbol":19.9924391},"na":{"name":11,"symbol":22.9897697},"mg":{"name":12,"symbol":23.985045},"al":{"name":13,"symbol":26.9815413},"si":{"name":14,"symbol":27.9769284},"p":{"name":15,"symbol":30.9737634},"s":{"name":16,"symbol":31.9720718},"cl":{"name":17,"symbol":34.968852729},"ar":{"name":18,"symbol":39.9623831},"k":{"name":19,"symbol":38.9637079},"ca":{"name":20,"symbol":39.9625907},"sc":{"name":21,"symbol":44.9559136},"ti":{"name":22,"symbol":47.9479467},"v":{"name":23,"symbol":50.9439625},"cr":{"name":24,"symbol":51.9405097},"mn":{"name":25,"symbol":54.9380463},"fe":{"name":26,"symbol":55.9349393},"co":{"name":27,"symbol":58.9331978},"ni":{"name":28,"symbol":57.9353471},"cu":{"name":29,"symbol":62.9295992},"zn":{"name":30,"symbol":63.9291454},"ga":{"name":31,"symbol":68.9255809},"ge":{"name":32,"symbol":73.9211788},"as":{"name":33,"symbol":74.9215955},"se":{"name":34,"symbol":79.9165205},"br":{"name":35,"symbol":78.9183361},"kr":{"name":36,"symbol":83.8},"rb":{"name":37,"symbol":85.4678},"sr":{"name":38,"symbol":87.62},"y":{"name":39,"symbol":88.9059},"zr":{"name":40,"symbol":91.22},"nb":{"name":41,"symbol":92.9064},"mo":{"name":42,"symbol":95.94},"tc":{"name":43,"symbol":98},"ru":{"name":44,"symbol":101.07},"rh":{"name":45,"symbol":102.9055},"pd":{"name":46,"symbol":106.4},"ag":{"name":47,"symbol":107.868},"cd":{"name":48,"symbol":112.41},"in":{"name":49,"symbol":114.82},"sn":{"name":50,"symbol":118.69},"sb":{"name":51,"symbol":121.75},"te":{"name":52,"symbol":127.6},"i":{"name":53,"symbol":126.9045},"xe":{"name":54,"symbol":131.3},"cs":{"name":55,"symbol":132.9054},"ba":{"name":56,"symbol":137.33},"la":{"name":57,"symbol":138.9055},"ce":{"name":58,"symbol":140.12},"pr":{"name":59,"symbol":140.9077},"nd":{"name":60,"symbol":144.24},"pm":{"name":61,"symbol":145},"sm":{"name":62,"symbol":150.4},"eu":{"name":63,"symbol":151.96},"gd":{"name":64,"symbol":157.25},"tb":{"name":65,"symbol":158.9254},"dy":{"name":66,"symbol":162.5},"ho":{"name":67,"symbol":164.9304},"er":{"name":68,"symbol":167.26},"tm":{"name":69,"symbol":168.9342},"yb":{"name":70,"symbol":173.04},"lu":{"name":71,"symbol":174.967},"hf":{"name":72,"symbol":178.49},"ta":{"name":73,"symbol":180.9479},"w":{"name":74,"symbol":183.85},"re":{"name":75,"symbol":186.207},"os":{"name":76,"symbol":190.2},"ir":{"name":77,"symbol":192.22},"pt":{"name":78,"symbol":195.09},"au":{"name":79,"symbol":196.9665},"hg":{"name":80,"symbol":200.59},"tl":{"name":81,"symbol":204.37},"pb":{"name":82,"symbol":207.2},"bi":{"name":83,"symbol":208.9804},"po":{"name":84,"symbol":209},"at":{"name":85,"symbol":210},"rn":{"name":86,"symbol":222},"fr":{"name":87,"symbol":223},"ra":{"name":88,"symbol":226.0254},"ac":{"name":89,"symbol":227.0278},"th":{"name":90,"symbol":232.0381},"pa":{"name":91,"symbol":231.0359},"u":{"name":92,"symbol":238.029},"np":{"name":93,"symbol":237.0482},"pu":{"name":94,"symbol":244},"am":{"name":95,"symbol":243},"cm":{"name":96,"symbol":247},"bk":{"name":97,"symbol":247},"cf":{"name":98,"symbol":251},"es":{"name":99,"symbol":254},"fm":{"name":100,"symbol":257},"md":{"name":101,"symbol":258},"no":{"name":102,"symbol":259},"lr":{"name":103,"symbol":260}}

class XYZColumbusConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("XYZ ⟷ Columbus Format Converter")
        self.geometry("1000x600")

        # Constants
        self.ANGSTROM_TO_AU = 1.8897259886  # Conversion factor from Angstrom to Atomic Units

        # Setup main frame
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create left panel (XYZ format)
        left_frame = ttk.LabelFrame(main_frame, text="XYZ Format")
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        
        # Create right panel (Columbus format)
        right_frame = ttk.LabelFrame(main_frame, text="Columbus Format")
        right_frame.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
        
        # Middle panel with conversion buttons
        middle_frame = ttk.Frame(main_frame)
        middle_frame.grid(row=0, column=1, sticky="ns", padx=10, pady=5)
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.rowconfigure(0, weight=1)
        
        # XYZ unit selection - Moved to top of left frame
        self.xyz_unit_var = tk.StringVar(value="Angstrom")
        xyz_unit_frame = ttk.Frame(left_frame)
        xyz_unit_frame.pack(fill=tk.X, pady=5)
        ttk.Label(xyz_unit_frame, text="Units:").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(xyz_unit_frame, text="Angstrom", variable=self.xyz_unit_var, value="Angstrom").pack(side=tk.LEFT, padx=5)
        ttk.Radiobutton(xyz_unit_frame, text="Atomic Units", variable=self.xyz_unit_var, value="AU").pack(side=tk.LEFT, padx=5)
        
        # XYZ Editor
        self.xyz_text = tk.Text(left_frame, wrap=tk.NONE)
        self.xyz_text.pack(fill=tk.BOTH, expand=True)
        xyz_scroll_y = ttk.Scrollbar(left_frame, orient="vertical", command=self.xyz_text.yview)
        xyz_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        xyz_scroll_x = ttk.Scrollbar(left_frame, orient="horizontal", command=self.xyz_text.xview)
        xyz_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.xyz_text.configure(yscrollcommand=xyz_scroll_y.set, xscrollcommand=xyz_scroll_x.set)
        
        # Columbus Editor
        self.col_text = tk.Text(right_frame, wrap=tk.NONE)
        self.col_text.pack(fill=tk.BOTH, expand=True)
        col_scroll_y = ttk.Scrollbar(right_frame, orient="vertical", command=self.col_text.yview)
        col_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        col_scroll_x = ttk.Scrollbar(right_frame, orient="horizontal", command=self.col_text.xview)
        col_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
        self.col_text.configure(yscrollcommand=col_scroll_y.set, xscrollcommand=col_scroll_x.set)
        
        # Set up Ctrl+A binding for both text editors
        self.xyz_text.bind("<Control-a>", self.select_all)
        self.col_text.bind("<Control-a>", self.select_all)
        
        # Conversion buttons
        ttk.Button(middle_frame, text="→\nXYZ to Columbus", command=self.xyz_to_columbus).pack(pady=20)
        ttk.Button(middle_frame, text="←\nColumbus to XYZ", command=self.columbus_to_xyz).pack(pady=20)
        
        # File menu
        self.menu_bar = tk.Menu(self)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open XYZ File", command=lambda: self.open_file(self.xyz_text))
        self.file_menu.add_command(label="Open Columbus File", command=lambda: self.open_file(self.col_text))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save XYZ File", command=lambda: self.save_file(self.xyz_text, ".xyz"))
        self.file_menu.add_command(label="Save Columbus File", command=lambda: self.save_file(self.col_text, ""))
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menu_bar)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_var.set("Ready")

    def select_all(self, event):
        """Select all text in the text widget that triggered the event"""
        event.widget.tag_add(tk.SEL, "1.0", tk.END)
        event.widget.mark_set(tk.INSERT, "1.0")
        event.widget.see(tk.INSERT)
        return "break"  # Prevent default behavior

    def open_file(self, text_widget):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                    text_widget.delete(1.0, tk.END)
                    text_widget.insert(tk.END, content)
                self.status_var.set(f"Opened: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to open file: {str(e)}")

    def save_file(self, text_widget, file_type):
        file_path = filedialog.asksaveasfilename(
            defaultextension=file_type,
            filetypes=[("XYZ files", "*.xyz")] if file_type == ".xyz" else [("Columbus files", "*")]
        )
        if file_path:
            try:
                content = text_widget.get(1.0, tk.END)
                with open(file_path, "w") as file:
                    file.write(content)
                self.status_var.set(f"Saved: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {str(e)}")

    def parse_xyz_content(self, xyz_text):
        """Parse XYZ content with better tolerance for format variations"""
        lines = xyz_text.split('\n')
        clean_lines = [line.strip() for line in lines if line.strip()]
        
        if not clean_lines:
            raise ValueError("Empty XYZ content")
        
        atom_lines = []
        start_idx = 0
        
        # Try to determine if first line is atom count
        try:
            num_atoms = int(clean_lines[0])
            # Check if this might be a valid atom count (reasonable range)
            if 1 <= num_atoms <= 1000:
                start_idx = 2  # Skip count and comment lines
                # If there's not enough lines after skipping, adjust
                if len(clean_lines) < start_idx + 1:
                    start_idx = 1  # Maybe there's no comment line
                    
                    # If still not enough lines, try to parse from beginning
                    if len(clean_lines) < start_idx + 1:
                        start_idx = 0
        except ValueError:
            # First line is not an integer, try to detect if it's atom data
            start_idx = 0
        
        # Try to detect comment line if we're starting from the beginning
        if start_idx == 0:
            # Check if first line might be a comment (not starting with element symbol)
            first_word = clean_lines[0].split()[0].lower() if clean_lines else ""

            elements = atomic_data.keys()
            if not any(first_word.lower() == elem for elem in elements) and not first_word.isdigit():
                start_idx = 1  # Skip this line as it's likely a comment
        
        # Collect atom lines and try to parse them
        for line in clean_lines[start_idx:]:
            parts = line.strip().split()
            
            # Check if this line looks like atom data (at least 4 parts: symbol, x, y, z)
            if len(parts) >= 4:
                try:
                    # Try to parse coordinates as float to confirm it's atom data
                    x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                    atom_lines.append(line)
                except ValueError:
                    # Not a valid coordinate line, skip
                    continue
        
        if not atom_lines:
            raise ValueError("No valid atom coordinate lines found in XYZ content")
            
        return atom_lines

    def xyz_to_columbus(self):
        try:
            xyz_text = self.xyz_text.get(1.0, tk.END).strip()
            if not xyz_text:
                messagebox.showerror("Error", "XYZ text area is empty")
                return
            
            try:
                atom_lines = self.parse_xyz_content(xyz_text)
            except ValueError as e:
                messagebox.showerror("Error", str(e))
                return
            
            # Parse XYZ format
            columbus_lines = []
            for i, line in enumerate(atom_lines, 1):
                parts = line.strip().split()
                
                atom_symbol = parts[0]
                # Handle case where atom symbol might include atomic number (e.g., "C1")
                if not any(c.isalpha() for c in atom_symbol):
                    # If no letters, it might be just a number (index)
                    if len(parts) > 1 and any(c.isalpha() for c in parts[1]):
                        atom_symbol = parts[1]
                        x, y, z = float(parts[2]), float(parts[3]), float(parts[4])
                    else:
                        messagebox.showerror("Error", f"Cannot determine atom symbol in line: {line}")
                        return
                else:
                    # Extract only the element symbol (letters) if mixed with numbers
                    element = ''.join(c for c in atom_symbol if c.isalpha())
                    atom_symbol = element
                    x, y, z = float(parts[1]), float(parts[2]), float(parts[3])
                
                # Convert from Angstrom to AU if needed
                if self.xyz_unit_var.get() == "Angstrom":
                    x *= self.ANGSTROM_TO_AU
                    y *= self.ANGSTROM_TO_AU
                    z *= self.ANGSTROM_TO_AU
                
                atom_data = atomic_data.get(atom_symbol.lower())
                if atom_data is None:
                    messagebox.showerror("Error", f"Unknown atom symbol: {atom_symbol}")
                    return
                atom_number = atom_data["name"]
                atom_mass = atom_data["symbol"]

                columbus_lines.append(f"{atom_symbol:<2} {atom_number} {x:15.10f} {y:15.10f} {z:15.10f} {atom_mass}")
            
            self.col_text.delete(1.0, tk.END)
            self.col_text.insert(tk.END, "\n".join(columbus_lines))
            self.status_var.set(f"Converted {len(columbus_lines)} atoms from XYZ to Columbus format")
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")

    def columbus_to_xyz(self):
        try:
            col_text = self.col_text.get(1.0, tk.END).strip()
            if not col_text:
                messagebox.showerror("Error", "Columbus text area is empty")
                return
                
            lines = [line for line in col_text.split('\n') if line.strip()]
            num_atoms = len(lines)
            
            # Parse Columbus format
            xyz_lines = [str(num_atoms), "Converted from Columbus format"]
            
            for line in lines:
                parts = line.strip().split()
                if len(parts) < 5:
                    messagebox.showerror("Error", f"Invalid Columbus line format: {line}")
                    return
                    
                atom_symbol = parts[1]
                x, y, z = float(parts[2]), float(parts[3]), float(parts[4])
                
                # Convert from AU to Angstrom if requested
                if self.xyz_unit_var.get() == "Angstrom":
                    x /= self.ANGSTROM_TO_AU
                    y /= self.ANGSTROM_TO_AU
                    z /= self.ANGSTROM_TO_AU
                
                xyz_lines.append(f"{atom_symbol:<2} {x:15.10f} {y:15.10f} {z:15.10f}")
            
            self.xyz_text.delete(1.0, tk.END)
            self.xyz_text.insert(tk.END, "\n".join(xyz_lines))
            self.status_var.set(f"Converted {num_atoms} atoms from Columbus to XYZ format")
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")

if __name__ == "__main__":
    app = XYZColumbusConverter()
    app.mainloop()