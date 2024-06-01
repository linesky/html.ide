import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import subprocess
import shutil
import os



class BareboneBuilder:
    def __init__(self, root):
        self.root = root
        self.root.title("zip")

        # Janela amarela
        self.root.configure(bg='yellow')

        # Área de texto
        self.text_area = tk.Text(self.root, height=10, width=50,bg='yellow')
        self.text_area.pack(pady=10)

        # Botões
        self.build_button = tk.Button(self.root, text="Build", command=self.build_kernel, bg='yellow')
        self.build_button.pack(pady=5)

        
    def execute_command(self, command,show:bool):
        try:
            
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True, text=True)
            self.text_area.insert(tk.END, result)
        except subprocess.CalledProcessError as e:
            if show:
                self.text_area.insert(tk.END,f"Error executing command:\n{e.output}")

    def build_kernel(self):
        filename = tk.filedialog.askopenfilename(title="Select file")
        self.text_area.delete(1.0, tk.END)
        
        
        self.execute_command('cp $filename $filename.bak'.replace("$filename",filename),True)
        files:str=filename.split("/")
        if len(files)>0:
            filename=files[len(files)-1]
        self.text_area.insert(tk.END,"build ... "+filename+"\n")
        self.execute_command('zip -r $filename.zip $filename'.replace("$filename",filename),True)
        
        
    
            


if __name__ == "__main__":
    root = tk.Tk()
    builder = BareboneBuilder(root)
    root.mainloop()
