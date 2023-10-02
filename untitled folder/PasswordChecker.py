import math
import tkinter
import customtkinter

# PasswordPaladin - PasswordChecker.py
# Jason Ngu & Alfred Zhu

userInput = ""

def strengthCheck(userInput):

    generalResultsLabel.configure(text="Basic Checkup Results")
    generalOutputBox.configure(state="normal")
    generalOutputBox.delete("0.0", "end-1c")
    generalProgressBar.set(0)
    generalProgressBar.configure(progress_color="#4A4D50")

    advancedResultsLabel.configure(text="Advanced Checkup Information")
    advancedOutputBox.configure(state="normal")
    advancedOutputBox.delete("0.0", "end-1c")

    bareMinimumCaseLabel.configure(text="Minimum Requirements Check")
    bareMinimumCaseBox.configure(state="normal")
    bareMinimumCaseBox.delete("0.0", "end-1c")
    bareMinimumBar.set(0)
    bareMinimumBar.configure(progress_color="#4A4D50")

    if (len(userInput) <= 0):
        outputText = "(✗) ERROR: Invalid Input. Please try again."

        generalResultsLabel.configure(text="Basic Checkup Results: N/A")
        advancedResultsLabel.configure(text="Advanced Checkup Information: N/A")
        bareMinimumCaseLabel.configure(text="Minimum Requirements Check: N/A")

        generalOutputBox.insert("0.0", outputText)
        advancedOutputBox.insert("0.0", outputText)
        bareMinimumCaseBox.insert("0.0", outputText)

        generalProgressBar.set(1)
        generalProgressBar.configure(progress_color="#990F02")

        bareMinimumBar.set(1)
        bareMinimumBar.configure(progress_color="#990F02")

    elif (len(userInput) > 0):
        int_NumOfDictWords = 0
        int_numOfLetters = 0
        int_numOfLowercase = 0
        int_numOfUppercase = 0
        int_numOfDigits = 0
        int_numOfSpecialChar = 0
        int_traceOfCommon = 0
        int_numOfLastDigits = 0
        int_numOfLastSpecial = 0
        int_containsCommonKeyboard = 0
        int_numOfTypes = 0


        bar_simple = 0
        bar_advanced = 0
        old_score = 0

        bool_isOneDictWord = False
        bool_hasDictWords = False

        bool_repeatedLetters = False

        bool_IsCommonPassW = False
        bool_traceOfCommon = False

        bool_IsCommonDigits = False
        bool_isCommonKeyboard = False
        bool_containsCommonDigits = False
        bool_containsCommonKeyboard = False

        bool_containsDigit = False
        bool_containsSpecialChar = False
        bool_containsUppercase = False
        bool_containsLowerCase = False

        bool_lastIsDigit = False
        bool_lastIsSpecialChar = False
        bool_firstIsUppercase = False
        bool_firstIsDigit = False
        bool_firstIsSpecial = False

        specialChars = "\"!@#$%^&*()[]{}~`-+?_=,<>\\/"

        # dictionary check
        with open('words_alpha.txt', 'r') as file:
            english_words = {word.strip().lower() for word in file}

        if userInput.lower() in english_words:
            bool_isOneDictWord = True
            bool_hasDictWords = True
            int_NumOfDictWords = 1

        else:
            # define a set to keep track of confirmed word indices
            confirmed_indices = set()
            # loop through all possible English words in descending order of length
            for substring_length in range(len(userInput), 2, -1):
                for i in range(len(userInput) - substring_length + 1):
                    # check if this index has already been confirmed to contain a word
                    if i in confirmed_indices:
                        continue

                    substring = userInput[i:i+substring_length].lower()
                    if (substring in english_words):
                        # check if the substring is an exact match with an English word
                        exact_match = next((word for word in english_words if word == substring), None)
                        if (exact_match is not None and exact_match == substring):
                            int_NumOfDictWords += 1
                            bool_hasDictWords = True

                            # add all indices that this word spans to the confirmed indices set
                            for j in range(i, i+substring_length):
                                confirmed_indices.add(j)

        # top 10000 passwords
        with open('top10000.txt', 'r') as file:
            common_passwords = {word.strip().lower() for word in file}

        if userInput.lower() in common_passwords:
            bool_IsCommonPassW = True
            bool_traceOfCommon = True

        else:
            # define a set to keep track of confirmed word indices
            confirmed_indices = set()

            # loop through all possible English words in descending order of length
            for substring_length in range(len(userInput), 2, -1):
                for i in range(len(userInput) - substring_length + 1):
                    # check if this index has already been confirmed to contain a word
                    if i in confirmed_indices:
                        continue

                    substring = userInput[i:i+substring_length]
                    if (substring in common_passwords):
                        # check if the substring is an exact match with an English word
                        exact_match = next((word for word in common_passwords if word == substring), None)
                        if (exact_match is not None and exact_match == substring):
                            bool_traceOfCommon = True
                            int_traceOfCommon += 1

                            # add all indices that this word spans to the confirmed indices set
                            for j in range(i, i+substring_length):
                                confirmed_indices.add(j)

        # checking for common digits
        with open('digits_alpha.txt', 'r') as file:
            common_digits = {word.strip().lower() for word in file}

        if userInput.lower() in common_digits:
            bool_IsCommonDigits = True

        else:
            # define a set to keep track of confirmed word indices
            confirmed_indices = set()

            # loop through all possible English words in descending order of length
            for substring_length in range(len(userInput), 1, -1):
                for i in range(len(userInput) - substring_length + 1):
                    # check if this index has already been confirmed to contain a word
                    if i in confirmed_indices:
                        continue

                    substring = userInput[i:i+substring_length]
                    if (substring in common_digits):
                        # check if the substring is an exact match with an English word
                        exact_match = next((word for word in common_digits if word == substring), None)
                        if (exact_match is not None and exact_match == substring):
                            bool_containsCommonDigits = True

                            # add all indices that this word spans to the confirmed indices set
                            for j in range(i, i+substring_length):
                                confirmed_indices.add(j)


        # checking for keyboard inputs
        with open('common_keyboard.txt', 'r') as file:
            common_inputs = {word.strip().lower() for word in file}

        if userInput.lower() in common_inputs:
            bool_isCommonKeyboard = True
            bool_containsCommonKeyboard = True
            int_containsCommonKeyboard = 1
        else:
            # define a set to keep track of confirmed word indices
            confirmed_indices = set()

            # loop through all possible English words in descending order of length
            for substring_length in range(len(userInput), 1, -1):
                for i in range(len(userInput) - substring_length + 1):
                    # check if this index has already been confirmed to contain a word
                    if i in confirmed_indices:
                        continue

                    substring = userInput[i:i+substring_length]
                    if (substring in common_inputs):
                        # check if the substring is an exact match with an English word
                        exact_match = next((word for word in common_inputs if word == substring), None)
                        if (exact_match is not None and exact_match == substring):
                            bool_containsCommonKeyboard = True
                            int_containsCommonKeyboard += 1

                            # add all indices that this word spans to the confirmed indices set
                            for j in range(i, i+substring_length):
                                confirmed_indices.add(j)

        # For loop to check every character 0 < x < length
        for indice in range (0, len(userInput)):
            currentInd = userInput[indice]

            # checking if current indice is lowercase
            if (currentInd.islower() == True):
                bool_containsLowerCase = True
                int_numOfLowercase += 1
                int_numOfLetters += 1

            # checking if current indice is uppercase
            elif (currentInd.isupper() == True):
                bool_containsUppercase = True
                int_numOfUppercase += 1
                int_numOfLetters += 1

            # checking if current indice is a digit 0-9
            elif (currentInd.isdigit() == True):
                bool_containsDigit = True
                int_numOfDigits += 1

            elif (any(j in specialChars for j in currentInd)):
                bool_containsSpecialChar = True
                int_numOfSpecialChar += 1

    # num of types
        if bool_containsDigit == True:
            int_numOfTypes += 1
        if bool_containsUppercase == True:
            int_numOfTypes += 1
        if bool_containsLowerCase == True:
            int_numOfTypes += 1
        if bool_containsSpecialChar == True:
            int_numOfTypes += 1

    # last digit checker
        for i in range(len(userInput)-1, -1, -1):
            if userInput[i].isdigit():
                bool_lastIsDigit = True
                int_numOfLastDigits += 1
            else:
                break

    # last special checker
        for i in range(len(userInput)-1, -1, -1):
            if (any(j in specialChars for j in userInput[i])):
                bool_lastIsSpecialChar = True
                int_numOfLastSpecial += 1
            else:
                break

    # if first is uppercase
        if (userInput[0].isupper() == True):
            bool_firstIsUppercase = True

    # if first is digit
        if (userInput[0].isdigit() == True):
            bool_firstIsDigit = True

    # if first is special char
        if (any(j in specialChars for j in userInput[0])):
            bool_firstIsSpecial = True

    # check for repeating letters
        for i in range(len(userInput)-1):
            if userInput[i] == userInput[i+1]:
                bool_repeatedLetters = True


    # BASIC PASSWORD CHECKUP
        # password length
        if (len(userInput) > 8):
            preText = "(✓) Length of Password is greater than 8"
            bar_simple += 0.2
        else:
            preText = "(✗) Length of Password is less than 8"

        outputText = preText
        generalOutputBox.insert("0.0", outputText)

        # contains uppercase
        if (bool_containsUppercase == True):
            preText = "\n(✓) Contains "
            bar_simple += 0.2
        else:
            preText = "\n(✗) Doesn't contain "
        outputText = preText + "uppercase letters (A → Z)"
        generalOutputBox.insert("end-1c", outputText)

        # contains lowercase
        if (bool_containsLowerCase == True):
            preText = "\n(✓) Contains "
            bar_simple += 0.2
        else:
            preText = "\n(✗) Doesn't contain "
        outputText = preText + "lowercase letters (a → z)"
        generalOutputBox.insert("end-1c", outputText)

        # contains numbers
        if (bool_containsDigit == True):
            preText = "\n(✓) Contains "
            bar_simple += 0.2
        else:
            preText = "\n(✗) Doesn't contain "
        outputText = preText + "numerical digits (0 → 9)"
        generalOutputBox.insert("end-1c", outputText)

        # contains numbers
        if (bool_containsSpecialChar == True):
            preText = "\n(✓) Contains "
            bar_simple += 0.2
        else:
            preText = "\n(✗) Doesn't contain any "
        outputText = preText + "special characters"
        generalOutputBox.insert("end-1c", outputText)

        if math.isclose(bar_simple, 0.0):
            generalProgressBar.configure(progress_color="red")
            generalResultsLabel.configure(text="Basic Checkup Score: 0/5")

        elif math.isclose(bar_simple, 0.2):
            generalProgressBar.configure(progress_color="red")
            generalResultsLabel.configure(text="Basic Checkup Score: 1/5")

        elif math.isclose(bar_simple, 0.4):
            generalProgressBar.configure(progress_color="orange")
            generalResultsLabel.configure(text="Basic Checkup Score: 2/5")

        elif math.isclose(bar_simple, 0.6):
            generalProgressBar.configure(progress_color="yellow")
            generalResultsLabel.configure(text="Basic Checkup Score: 3/5")

        elif math.isclose(bar_simple, 0.8):
            generalProgressBar.configure(progress_color="green")
            generalResultsLabel.configure(text="Basic Checkup Score: 4/5")

        elif math.isclose(bar_simple, 1.0):
            generalProgressBar.configure(progress_color="green")
            generalResultsLabel.configure(text="Basic Checkup Score: 5/5")

        generalProgressBar.set(bar_simple)
        generalOutputBox.configure(state="disabled")



        # BARE MINIMUM CHECK
        minimumCounter = 0

        if len(userInput) == 8:
            outputText = "(✓) Is exactly minimum length 8\n"
            minimumCounter += 1
        elif len(userInput) > 8:
            outputText = "(✓) Is longer than minimum length 8\n"
            minimumCounter += 2
        else:
            outputText = "(✗) Is shorter than mininum length 8\n"
        bareMinimumCaseBox.insert("end-1c", outputText)

        if bool_containsUppercase == True:
            if int_numOfUppercase == 1:
                outputText = "(✓) Contains exactly one uppercase\n"
                minimumCounter += 1
            else:
                outputText = "(✓) Contains more than one uppercase\n"
                minimumCounter += 2
        else:
            outputText = "(✗) Does not contain uppercase\n"
        bareMinimumCaseBox.insert("end-1c", outputText)

        if bool_containsLowerCase == True:
            if int_numOfLowercase == 1:
                outputText = "(✓) Contains exactly one lowercase\n"
                minimumCounter += 1
            else:
                outputText = "(✓) Contains more than one lowercase\n"
                minimumCounter += 2
        else:
            outputText = "(✗) Does not contain lowercase\n"
        bareMinimumCaseBox.insert("end-1c", outputText)

        if bool_containsDigit == True:
            if int_numOfDigits == 1:
                outputText = "(✓) Contains exactly one digit\n"
                minimumCounter += 1
            else:
                outputText = "(✓) Contains more than one digit\n"
                minimumCounter += 2
        else:
            outputText = "(✗) Does not contain any digits\n"
        bareMinimumCaseBox.insert("end-1c", outputText)

        if bool_containsSpecialChar == True:
            if int_numOfSpecialChar == 1:
                outputText = "(✓) Contains exactly one special character"
                minimumCounter += 1
            else:
                outputText = "(✓) Contains more than one special character"
                minimumCounter += 2
        else:
            outputText = "(✗) Does not contain any special characters"
        bareMinimumCaseBox.insert("end-1c", outputText)

        if bool_containsLowerCase == True and bool_containsUppercase == True and bool_containsDigit and bool_containsSpecialChar == True:
            if minimumCounter == 5:
                bareMinimumBar.set(minimumCounter/10)
                bareMinimumBar.configure(progress_color="yellow")
                bareMinimumCaseLabel.configure(text="Minimum Requirements Check: Just Met")
            else:
                bareMinimumBar.set(minimumCounter/10)
                bareMinimumBar.configure(progress_color="green")
                bareMinimumCaseLabel.configure(text="Minimum Requirements Check: Minimum Exceeded")
        else:
            bareMinimumBar.set(minimumCounter/10)
            bareMinimumBar.configure(progress_color="red")
            bareMinimumCaseLabel.configure(text="Minimum Requirements Check: Not Met")

        bareMinimumCaseBox.configure(state="disabled")

        # ADVANCED CHECKUP
        old_score = 15
        bar_advanced = 10
        # is literally a common password
        if (bool_IsCommonPassW == True):
            old_score = -1000
            bar_advanced -= 1
            outputText = "(✗) Is in top 10,000 most common passwords\n"
        else:
            outputText = "(✓) Is not top 10,000 most common passwords\n"
        advancedOutputBox.insert("end-1c", outputText)

        # has traces of common passwords
        if (bool_traceOfCommon == True):
            old_score -= 2
            bar_advanced -= 1
            outputText = "(✗) Traces of top 10,000 common passwords\n"
        else:
            outputText = "(✓) No traces of 10,000 common passwords\n"
        advancedOutputBox.insert("end-1c", outputText)

        # is literally just a dictionary word
        if (bool_isOneDictWord == True):
            old_score = -1000
            bar_advanced -= 1
            outputText = "(✗) Is literally just a lone dictionary word (eg: tomato)\n"
        else:
            outputText = "(✓) Is not just a lone dictionary word\n"
        advancedOutputBox.insert("end-1c", outputText)

        # contains dictionary words
        if (bool_hasDictWords == True):
            if (int_NumOfDictWords == 1):
                old_score -= 1
                bar_advanced -= 1
                outputText = "(✗) Contains a dictionary word (eg: salad)\n"
            else:
                old_score -= 0.5
                outputText = "(✗) Has multiple dictionary words (eg: tomatosoup)\n"
        else:
            outputText = "(✓) Does not contain any dictionary words\n"
        advancedOutputBox.insert("end-1c", outputText)

        # is default keystrokes
        if (bool_isCommonKeyboard == True):
            old_score = -1000
            bar_advanced -= 1
            outputText = "(✗) Is just common keyboard keys (eg: qwerty)\n"
        else:
            outputText = "(✓) Is not just common keyboard keys (eg: qwerty)\n"
        advancedOutputBox.insert("end-1c", outputText)

        # traces of common keystrokes
        if (bool_containsCommonKeyboard):
            if (int_containsCommonKeyboard == 1):
                old_score -= 1
                bar_advanced -= 1
                outputText = "(✗) Has traces of common keyboard keys\n"
            else:
                old_score -= 0.5
                bar_advanced -= 1
                outputText = "(✗) Has multiple traces of common keyboard keys\n"
        else:
            outputText = "(✓) Has no traces of common keyboard keys\n"
        advancedOutputBox.insert("end-1c", outputText)

        # just a dictionary word followed by numbers
        if (bool_hasDictWords == True and int_NumOfDictWords == 1 and bool_containsDigit == True and bool_containsSpecialChar == False):
            old_score -= 5
            bar_advanced -= 1
            outputText = "(✗) Is just a lone dictionary word with numbers\n"
        else:
            outputText = "(✓) Is not just a dictionary word with numbers\n"
        advancedOutputBox.insert("end-1c", outputText)

        # if just one type of input
        if (bool_containsDigit == True and bool_containsLowerCase == False and bool_firstIsUppercase == False and bool_containsSpecialChar == False):
            outputText = "(✗) Contains only digits (eg: 12345)\n"
            old_score = -1
            bar_advanced -= 1
        elif (bool_containsDigit == False and bool_containsLowerCase == False and bool_containsUppercase == True and bool_containsSpecialChar == False):
            outputText = "(✗) Contains only uppercase letters (eg: ABCDE)\n"
            old_score = -1
            bar_advanced -= 1
        elif (bool_containsDigit == False and bool_containsLowerCase == True and bool_containsUppercase == False and bool_containsSpecialChar == False):
            outputText = "(✗) Contains only lowercase letters (eg: abcde)\n"
            old_score = -1
            bar_advanced -= 1
        elif (bool_containsDigit == False and bool_containsLowerCase == True and bool_containsUppercase == True and bool_containsSpecialChar == False):
            outputText = "(✗) Contains only letters (eg: Abcde)\n"
            old_score = -1
            bar_advanced -= 1
        elif (bool_containsDigit == False and bool_containsLowerCase == False and bool_firstIsUppercase == False and bool_containsSpecialChar == True):
            outputText = "(✗) Contains only special characters (eg: !@#$%)\n"
            old_score = -1
            bar_advanced -= 1
        else:
            outputText = "(✓) Password contains more than 1 type of input\n"
        advancedOutputBox.insert("end-1c", outputText)

        # if is just common digits
        if (bool_IsCommonDigits == True):
            outputText = "(✗) Password is just input of common digits\n"
            old_score = -1
            bar_advanced -= 1
        else:
            outputText = "(✓) Password is not just input of common digits\n"
        advancedOutputBox.insert("end-1c", outputText)

        if (bool_repeatedLetters == True):
            outputText = "(✗) Contains repeating letters (eg: \"oo\" in \"zoo\")\n"
            old_score -= 1
            bar_advanced -= 1
        else:
            outputText = "(✓) Doesn't have repeating letters (eg: \"oo\" in \"zoo\")\n"
        advancedOutputBox.insert("end-1c", outputText)

        # last is digit
        if (bool_lastIsDigit == True):
            if (int_numOfLastDigits == 1):
                outputText = "(#) Last indice of password is a digit\n"
            else:
                outputText = "(#) Last " + str(int_numOfLastDigits) + " indices in password are digits\n"
        else:
            outputText = "(#) Last indice of password is not a digit\n"
        advancedOutputBox.insert("end-1c", outputText)

        # last is special char
        if (bool_lastIsSpecialChar == True):
            if (int_numOfLastSpecial == 1):
                outputText = "(#) Last indice of password is a special character\n"
            else:
                outputText = "(#) Last " + str(int_numOfLastSpecial) + " indices are special characters\n"
        else:
            outputText = "(#) Last indice is not a special character\n"
        advancedOutputBox.insert("end-1c", outputText)

        # if first is uppercase
        if (bool_firstIsUppercase == True):
            outputText = "(#) First indice of password is uppercase\n"
        else:
            outputText = "(#) First indice of password is not uppercase\n"
        advancedOutputBox.insert("end-1c", outputText)

        # if first is a digit
        if (bool_firstIsDigit == True):
            outputText = "(#) First indice of password is a digit\n"
        else:
            outputText = "(#) First indice of password is not a digit\n"
        advancedOutputBox.insert("end-1c", outputText)

        # if first is special char
        if (bool_firstIsSpecial == True):
            outputText = "(#) First indice is a special character"
        else:
            outputText = "(#) First indice is not a special character"
        advancedOutputBox.insert("end-1c", outputText)

        # password length
        if (len(userInput) < 8):
            old_score -= 2
        elif (len(userInput) > 16):
            old_score += 4

        if (int_numOfTypes == 1):
            old_score -= 5
        if (int_numOfTypes == 2):
            old_score -= 3
        if (int_numOfTypes == 3):
            old_score -= 1

        advancedOutputBox.configure(state="disabled")

