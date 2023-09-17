import string
from string import *
import random
import customtkinter
import tkinter
import pyperclip

# CPSC 329 W23 PasswordGenerator.py
# Jason Ngu & Alfred Zhu

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '~', '`', '{', '}', '[', ']']
specialChars = "\"!@#$%^&*()[]{}~`-+?_=,<>\\/"

int_numOfSelected = 0
bool_generate = False
bool_requestAddLetters = False
bool_requestLower = False
bool_requestUpper = False
bool_requestDigits = False
bool_requestSpecial = False
bool_requestDict = False
bool_requestMemorable = False

def generatePassword(int_requestLength):
    additionalNotesLabel.configure(state="normal")
    additionalNotesLabel.configure(text="Note: No Additional Notes at this time")

    if (bool_requestLower == True or bool_requestUpper == True) and (bool_requestDict == False and bool_requestAddLetters == False):
        generalResultsLabel.configure(text="Password Output | ERROR")
        additionalNotesLabel.configure(text="ERROR: Cannot have uppercase/lowercase without any letters to begin with.")
        return ""

    if (int_requestLength > 48):
        generalResultsLabel.configure(text="Password Output | ERROR")
        additionalNotesLabel.configure(text="ERROR: Cannot generate password of length > 48.")
        return ""

    elif (int_numOfSelected == 1 and bool_requestMemorable == True):
        generalResultsLabel.configure(text="Password Output | ERROR")
        additionalNotesLabel.configure(text="ERROR: More than just the Memorable Radio Button must be selected.")
        return ""

    elif (int_requestLength < 8):
        generalResultsLabel.configure(text="Password Output | ERROR")
        additionalNotesLabel.configure(text="ERROR: Requested Length Must be 8 Minimum.")
        return ""

    # function to insert random word into the random jargle of info made
    def insertString(original, insert):
        index = random.randint(0, len(original))
        return original[:index] + insert + original[index:]

    # function to get random word from dictionary
    def getRandWord(requestedLength):
        lines = open('words_alpha.txt').read().splitlines()
        wordLoop = True

        while wordLoop:
            obtainedWord = random.choice(lines)

            if len(obtainedWord) == requestedLength:
                return obtainedWord

            else:
                wordLoop = True

    if (bool_generate == False):
        additionalNotesLabel.configure(text="ERROR: No Radio Buttons Have Been Selected")
        generalResultsLabel.configure(text="Password Output | ERROR")
        return ""

    else:
        generateLoop = True

    while generateLoop == True:

        remainingLength = int_requestLength
        randomWord = "N/A"
        appendVal = ""

        reLoopCondition = False
        bool_containsLowercase = False
        bool_containsUppercase = False
        bool_containsDigit = False
        bool_containsSpecialChar = False

        int_randLetters = 0
        int_randDigits = 0
        int_randSpecial = 0
        int_randWord = 0

        if bool_requestLower == True or bool_requestUpper == True:
            test = True
        else:
            test = False

        # if random word is requested
        if bool_requestDict == True:

            if int_numOfSelected == 1:
                additionalNotesLabel.configure(text="ERROR: Cannot generate a word without upperase or lowercase")
                generalResultsLabel.configure(text="Password Output | ERROR")
                return ""

            if bool_requestLower == False and bool_requestUpper == False:
                additionalNotesLabel.configure(text="ERROR: Cannot generate a word without upperase or lowercase")
                generalResultsLabel.configure(text="Password Output | ERROR")
                return ""

            if int_requestLength < 25:
                int_randWord = int_requestLength
            elif (int_requestLength > 25 and bool_requestAddLetters == False and bool_requestSpecial == False and bool_requestDigits == False):
                additionalNotesLabel.configure(text="ERROR: Cannot generate a lone dictionary word over length 24")
                generalResultsLabel.configure(text="Password Output | ERROR")
                return ""

            if (int_requestLength <= 11):
                int_randWord = random.randint(3, 6)

            elif (11 < int_requestLength <= 20):
                int_randWord = random.randint(6, 10)

            elif (20 < int_requestLength <= 40):
                int_randWord = random.randint(8, 12)

            elif (40 < int_requestLength < 60):
                int_randWord = random.randint(11, 16)

            else:
                int_randWord = random.randint(16, 24)

            if int_numOfSelected == 2 and test == True:
                int_randWord = int_requestLength

            elif int_numOfSelected == 3 and bool_requestUpper == True and bool_requestLower == True:
                int_randWord = int_requestLength

            randomWord = getRandWord(int_randWord)

            if (bool_requestLower == False):
                randomWord = randomWord.upper()
            elif (bool_requestUpper == False):
                randomWord = randomWord.lower()

            if (bool_requestLower == True and bool_requestUpper == True and bool_requestAddLetters == False):

                num_uppercase = random.randint(1, len(randomWord))

                # Choose random indices to uppercase
                uppercase_indices = random.sample(range(len(randomWord)), num_uppercase)

                # Convert the characters to uppercase
                result = ""
                for i, c in enumerate(randomWord):
                    if i in uppercase_indices:
                        result += c.upper()
                    else:
                        result += c

                randomWord = result

            remainingLength -= len(randomWord)

        # if random letters are requested
        if bool_requestAddLetters == True:

            if (int_numOfSelected == 2):
                int_randLetters = int_requestLength
            else:
                int_randLetters = random.randint(2, remainingLength)
                remainingLength -= int_randLetters

                if remainingLength <= 2:
                    remainingLength = random.randint(3, 6)

            for indice in range(int_randLetters):
                appendVal += random.choice(string.ascii_letters)

            if bool_requestLower == False:
                appendVal = appendVal.upper()

            elif bool_requestUpper == False:
                appendVal = appendVal.lower()

        # if random digits are requested
        if bool_requestDigits == True:

            if int_numOfSelected == 1:
                int_randDigits = int_requestLength
            else:
                int_randDigits = random.randint(2, remainingLength)
                remainingLength -= int_randDigits

                if remainingLength <= 2:
                    remainingLength = random.randint(3, 6)

            for indice in range(int_randDigits):
                appendVal += random.choice(numbers)

        # if random special characters are requested
        if bool_requestSpecial == True:

            if int_numOfSelected == 1:
                int_randSpecial = int_requestLength
            else:
                int_randSpecial = remainingLength
                remainingLength -= remainingLength

            for indice in range(int_randSpecial):
                appendVal += random.choice(symbols)

        mixup = list(appendVal)
        random.shuffle(mixup)
        result = ''.join(mixup)

        if bool_requestDict == True:
            if bool_requestMemorable == False:
                result = result[0:int_requestLength-len(randomWord)]
                password = insertString(result, randomWord)
            else:
                result = result[0:int_requestLength-len(randomWord)]
                password = randomWord + result
        else:
            if bool_requestMemorable == False:
                result = result[0:int_requestLength]
                password = result
            else:
                password = appendVal[0:int_requestLength]

    # For loop to check every character 0 < x < length
        for indice in range (0, len(password)):
            currentInd = password[indice]

            if (currentInd.islower() == True):
                bool_containsLowercase = True

            # checking if current indice is uppercase
            if (currentInd.isupper() == True):
                bool_containsUppercase = True

            # checking if current indice is a digit 0-9
            elif (currentInd.isdigit() == True):
                bool_containsDigit = True

            elif (any(j in specialChars for j in currentInd)):
                bool_containsSpecialChar = True
        # end of for loop

        if (len(password) != int_requestLength):
            reLoopCondition = True

        if bool_requestLower == True:
            if bool_containsLowercase == False:
                reLoopCondition = True

        if bool_requestUpper == True:
            if bool_containsUppercase == False:
                reLoopCondition = True

        if bool_requestDigits == True:
            if bool_containsDigit == False:
                reLoopCondition = True

        if bool_requestSpecial == True:
            if bool_containsSpecialChar == False:
                reLoopCondition = True

        if reLoopCondition == True:
            generateLoop = True
        else:

            if randomWord != "N/A":
                text = "Password Output | Random Word: \"" + randomWord.lower() + "\""
            else:
                text = "Password Output | No Random Word"
            generalResultsLabel.configure(text=text)
            return password

