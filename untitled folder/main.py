import customtkinter
from subprocess import run

# PasswordPaladin
# By: Jason Ngu & Alfred Zhu

# initial setup
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

# application
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("PasswordPaladin | Password Checker & Generator")
app.geometry("480x360")
app.resizable(False, False)

# application frame
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=5, padx=5, fill="both", expand=True)

# application name titleLabel
titleLabel = customtkinter.CTkLabel(master=frame, text="PasswordPaladin", font=("OpenSans", 32))
titleLabel.pack(pady=5, padx=5)

titleLabel = customtkinter.CTkLabel(master=frame, text="Password Checker and Generator", font=("OpenSans", 14))
titleLabel.pack(pady=0, padx=5)

def launchGenerator():
    run(["python", "PasswordGenerator.py"])

def launchChecker():
    run(["python", "PasswordChecker.py"])


infoText = "Please select between the two options to continue to their respective programs."
titleLabel = customtkinter.CTkTextbox(master=frame, height=50, width=350, border_width=0, wrap="word", font=("OpenSans", 14), fg_color="#2b2b2b")
titleLabel.insert("0.0", text=infoText)
titleLabel.configure(state="disabled")
titleLabel.pack(pady=5, padx=5)

checkerButton = customtkinter.CTkButton(frame, text="Launch Password Checker", font=("OpenSans", 14), width=350, height=50, command=launchChecker)
checkerButton.pack(pady=10, padx=10)

generatorButton = customtkinter.CTkButton(frame, text="Launch Password Generator", font=("OpenSans", 14), width=350, height=50, command=launchGenerator)
generatorButton.pack(pady=10, padx=10)

nameLabel = customtkinter.CTkLabel(master=frame, text="Jason Ngu & Alfred Zhu 2023", font=("OpenSans", 9))
nameLabel.pack(pady=20, padx=0)

app.mainloop()
