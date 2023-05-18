import os
import subprocess
import tkinter
import tkinter.messagebox
import webbrowser
import customtkinter
# subprocess.call("conda init cmd.exe",shell=True)
# subprocess.call("CALL conda.bat activate gest",shell=True)
# import BasicMode
# import VirtualMouse

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("GEST")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Gesture Detector", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.basic_button = customtkinter.CTkButton(self.sidebar_frame, command=self.basic_mode,text='Basic Mode')
        self.basic_button.grid(row=1, column=0, padx=20, pady=10)
        self.vm_button = customtkinter.CTkButton(self.sidebar_frame, command=self.vm_mode,text='Virtual Mouse Mode')
        self.vm_button.grid(row=2, column=0, padx=20, pady=10)
        self.instr_button = customtkinter.CTkButton(self.sidebar_frame, command=self.instruction)
        self.instr_button.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.exit_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),text='Exit',command=self.destroy)
        self.exit_button.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.basic_act_button = customtkinter.CTkButton(master=self,text="Activate Basic Mode",command=self.basic_mode_act,width=120,height=32,font=("",20))
        #self.basic_act_button.grid(row=2,column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.vm_act_button = customtkinter.CTkButton(master=self,text="Activate Virtual Mouse",command=self.virtual_mouse_act,width=120,height=32,font=("",20))
        #self.vm_act_button.grid(row=2,column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=700)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        self.note = customtkinter.CTkTextbox(self,width=500,height=50)
        self.note.grid(row=3, column=1, padx=(20, 0), pady=(10, 20), sticky="nsew")

        self.instr_button.configure(text="Instruction Manual")
        self.appearance_mode_optionemenu.set("Dark")
        self.textbox.insert("0.0",'''
        
        Welcome to Gesture Detector

        GEST is a Human Computer Interaction(HCI) software that aims to provide contactless HCI experience to the user. 
        
        With GEST, you can perform basic system functions on the go and without the hassle of clicking away to find the 
        required setting. 

        GEST also provides you with a virtual mouse mode that completely emulates the behaviour of the traditional mouse 
        with all the key functionalities.
        
        
        ''')
        self.textbox.configure(state =tkinter.DISABLED)
        self.note.insert("0.0","Note:\n" + "It is recommended to use the Instruction Manual to understand all gestures and associated functionalities before usage")
        self.note.configure(state= tkinter.DISABLED)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def sidebar_button_event(self):
        print("sidebar_button click")

    def basic_mode(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0","end")
        
        self.textbox.insert("0.0",
                            '''Basic Mode

    Basic mode provides assistance functionalities that allow you to perform some basic system operations as you go. 
    The functionalities included are as follows:

        •	Opening web browser
        •	Play / Pause / Resume / Stop Music
        •	Adjust system volume
        •	Adjust system brightness
        •	Horizontal/Vertical scrolling
        •	Quit mode

        To see the gestures associated with the above functions, please refer to the Instruction manual.

        ''')

        self.textbox.configure(state="disabled")
        self.vm_act_button.grid_forget()
        self.basic_act_button.grid(row=2,column=1, padx=(50, 20), pady=(20, 50), sticky="nsew")

    def vm_mode(self):
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0","end")
        self.textbox.insert("0.0",'''Virtual Mouse Mode

    Virtual mouse mode allows you to completely control the mouse pointer using hand gestures. 
    The functionalities included are as follows:
        •	Left click
        •	Right click
        •	Double click (left)
        •	Drag and Drop
        •	Multiple Select
        •	Horizontal/Vertical Scroll
        •	Quit mode

        To see the gestures associated with the above functions, please refer to the Instruction manual.

        ''')
        self.textbox.configure(state="disabled")
        self.basic_act_button.grid_forget()
        self.vm_act_button.grid(row=2,column=1, padx=(50, 20), pady=(20, 50), sticky="nsew")

    def basic_mode_act(self):
        return os.system("conda run -n gest python BasicMode.py")

    def virtual_mouse_act(self):
        return os.system("conda run -n gest python VirtualMouse.py")

    def instruction(self):
        return webbrowser.open_new(r"Instruction Manual.pdf")


if __name__ == "__main__":
    app = App()
    app.mainloop()