def getText():
    userInput = (inputBox.get("1.0", 'end-1c'))
    strengthCheck(userInput)

        # GUI CODE #

# initial setup
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")

# application
app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.title("PasswordPaladin | Password Checker")
app.geometry("640x890")
app.resizable(False, False)

# application frame
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=5, padx=5, fill="both", expand=True)

# application name titleLabel
titleLabel = customtkinter.CTkLabel(master=frame, text="PasswordPaladin | Password Checker", font=("OpenSans", 20))
titleLabel.pack(pady=5, padx=5)

# titleLabel test
infoText = "The following is an application which takes in a user-inputted password, and checks it under variety of tests to see if it passes a basic checkup, minimum requirements check, and additional advanced test cases. For additional info, please read the provided PDF for additional documentation."
infoTex = """The following application checks a user-inputted password for its strength based on a multitude of factors, reporting back to the user any found weaknesses and an overall strength score based on the tests run on the password. Please input the password you wish to test in the below test box, and press "Check Password" to check it."""
titleLabel = customtkinter.CTkTextbox(master=frame, height=85, width=510, border_width=0, wrap="word", font=("OpenSans", 12), fg_color="#2b2b2b")
titleLabel.insert("0.0", text=infoText)
titleLabel.configure(state="disabled")
titleLabel.pack(pady=5, padx=5)

