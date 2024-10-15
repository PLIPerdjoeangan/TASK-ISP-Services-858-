import tkinter as tk

# Main application class to handle the different scenes
class USSDApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USSD Simulator")
        self.geometry("300x400")

        # Create scenes
        self.phone_screen()

    # Scene 1: Phone screen with *858# and a phone button
    def phone_screen(self):
        # Clear the window
        self.clear_window()

        # Label with *858#
        label = tk.Label(self, text="*858#", font=("Arial", 18))
        label.pack(pady=20)

        # Phone button
        phone_button = tk.Button(self, text="📞", font=("Arial", 40), command=self.menu_screen)
        phone_button.pack(pady=10)

    # Scene 2: USSD menu screen
    def menu_screen(self):
        # Clear the window
        self.clear_window()

        # USSD menu label (aligned to the left)
        menu_label = tk.Label(self, text="Mau iPhone 15Plus dr Saskia Chadwick?\nHub *500*117#", font=("Arial", 14), anchor='w', justify='left')
        menu_label.pack(pady=10, anchor='w')

        # USSD options (aligned to the left)
        options_label = tk.Label(self, text="1. Transfer Pulsa\n2. Minta Pulsa\n3. Auto TP\n4. Delete Auto TP\n5. List Auto TP\n6. Cek Kupon Undian TP", font=("Arial", 12), anchor='w', justify='left')
        options_label.pack(pady=10, anchor='w')

        # Single-line Entry field
        self.entry = tk.Entry(self, font=("Arial", 14), width=25)
        self.entry.pack(pady=5)

        # Create a frame for the Cancel and Send buttons
        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)

        # Cancel and Send buttons side by side
        cancel_button = tk.Button(button_frame, text="Cancel", command=self.phone_screen, width=10)
        cancel_button.pack(side=tk.LEFT, padx=10)

        send_button = tk.Button(button_frame, text="Send", command=self.handle_menu_input, width=10)
        send_button.pack(side=tk.LEFT, padx=10)

    # Scene 3: Transfer Pulsa screen (no new window, everything stays in the same window)
    def transfer_pulsa_screen(self):
        # Clear the window
        self.clear_window()

        # Ask for the destination number directly in the same window
        transfer_label = tk.Label(self, text="Masukkan nomor tujuan Transfer Pulsa\n(contoh: 08xxxx atau 628xxxx)", font=("Arial", 12))
        transfer_label.pack(pady=10)

        # Entry to accept the phone number
        self.phone_entry = tk.Entry(self, font=("Arial", 14), width=15)
        self.phone_entry.pack(pady=10)

        # Create a frame for the Submit and Back buttons in the Transfer Pulsa scene
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # Submit and Back buttons side by side
        submit_button = tk.Button(button_frame, text="Submit", command=self.confirm_transfer, width=10)
        submit_button.pack(side=tk.LEFT, padx=5)

        back_button = tk.Button(button_frame, text="Back", command=self.menu_screen, width=10)
        back_button.pack(side=tk.LEFT, padx=5)

    # Confirmation of Transfer Pulsa
    def confirm_transfer(self):
          # Get the entered phone number
        destination_number = self.phone_entry.get()

        # Clear the window
        self.clear_window()

        # Display confirmation message (aligned to the left)
        confirmation_label = tk.Label(self, text=f"Pulsa successfully transferred to: {destination_number}", font=("Arial", 12), fg="green", anchor='w', justify='left')
        confirmation_label.pack(pady=20, anchor='w')

        # Button to go back to the phone screen (aligned to the left)
        back_button = tk.Button(self, text="Back", command=self.phone_screen)
        back_button.pack(pady=10, anchor='w')

    # Handle the user input from the USSD menu
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
