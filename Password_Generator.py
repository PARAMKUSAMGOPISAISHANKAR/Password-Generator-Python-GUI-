import random
import string
import customtkinter as ctk


def build_charset(use_letters, use_numbers, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    return characters


def create_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = build_charset(use_letters, use_numbers, use_symbols)
    if not characters:
        return ""
    return "".join(random.choice(characters) for _ in range(length))


def evaluate_strength(password):
    score = 0
    if any(char.islower() for char in password):
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1
    if len(password) >= 12:
        score += 1
    return score


def update_strength_ui(password):
    if not password:
        strength_label.configure(text="Strength: -", text_color="#64748b")
        strength_bar.set(0)
        return

    score = evaluate_strength(password)
    progress = min(score / 5, 1)
    strength_bar.set(progress)

    if score <= 2:
        strength_label.configure(text="Strength: Weak", text_color="#fb7185")
        strength_bar.configure(progress_color="#ef4444")
    elif score == 3:
        strength_label.configure(text="Strength: Medium", text_color="#facc15")
        strength_bar.configure(progress_color="#eab308")
    else:
        strength_label.configure(text="Strength: Strong", text_color="#34d399")
        strength_bar.configure(progress_color="#10b981")


def on_length_change(value):
    length_value_label.configure(text=f"{int(float(value))} chars")


def generate_password_action():
    length = int(length_slider.get())
    password = create_password(
        length=length,
        use_letters=var_letters.get(),
        use_numbers=var_numbers.get(),
        use_symbols=var_symbols.get(),
    )

    result_box.delete(0, "end")
    if not password:
        result_box.insert(0, "Select at least one option")
        update_strength_ui("")
        return

    result_box.insert(0, password)
    copy_status.configure(text="")
    update_strength_ui(password)


def copy_password_action():
    password = result_box.get().strip()
    if not password or password == "Select at least one option":
        copy_status.configure(text="Generate a password first", text_color="#dc2626")
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    copy_status.configure(text="Password copied to clipboard", text_color="#059669")
    root.after(1800, lambda: copy_status.configure(text=""))


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Smart Password Generator")
root.geometry("520x600")
root.minsize(450, 560)
root.configure(fg_color="#eef4ff")

background = ctk.CTkFrame(root, fg_color="#eef4ff", corner_radius=0)
background.pack(fill="both", expand=True)

hero = ctk.CTkFrame(
    background,
    corner_radius=22,
    fg_color="#dbeafe",
    border_width=1,
    border_color="#bfdbfe",
)
hero.pack(fill="x", padx=24, pady=(24, 14))

title = ctk.CTkLabel(
    hero,
    text="Password Generator",
    font=("Segoe UI Semibold", 30),
    text_color="#1e3a8a",
)
title.pack(anchor="w", padx=20, pady=(16, 4))

subtitle = ctk.CTkLabel(
    hero,
    text="Create stronger passwords with one click",
    font=("Segoe UI", 14),
    text_color="#475569",
)
subtitle.pack(anchor="w", padx=20, pady=(0, 16))

card = ctk.CTkFrame(
    background,
    corner_radius=22,
    fg_color="#ffffff",
    border_width=1,
    border_color="#cbd5e1",
)
card.pack(fill="both", expand=True, padx=24, pady=(0, 24))

length_row = ctk.CTkFrame(card, fg_color="transparent")
length_row.pack(fill="x", padx=20, pady=(20, 4))

length_title = ctk.CTkLabel(
    length_row,
    text="Password length",
    font=("Segoe UI Semibold", 15),
    text_color="#0f172a",
)
length_title.pack(side="left")

length_value_label = ctk.CTkLabel(
    length_row,
    text="12 chars",
    font=("Segoe UI", 13),
    text_color="#2563eb",
)
length_value_label.pack(side="right")

length_slider = ctk.CTkSlider(
    card,
    from_=6,
    to=40,
    number_of_steps=34,
    command=on_length_change,
    progress_color="#2563eb",
    button_color="#3b82f6",
    button_hover_color="#1d4ed8",
)
length_slider.set(12)
length_slider.pack(fill="x", padx=20, pady=(0, 14))

var_letters = ctk.BooleanVar(value=True)
var_numbers = ctk.BooleanVar(value=True)
var_symbols = ctk.BooleanVar(value=True)

checkbox_style = dict(
    fg_color="#2563eb",
    hover_color="#1d4ed8",
    border_color="#94a3b8",
    checkmark_color="#ffffff",
    text_color="#0f172a",
    font=("Segoe UI", 14),
)

ctk.CTkCheckBox(card, text="Include letters", variable=var_letters, **checkbox_style).pack(
    anchor="w", padx=20, pady=(2, 2)
)
ctk.CTkCheckBox(card, text="Include numbers", variable=var_numbers, **checkbox_style).pack(
    anchor="w", padx=20, pady=(2, 2)
)
ctk.CTkCheckBox(card, text="Include symbols", variable=var_symbols, **checkbox_style).pack(
    anchor="w", padx=20, pady=(2, 8)
)

generate_button = ctk.CTkButton(
    card,
    text="Generate Password",
    command=generate_password_action,
    font=("Segoe UI Semibold", 15),
    height=42,
    corner_radius=12,
    fg_color="#2563eb",
    hover_color="#1d4ed8",
)
generate_button.pack(fill="x", padx=20, pady=(10, 10))

result_box = ctk.CTkEntry(
    card,
    font=("Consolas", 15),
    height=40,
    corner_radius=12,
    border_width=1,
    border_color="#94a3b8",
    fg_color="#f8fafc",
    text_color="#0f172a",
)
result_box.pack(fill="x", padx=20, pady=(2, 8))

strength_label = ctk.CTkLabel(
    card,
    text="Strength: -",
    font=("Segoe UI Semibold", 13),
    text_color="#64748b",
)
strength_label.pack(anchor="w", padx=20, pady=(2, 4))

strength_bar = ctk.CTkProgressBar(
    card,
    height=12,
    corner_radius=6,
    fg_color="#e2e8f0",
    progress_color="#94a3b8",
)
strength_bar.set(0)
strength_bar.pack(fill="x", padx=20, pady=(0, 12))

copy_button = ctk.CTkButton(
    card,
    text="Copy Password",
    command=copy_password_action,
    font=("Segoe UI Semibold", 14),
    height=40,
    corner_radius=12,
    fg_color="#0f766e",
    hover_color="#0d9488",
)
copy_button.pack(fill="x", padx=20, pady=(0, 8))

copy_status = ctk.CTkLabel(
    card,
    text="",
    font=("Segoe UI", 12),
    text_color="#86efac",
)
copy_status.pack(anchor="w", padx=20, pady=(0, 16))

root.mainloop()
