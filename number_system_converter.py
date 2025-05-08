import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class NumberSystemConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Number System Converter")
        self.root.geometry("500x700")
        self.root.configure(bg='#f0f2f5')
        self.root.option_add("*Font", "Segoe 10")
        
        # Center window on screen
        self.center_window()

        # Style configuration
        self.setup_styles()
        
        # Main container with fixed width for better centering
        outer_container = ttk.Frame(root, style='TFrame')
        outer_container.pack(fill='both', expand=True)
        
        main_container = ttk.Frame(outer_container, style='TFrame', padding=15, width=450)
        main_container.pack(pady=10, fill='y', expand=True)
        
        # Title
        ttk.Label(main_container, text="Number System Converter", 
                 font=('Segoe UI', 16, 'bold')).pack(anchor='center', pady=(0, 20))
        
        # Create and setup UI components
        self.create_input_card(main_container)
        self.create_results_card(main_container)
        self.create_calculator_card(main_container)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles for all widgets
        style.configure('TFrame', background='#f0f2f5')
        style.configure('TLabel', background='#f0f2f5', font=('Segoe UI', 10))
        style.configure('Header.TLabel', background='#f0f2f5', font=('Segoe UI', 12, 'bold'))
        style.configure('TEntry', font=('Consolas', 11))
        style.configure('TButton', font=('Segoe UI', 10))
        style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'))
        style.configure('TCombobox', font=('Segoe UI', 10))
        style.configure('Card.TFrame', background='#ffffff')

    def create_input_card(self, parent):
        # Input Card
        input_card = ttk.Frame(parent, style='Card.TFrame', padding=15)
        input_card.pack(fill='x', pady=10)
        self.add_shadow_to_frame(input_card)
        
        ttk.Label(input_card, text="INPUTS", style='Header.TLabel').pack(anchor='w', pady=(0, 10))
        
        # Input 1
        input1_frame = ttk.Frame(input_card, style='Card.TFrame')
        input1_frame.pack(fill='x', pady=5)
        
        ttk.Label(input1_frame, text="Value 1:", width=8).pack(side='left', padx=5)
        self.number_entry1 = ttk.Entry(input1_frame, width=20, font=('Consolas', 11))
        self.number_entry1.insert(0, "Enter number")
        self.number_entry1.bind("<FocusIn>", lambda e: self.clear_placeholder(self.number_entry1, "Enter number"))
        self.number_entry1.bind("<FocusOut>", lambda e: self.restore_placeholder(self.number_entry1, "Enter number"))
        self.number_entry1.pack(side='left', padx=5)
        
        ttk.Label(input1_frame, text="Base:").pack(side='left', padx=5)
        self.input_base1 = ttk.Combobox(input1_frame, values=["Decimal", "Binary", "Octal", "Hexadecimal"], width=12)
        self.input_base1.set("Decimal")
        self.input_base1.pack(side='left', padx=5)
        
        # Input 2
        input2_frame = ttk.Frame(input_card, style='Card.TFrame')
        input2_frame.pack(fill='x', pady=5)
        
        ttk.Label(input2_frame, text="Value 2:", width=8).pack(side='left', padx=5)
        self.number_entry2 = ttk.Entry(input2_frame, width=20, font=('Consolas', 11))
        self.number_entry2.insert(0, "Enter number")
        self.number_entry2.bind("<FocusIn>", lambda e: self.clear_placeholder(self.number_entry2, "Enter number"))
        self.number_entry2.bind("<FocusOut>", lambda e: self.restore_placeholder(self.number_entry2, "Enter number"))
        self.number_entry2.pack(side='left', padx=5)
        
        ttk.Label(input2_frame, text="Base:").pack(side='left', padx=5)
        self.input_base2 = ttk.Combobox(input2_frame, values=["Decimal", "Binary", "Octal", "Hexadecimal"], width=12)
        self.input_base2.set("Decimal")
        self.input_base2.pack(side='left', padx=5)
        
        # Output Base
        output_frame = ttk.Frame(input_card, style='Card.TFrame')
        output_frame.pack(fill='x', pady=10)
        
        ttk.Label(output_frame, text="Convert to:").pack(side='left', padx=5)
        self.convert_base = ttk.Combobox(output_frame, values=["Decimal", "Binary", "Octal", "Hexadecimal"], width=12)
        self.convert_base.set("Binary")
        self.convert_base.pack(side='left', padx=5)
        
        convert_button = ttk.Button(output_frame, text="Convert", command=self.convert, style='Accent.TButton')
        convert_button.pack(side='right', padx=10)
    
    def create_results_card(self, parent):
        # Results Card
        results_card = ttk.Frame(parent, style='Card.TFrame', padding=15)
        results_card.pack(fill='x', pady=10)
        self.add_shadow_to_frame(results_card)
        
        ttk.Label(results_card, text="RESULTS", style='Header.TLabel').pack(anchor='w', pady=(0, 10))
        
        # Results container
        results_container = ttk.Frame(results_card, style='Card.TFrame')
        results_container.pack(fill='x')
        
        # Left Result
        left_result_frame = ttk.Frame(results_container, style='Card.TFrame')
        left_result_frame.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        ttk.Label(left_result_frame, text="Value 1:").pack(anchor='w', padx=5, pady=(0, 5))
        left_border = tk.Frame(left_result_frame, bd=1, relief="solid", bg="#e6e6e6")
        left_border.pack(fill='x', padx=5, pady=5)
        
        self.left_result = ttk.Label(left_border, text="", font=('Consolas', 12), background='#f0f0f0')
        self.left_result.pack(fill='x', ipady=8, ipadx=8)
        
        # Right Result
        right_result_frame = ttk.Frame(results_container, style='Card.TFrame')
        right_result_frame.pack(side='right', fill='x', expand=True, padx=(5, 0))
        
        ttk.Label(right_result_frame, text="Value 2:").pack(anchor='w', padx=5, pady=(0, 5))
        right_border = tk.Frame(right_result_frame, bd=1, relief="solid", bg="#e6e6e6")
        right_border.pack(fill='x', padx=5, pady=5)
        
        self.right_result = ttk.Label(right_border, text="", font=('Consolas', 12), background='#f0f0f0')
        self.right_result.pack(fill='x', ipady=8, ipadx=8)
    
    def create_calculator_card(self, parent):
        # Calculator Card
        calc_card = ttk.Frame(parent, style='Card.TFrame', padding=15)
        calc_card.pack(fill='x', pady=10)
        self.add_shadow_to_frame(calc_card)
        
        ttk.Label(calc_card, text="CALCULATOR", style='Header.TLabel').pack(anchor='w', pady=(0, 10))
        
        # Button container
        buttons_container = ttk.Frame(calc_card, style='Card.TFrame')
        buttons_container.pack(anchor='center', pady=5)
        
        # Calculator buttons
        self.create_calc_button(buttons_container, "+", self.calculate_add)
        self.create_calc_button(buttons_container, "−", self.calculate_subtract)
        self.create_calc_button(buttons_container, "×", self.calculate_multiply)
        self.create_calc_button(buttons_container, "÷", self.calculate_divide)
        
        # Calculator result
        calc_result_frame = ttk.Frame(calc_card, style='Card.TFrame')
        calc_result_frame.pack(fill='x', pady=10)
        
        ttk.Label(calc_result_frame, text="Result:").pack(anchor='w', padx=5, pady=(0, 5))
        calc_border = tk.Frame(calc_result_frame, bd=1, relief="solid", bg="#e6e6e6")
        calc_border.pack(fill='x', padx=5, pady=5)
        
        self.calc_result = ttk.Label(calc_border, text="", font=('Consolas', 12), background='#f0f0f0')
        self.calc_result.pack(fill='x', ipady=8, ipadx=8)

    def center_window(self):
        """Center the window on the screen."""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def add_shadow_to_frame(self, frame):
        """Add a shadow effect to frames for better appearance."""
        frame.configure(borderwidth=1, relief="solid")
        frame['padding'] = (15, 15, 15, 15)

    def create_calc_button(self, parent, text, command):
        btn = tk.Button(
            parent,
            text=text,
            font=('Segoe UI', 12, 'bold'),
            width=3,
            height=1,
            bg='#4a86e8',
            fg='white',
            relief='flat',
            command=command
        )
        btn.pack(side='left', padx=10, pady=5)
        
        # Add hover effect
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg='#3a76d8'))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg='#4a86e8'))

    def clear_placeholder(self, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    def restore_placeholder(self, entry, placeholder):
        if not entry.get():
            entry.insert(0, placeholder)

    def convert(self):
        try:
            # Get and validate inputs
            input_num1 = self.number_entry1.get().strip()
            input_num2 = self.number_entry2.get().strip()
            
            if input_num1 == "Enter number":
                messagebox.showerror("Error", "Please enter a number in Value 1")
                return
                
            if input_num2 == "Enter number":
                messagebox.showerror("Error", "Please enter a number in Value 2")
                return
            
            # Get selected bases
            base1 = self.input_base1.get()
            base2 = self.input_base2.get()
            target_base = self.convert_base.get()
                
            # Convert inputs to decimal
            decimal1 = self.to_decimal(input_num1, base1)
            decimal2 = self.to_decimal(input_num2, base2)

            # Convert decimals to target base
            result1 = self.from_decimal(decimal1, target_base)
            result2 = self.from_decimal(decimal2, target_base)

            # Display results
            self.left_result.config(text=result1)
            self.right_result.config(text=result2)

        except ValueError:
            messagebox.showerror("Error", "Invalid input number for the selected base")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def to_decimal(self, value, base):
        """Convert a value from given base to decimal"""
        if base == "Decimal":
            return int(value)
        elif base == "Binary":
            return int(value, 2)
        elif base == "Octal":
            return int(value, 8)
        elif base == "Hexadecimal":
            return int(value, 16)
    
    def from_decimal(self, decimal, target_base):
        """Convert a decimal value to target base"""
        if target_base == "Decimal":
            return str(decimal)
        elif target_base == "Binary":
            return bin(decimal)[2:].zfill(4)
        elif target_base == "Octal":
            return oct(decimal)[2:]
        elif target_base == "Hexadecimal":
            return hex(decimal)[2:].upper()

    def get_numbers(self):
        try:
            # Get the converted values from result fields
            num1 = self.left_result.cget("text").strip()
            num2 = self.right_result.cget("text").strip()
            
            if not num1 or not num2:
                messagebox.showerror("Error", "Please convert the numbers first")
                return None, None
                
            # Get the target base and convert
            base = self.convert_base.get()
            n1 = self.to_decimal(num1, base)
            n2 = self.to_decimal(num2, base)
                
            return n1, n2
            
        except ValueError:
            messagebox.showerror("Error", "Invalid numbers in result fields")
            return None, None
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None, None

    def show_result(self, result):
        try:
            target_base = self.convert_base.get()
            result_str = self.from_decimal(int(result), target_base)
            self.calc_result.config(text=result_str)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calculate_add(self):
        n1, n2 = self.get_numbers()
        if n1 is not None and n2 is not None:
            self.show_result(n1 + n2)
            
    def calculate_subtract(self):
        n1, n2 = self.get_numbers()
        if n1 is not None and n2 is not None:
            self.show_result(n1 - n2)
            
    def calculate_multiply(self):
        n1, n2 = self.get_numbers()
        if n1 is not None and n2 is not None:
            self.show_result(n1 * n2)
            
    def calculate_divide(self):
        n1, n2 = self.get_numbers()
        if n1 is not None and n2 is not None:
            try:
                self.show_result(n1 / n2)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero!")

if __name__ == "__main__":
    root = tk.Tk()
    app = NumberSystemConverter(root)
    root.mainloop() 