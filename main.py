import tkinter as tk
from tkinter import messagebox

def en_to_fa_numbers(number_str):
    """
    این تابع یک رشته از اعداد انگلیسی را به معادل فارسی تبدیل می‌کند.
    """
    english_to_farsi = {
        '0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴',
        '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'
    }
    
    farsi_number = ''
    for digit in number_str:
        if digit in english_to_farsi:
            farsi_number += english_to_farsi[digit]
        else:
            farsi_number += digit
            
    return farsi_number

def convert_and_display(event=None):
    """
    این تابع ورودی را می‌گیرد و آن را به اعداد فارسی تبدیل می‌کند.
    در صورت ورودی نامعتبر، خطای مربوطه را نمایش می‌دهد.
    """
    english_number = entry_input.get()
    
    try:
        if not english_number:
            raise ValueError("لطفا یک عدد وارد کنید.")

        if any(char not in '0123456789.' for char in english_number):
            raise ValueError("ورودی نامعتبر! لطفا فقط عدد وارد کنید.")

        float(english_number)
        
        farsi_number = en_to_fa_numbers(english_number)
        
        entry_output.config(state='normal')
        entry_output.delete(0, tk.END)
        entry_output.insert(0, farsi_number)
        entry_output.config(state='readonly')
        
    except ValueError as e:
        messagebox.showerror("خطا", str(e))
        entry_output.config(state='normal')
        entry_output.delete(0, tk.END)
        entry_output.config(state='readonly')

def copy_to_clipboard():
    """
    این تابع متن موجود در کادر خروجی را در کلیپ‌بورد کپی می‌کند.
    """
    text_to_copy = entry_output.get()
    
    if text_to_copy:
        root.clipboard_clear()
        root.clipboard_append(text_to_copy)
        root.update()
        messagebox.showinfo("موفق", "✅ عدد فارسی با موفقیت کپی شد!")
    else:
        messagebox.showwarning("توجه", "❌ کادر خروجی خالی است.")

def clear_fields():
    """
    این تابع محتوای هر دو کادر ورودی و خروجی را پاک می‌کند.
    """
    entry_input.delete(0, tk.END)
    entry_output.config(state='normal')
    entry_output.delete(0, tk.END)
    entry_output.config(state='readonly')
    entry_input.focus()

# --- ساخت پنجره اصلی ---
root = tk.Tk()
root.title("تبدیل اعداد انگلیسی به فارسی 🔄")
root.geometry("400x290")
root.resizable(False, False)

# --- ساخت و قرار دادن ویجت‌ها ---
label_title = tk.Label(root, text="🔢 لطفا عدد انگلیسی را وارد کنید:", font=("Arial", 12))
label_title.pack(pady=10)

entry_input = tk.Entry(root, font=("Arial", 14), width=30, justify='center')
entry_input.pack(pady=5)
entry_input.focus()

# اتصال رویداد Enter به تابع تبدیل
# '<Return>' نام رویداد Enter در Tkinter است
entry_input.bind('<Return>', convert_and_display)

button_convert = tk.Button(root, text="تبدیل", command=convert_and_display, font=("Arial", 12), bg="#4CAF50", fg="white")
button_convert.pack(pady=10)

label_output = tk.Label(root, text="📋 معادل فارسی:", font=("Arial", 12, "bold"))
label_output.pack(pady=5)

entry_output = tk.Entry(root, font=("Arial", 14), width=30, justify='center', state='readonly')
entry_output.pack(pady=5)

# فریم برای دکمه‌های کپی و پاک کردن
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

button_copy = tk.Button(button_frame, text="کپی کردن", command=copy_to_clipboard, font=("Arial", 12), bg="#2196F3", fg="white")
button_copy.pack(side=tk.LEFT, padx=5)

button_clear = tk.Button(button_frame, text="پاک کردن", command=clear_fields, font=("Arial", 12), bg="#f44336", fg="white")
button_clear.pack(side=tk.LEFT, padx=5)

# اجرای برنامه
root.mainloop()