def printPassword(int_requestLength):
    output = generatePassword(int_requestLength)
    outputLabel.configure(text=output)

    if output == "":
        return -1
    else:
        return 0

def generatePass():

    try:
        userInput = int(inputBox.get("1.0", 'end-1c'))
    except:
        generalResultsLabel.configure(text="Password Output | ERROR")
        additionalNotesLabel.configure(text="ERROR: Invalid Length Input, please try again.")
    else:
        output = printPassword(userInput)

        if output == 0:
            if (bool_requestDict == True and bool_requestMemorable == True):
                additionalNotesLabel.configure(text="Note: Request for a dictionary word and memorable password makes password weaker.")
            elif (bool_requestDict == True):
                additionalNotesLabel.configure(text="Note: Request for a dictionary word may make the password weaker")
            elif (bool_requestMemorable == True):
                additionalNotesLabel.configure(text="Note: Request for a memorable password makes password weaker")
            elif (userInput < 12):
                additionalNotesLabel.configure(text="Note: Length of password could be a weakness")
            else:
                additionalNotesLabel.configure(text="Now that's a strong password, now comes the challenge of remembering it...")


# GUI CODE
# initial setup
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

# application
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("CPSC 329 W23 | Password Generator")
app.geometry("640x640")
app.resizable(False, False)