# userInput textBox
inputBox = customtkinter.CTkTextbox(master=frame, height=40, width=350)
inputBox.pack(pady=5, padx=10)

# CheckPasswordButton
checkPWButton = customtkinter.CTkButton(frame, text="Check Password", width=350, command=getText)
checkPWButton.pack(pady=5, padx=10)

# results titleLabel
generalResultsLabel = customtkinter.CTkLabel(master=frame, text="Basic Checkup Results", font=("OpenSans", 14))
generalResultsLabel.pack(pady=5, padx=5)

# generalprogress bar
generalProgressBar = customtkinter.CTkProgressBar(master=frame, height=10, width=350, progress_color="#4A4D50", mode="determinate", determinate_speed=0)
generalProgressBar.set(0)
generalProgressBar.pack(pady=3, padx=10)

# generalOutputBox textBox
generalOutputBox = customtkinter.CTkTextbox(master=frame, height=95, width=350) #fg_color = "#2b2b2b"
generalOutputBox.pack(pady=5, padx=10)


# bareminimum titleLabel
bareMinimumCaseLabel = customtkinter.CTkLabel(master=frame, text="Minimum Requirements Check", font=("OpenSans", 14))
bareMinimumCaseLabel.pack(pady=5, padx=5)

#bareMinimum progressBar
bareMinimumBar = customtkinter.CTkProgressBar(master=frame, height=10, width=350, progress_color="#4A4D50", mode="determinate", determinate_speed=0)
bareMinimumBar.set(0)
bareMinimumBar.pack(pady=3, padx=10)

# bareminimum textbox
bareMinimumCaseBox = customtkinter.CTkTextbox(master=frame, height=100, width=350) #fg_color = "#2b2b2b"
bareMinimumCaseBox.pack(pady=5, padx=10)


# advancedResults titleLabel
advancedResultsLabel = customtkinter.CTkLabel(master=frame, text="Advanced Checkup Information", font=("OpenSans", 14))
advancedResultsLabel.pack(pady=5, padx=5)
# advancedOutputBox textbox
advancedOutputBox = customtkinter.CTkTextbox(master=frame, height=255, width=350) #fg_color = "#2b2b2b"
advancedOutputBox.pack(pady=5, padx=10)

nameLabel = customtkinter.CTkLabel(master=frame, text="Jason Ngu & Alfred Zhu 2023", font=("OpenSans", 9))
nameLabel.pack(pady=10, padx=0)

app.mainloop()
