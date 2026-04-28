## 🔐 Smart Password Generator (Python GUI)

A modern and interactive **Password Generator Application** built using **Python** and **Custom Tkinter**.
This app helps users create **secure, customizable passwords** with real-time strength analysis.

---

## 🚀 Features

* 🔢 Generate passwords with custom length (6–40 characters)
* 🔤 Include/exclude:

  * Letters
  * Numbers
  * Symbols
* 📊 Real-time password strength indicator
* 📋 Copy password to clipboard
* ⚡ Fast and dynamic password generation
* 🎨 Clean and modern UI using CustomTkinter

---

## 🛠️ Tech Stack

* **Python**
* **CustomTkinter (GUI framework)**
* Built-in libraries:

  * `random`
  * `string`

---

## 📂 Project Structure

```id="z3kq7p"
password-generator/
│
├── Password_Generator.py   # Main application file
├── README.md               # Documentation
```

---

## ▶️ How to Run the Project

### 1. Clone the Repository

```id="r9k2lx"
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

---

### 2. Install Dependencies

```id="w1b7qn"
pip install customtkinter
```

---

### 3. Run the Application

```id="u8d5mj"
python Password_Generator.py
```

---

## 💡 How It Works

* Password is generated using:

```python
create_password(length, use_letters, use_numbers, use_symbols)
```

* Character sets are dynamically built using:

```python
string.ascii_letters
string.digits
string.punctuation
```

* Strength is evaluated based on:

  * Uppercase & lowercase letters
  * Numbers
  * Symbols
  * Password length

---

## 📊 Strength Levels

* 🔴 Weak
* 🟡 Medium
* 🟢 Strong

Displayed using:

* Progress bar
* Color indicators

---

## 📸 Application Preview

* Select password length using slider
* Choose character types
* Click **Generate Password**
* View strength instantly
* Copy password with one click

---

## 🔥 Key Functionalities

* Dynamic password generation
* Real-time strength analysis
* Clipboard integration
* Interactive GUI components
* Event-driven programming

---

## 📌 Future Improvements

* Save password history
* Add password encryption
* Export passwords to file
* Add dark/light theme toggle
* Strength suggestions for weak passwords

---

## 🙌 Acknowledgements

* Built using **CustomTkinter** for modern GUI design

---

## 📧 Contact

Feel free to connect for suggestions or improvements!

---

⭐ If you like this project, give it a star on GitHub!