# application frame
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=5, padx=5, fill="both", expand=True)

# application name titleLabel
titleLabel = customtkinter.CTkLabel(master=frame, text="CPSC 329 W23 | Password Generator", font=("OpenSans", 20))
titleLabel.pack(pady=5, padx=5)

# titleLabel test
infoText = "The following is an application which takes in a user-inputted password, and checks it under variety of tests to see if it passes a basic checkup, minimum requirements check, and additional advanced test cases. For additional info, please read the provided PDF for additional documentation."
infoText = "The following application is an application which takes in specific user requests to generate unique passwords to suit their specific needs via radio buttons + requested length."
titleLabel = customtkinter.CTkTextbox(master=frame, height=60, width=550, wrap="word", border_width=0, font=("OpenSans", 12), fg_color="#2b2b2b")
titleLabel.insert("0.0", text=infoText)
titleLabel.configure(state="disabled")
titleLabel.pack(pady=5, padx=5)

rvarDictionary = tkinter.IntVar(app, 0)
rvarAddLetters = tkinter.IntVar(app, 0)
rvarUppercase = tkinter.IntVar(app, 0)
rvarLowercase = tkinter.IntVar(app, 0)
rvarDigits = tkinter.IntVar(app, 0)
rvarSpecial = tkinter.IntVar(app, 0)
rvarMemorable = tkinter.IntVar(app, 0)

def enableDictionary():
    if rvarDictionary.get() == 1:
        global int_numOfSelected
        global bool_generate
        global bool_requestDict
        bool_generate= True
        bool_requestDict = True
        int_numOfSelected += 1

def enableAddLetters():
    if rvarAddLetters.get() == 1:
        global int_numOfSelected
        global bool_generate
        global bool_requestAddLetters
        bool_generate= True
        bool_requestAddLetters = True
        int_numOfSelected += 1

def enableUppercase():
    if rvarUppercase.get() == 1:
        global int_numOfSelected
        global bool_generate
        global bool_requestUpper
        bool_generate= True
        bool_requestUpper = True
        int_numOfSelected += 1

def enableLowercase():
    if rvarLowercase.get() == 1:
        global int_numOfSelected
        global bool_generate
        global bool_requestLower
        bool_generate= True
        bool_requestLower = True
        int_numOfSelected += 1

def enableDigits():
    if rvarDigits.get() == 1:
        global int_numOfSelected
        global bool_generate
        global bool_requestDigits
        bool_generate= True
        bool_requestDigits = True
        int_numOfSelected += 1

def enableSpecial():
    if rvarSpecial.get() == 1:
        global int_numOfSelected
        global bool_generate
        global bool_requestSpecial
        bool_generate = True
        bool_requestSpecial = True
        int_numOfSelected += 1

def enableMemorable():
    if rvarMemorable.get() == 1:
        global int_numOfSelected
        global bool_generate
        global bool_requestMemorable
        bool_generate = True
        bool_requestMemorable = True
        int_numOfSelected += 1

