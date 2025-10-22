from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class BancoVirtual:
    def __init__(self, root):
        self.root = root
        self.root.title("Banco Virtual")
        self.root.geometry("400x500")
        
        # Variables
        self.saldo = 1000.00  # Saldo inicial
        self.saldo_var = StringVar()
        self.saldo_var.set(f"${self.saldo:.2f}")
        
        # Frame principal
        mainframe = ttk.Frame(root, padding="20 20 20 20")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        
        # Título
        ttk.Label(mainframe, text="Banco Virtual", font=("Arial", 20, "bold")).grid(column=0, row=0, columnspan=2, pady=20)
        
        # Saldo
        ttk.Label(mainframe, text="Saldo Actual:", font=("Arial", 12)).grid(column=0, row=1, sticky=W)
        ttk.Label(mainframe, textvariable=self.saldo_var, font=("Arial", 12, "bold")).grid(column=1, row=1, sticky=W)
        
        # Frame para operaciones
        operaciones_frame = ttk.LabelFrame(mainframe, text="Operaciones", padding="10 10 10 10")
        operaciones_frame.grid(column=0, row=2, columnspan=2, pady=20, sticky=(W, E))
        
        # Monto
        ttk.Label(operaciones_frame, text="Monto:").grid(column=0, row=0, sticky=W)
        self.monto = StringVar()
        ttk.Entry(operaciones_frame, textvariable=self.monto, width=15).grid(column=1, row=0, padx=5)
        
        # Botones
        ttk.Button(operaciones_frame, text="Depositar", command=self.depositar).grid(column=0, row=1, pady=10)
        ttk.Button(operaciones_frame, text="Retirar", command=self.retirar).grid(column=1, row=1, pady=10)
        
        # Historial
        ttk.Label(mainframe, text="Historial de Transacciones:", font=("Arial", 12)).grid(column=0, row=3, columnspan=2, pady=10)
        self.historial = Text(mainframe, height=8, width=40)
        self.historial.grid(column=0, row=4, columnspan=2)
        
        # Configurar el grid
        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
    
    def depositar(self):
        try:
            monto = float(self.monto.get())
            if monto <= 0:
                messagebox.showerror("Error", "El monto debe ser mayor a 0")
                return
            self.saldo += monto
            self.saldo_var.set(f"${self.saldo:.2f}")
            self.historial.insert(END, f"Depósito: +${monto:.2f}\n")
            self.monto.set("")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido")
    
    def retirar(self):
        try:
            monto = float(self.monto.get())
            if monto <= 0:
                messagebox.showerror("Error", "El monto debe ser mayor a 0")
                return
            if monto > self.saldo:
                messagebox.showerror("Error", "Saldo insuficiente")
                return
            self.saldo -= monto
            self.saldo_var.set(f"${self.saldo:.2f}")
            self.historial.insert(END, f"Retiro: -${monto:.2f}\n")
            self.monto.set("")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un monto válido")

if __name__ == "__main__":
    root = Tk()
    app = BancoVirtual(root)
    root.mainloop() 