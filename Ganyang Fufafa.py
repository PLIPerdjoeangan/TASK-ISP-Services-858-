import tkinter as tk


class USSDApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USSD Simulator")
        self.geometry("300x400")

        
        self.phone_screen()

    
    def phone_screen(self):
       
        self.clear_window()

        
        label = tk.Label(self, text="*858#", font=("Arial", 18))
        label.pack(pady=20)

       
        phone_button = tk.Button(self, text="📞", font=("Arial", 40), command=self.menu_screen)
        phone_button.pack(pady=10)

   
    def menu_screen(self):
        
        self.clear_window()

        
        menu_label = tk.Label(self, text="Mau iPhone 15Plus dr Saskia Chadwick?\nHub *500*117#", font=("Arial", 14), anchor='w', justify='left')
        menu_label.pack(pady=10, anchor='w')

        
        options_label = tk.Label(self, text="1. Transfer Pulsa\n2. Minta Pulsa\n3. Auto TP\n4. Delete Auto TP\n5. List Auto TP\n6. Cek Kupon Undian TP", font=("Arial", 12), anchor='w', justify='left')
        options_label.pack(pady=10, anchor='w')

      
        self.entry = tk.Entry(self, font=("Arial", 14), width=25)
        self.entry.pack(pady=5)

        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        
        cancel_button = tk.Button(button_frame, text="Cancel", command=self.phone_screen, width=10)
        cancel_button.pack(side=tk.LEFT, padx=10)

        send_button = tk.Button(button_frame, text="Send", command=self.handle_menu_input, width=10)
        send_button.pack(side=tk.LEFT, padx=10)

    
    def transfer_pulsa_screen(self):
       
        self.clear_window()

        
        transfer_label = tk.Label(self, text="Masukkan nomor tujuan Transfer Pulsa\n(contoh: 08xxxx atau 628xxxx)", font=("Arial", 12))
        transfer_label.pack(pady=10)

     
        self.phone_entry = tk.Entry(self, font=("Arial", 14), width=15)
        self.phone_entry.pack(pady=10)

        
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

   
        submit_button = tk.Button(button_frame, text="Submit", command=self.confirm_transfer, width=10)
        submit_button.pack(side=tk.LEFT, padx=5)

        back_button = tk.Button(button_frame, text="Back", command=self.menu_screen, width=10)
        back_button.pack(side=tk.LEFT, padx=5)


    def confirm_transfer(self):
          
        destination_number = self.phone_entry.get()

       
        self.clear_window()

        
        confirmation_label = tk.Label(self, text=f"Pulsa successfully transferred to: {destination_number}", font=("Arial", 12), fg="green", anchor='w', justify='left')
        confirmation_label.pack(pady=20, anchor='w')

       
        back_button = tk.Button(self, text="Back", command=self.phone_screen)
        back_button.pack(pady=10, anchor='w')

   
    def handle_menu_input(self):
        choice = self.entry.get()

        if choice == "1":
           
            self.transfer_pulsa_screen()
        else:
           
            self.phone_screen()

    
    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()


if __name__ == "__main__":  
    app = USSDApp()
    app.mainloop()