button_dictionary = customtkinter.CTkRadioButton(master=frame, radiobutton_height=15, radiobutton_width=15, text="Contains Dictionary Word", command=enableDictionary, variable= rvarDictionary, value=1)
button_dictionary.pack(padx=200, pady=1)
button_addLetters = customtkinter.CTkRadioButton(master=frame, radiobutton_height=15, radiobutton_width=15, text="Contains Additional Letters", command=enableAddLetters, variable= rvarAddLetters, value=1)
button_addLetters.pack(padx=200, pady=1)
button_uppercase = customtkinter.CTkRadioButton(master=frame, radiobutton_height=15, radiobutton_width=15, text="Contains Uppercase Letters", command=enableUppercase, variable= rvarUppercase, value=1)
button_uppercase.pack(padx=200, pady=1)
button_lowercase = customtkinter.CTkRadioButton(master=frame, radiobutton_height=15, radiobutton_width=15, text="Contains Lowercase Letters", command=enableLowercase, variable= rvarLowercase, value=1)
button_lowercase.pack(padx=200, pady=1)
button_digits = customtkinter.CTkRadioButton(master=frame, radiobutton_height=15, radiobutton_width=15, text="Contains Numerical Digits", command=enableDigits, variable= rvarDigits, value=1)
button_digits.pack(padx=200, pady=1)
button_special = customtkinter.CTkRadioButton(master=frame, radiobutton_height=15, radiobutton_width=15, text="Contains Special Characters", command=enableSpecial, variable= rvarSpecial, value=1)
button_special.pack(padx=200, pady=1)
button_memorable = customtkinter.CTkRadioButton(master=frame, radiobutton_height=15, radiobutton_width=15, text="Slightly More Memorable", command=enableMemorable, variable= rvarMemorable, value=1)
button_memorable.pack(padx=200, pady=1)

def resetButtons():
    button_uppercase.deselect()
    button_lowercase.deselect()
    button_dictionary.deselect()
    button_addLetters.deselect()
    button_digits.deselect()
    button_special.deselect()
    button_memorable.deselect()

    global bool_generate
    global bool_requestAddLetters
    global bool_requestLower
    global bool_requestUpper
    global bool_requestUpper
    global bool_requestDigits
    global bool_requestSpecial
    global bool_requestDict
    global bool_requestMemorable
    global int_numOfSelected

    bool_generate = False
    bool_requestAddLetters = False
    bool_requestLower = False
    bool_requestUpper = False
    bool_requestDigits = False
    bool_requestSpecial = False
    bool_requestDict = False
    bool_requestMemorable = False
    int_numOfSelected = 0

    outputLabel.configure(text="")
    generalResultsLabel.configure(text="Password Output")
    additionalNotesLabel.configure(text="Note: No Additional Notes at this time")
    inputBox.delete("0.0", "end-1c")


def copy():
    copied_var = outputLabel.cget("text")
    pyperclip.copy(copied_var)
    test = pyperclip.paste()

    if copied_var != "":
        additionalNotesLabel.configure(text="Note: Password Successfully copied to clipboard.")
    else:
        additionalNotesLabel.configure(text="Error: No Password to copy to clipboard.")


generalResultsLabel = customtkinter.CTkLabel(master=frame, text="Input Requested Length Below:", font=("OpenSans", 12))
generalResultsLabel.pack(pady=0, padx=5)
# userInput textBox

inputBox = customtkinter.CTkTextbox(master=frame, height=20, width=50, activate_scrollbars=False)
inputBox.pack(pady=0, padx=10)
# CheckPasswordButton

checkPWButton = customtkinter.CTkButton(frame, text="Generate Password", width=150, command=generatePass)
checkPWButton.pack(pady=5, padx=10)

# output results label
generalResultsLabel = customtkinter.CTkLabel(master=frame, text="Password Output", font=("OpenSans", 14))
generalResultsLabel.pack(pady=5, padx=5)

# password output
outputLabel = customtkinter.CTkLabel(master=frame, text="", font=("OpenSans", 18))
outputLabel.pack(pady=10, padx=5)


additionalNotesLabel = customtkinter.CTkLabel(master=frame, text="Note: No Additional Notes at this time", font=("OpenSans", 12))
additionalNotesLabel.pack(pady=10, padx=5)

resetButton = customtkinter.CTkButton(frame, text="Copy to Clipboard", width=150, command=copy)
resetButton.pack(pady=5, padx=10)

resetButton = customtkinter.CTkButton(frame, text="Reset Options", width=150, command=resetButtons)
resetButton.pack(pady=5, padx=10)

nameLabel = customtkinter.CTkLabel(master=frame, text="CPSC 329 W23 | Group 9", font=("OpenSans", 9))
nameLabel.pack(pady=10, padx=0)

app.mainloop()
