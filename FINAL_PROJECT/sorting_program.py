import tkinter as tk
from tkinter import ttk
import time
import re
import tkinter.messagebox as msg


def validate_input(values):
    if values == "":
        return True
    try:
        parts = values.split(",")
        for part in parts:
            part = part.strip()
            part_rematched = re.match(r'^-?\d*\.?\d*$', part)
            if part and not part_rematched:
                return False
        return True
    except Exception as e:
        print(e)
        return False


def save_results(sequence, joined_sequence, final_time):
    with open("results.txt", "w") as file:
        file.write("Введенная последовательность: " + sequence + "\n")
        file.write("Отсортированная последовательность: " + joined_sequence + "\n")
        file.write("Время затраченное на сортировку: " + final_time + " секунд\n")
    return


def sort_sequence():
    global entry, result_text, sort_combobox  # Define the global variables here

    try:
        sequence = entry.get()
        if not validate_input(sequence):
            raise ValueError("Invalid input format")

        sequence_parts = sequence.split(",")
        sorted_sequence = []
        for part in sequence_parts:
            part = part.strip()
            if part:
                if '.' in part:
                    sorted_sequence.append(float(part))
                else:
                    sorted_sequence.append(int(part))
        start_time = time.time()
        if sort_combobox.get() == "Ascending":
            sorted_sequence.sort()
        elif sort_combobox.get() == "Descending":
            sorted_sequence.sort(reverse=True)
        end_time = time.time()
        result_text.delete(1.0, tk.END)
        joined_sequence = ', '.join(map(str, sorted_sequence))
        result_text.insert(tk.END, "Sorted sequence: " + joined_sequence)
        time_taken = end_time - start_time
        final_time = "{:.6f}".format(time_taken)
        time_label.config(text="Sorting time: " + final_time + " seconds")

        save_choice = msg.askquestion("Save results", "Do you want to save the results to a file?")
        if save_choice == 'yes':
            save_results(sequence, joined_sequence, final_time)

        choice = msg.askquestion("Repeat sorting", "Do you want to repeat the sorting?")
        if choice == 'yes':
            entry.delete(0, tk.END)
        else:
            root.destroy()

    except ValueError as e:
        print(e)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: " + str(e))
    except Exception as e:
        print(e)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "An error occurred")


def run_gui():
    global entry, result_text, sort_combobox, time_label, root  # Определяем глобальные переменные
    root = tk.Tk()
    root.title("Sorting Program")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.configure(bg='light blue')
    large_font = ("Arial", 24)  # Установка большого шрифта

    default_font = ("Arial", 12)
    root.option_add("*Font", large_font)

    welcome_label = tk.Label(root, text="Welcome to sorting program!", font=("Arial", 35, "bold"), fg="blue")
    welcome_label.pack(pady=20)  # Увеличение отступа между приветственной фразой и другими элементами интерфейса

    note_label = tk.Label(root, text="ENTER NUMBERS SEPARATED BY COMMA:", font=large_font, fg="blue")
    note_label.pack()

    entry = tk.Entry(root, width=50)  # Установка ширины поля ввода на 50 символов
    entry.pack(pady=10)  # Увеличение отступа между полем ввода и другими элементами интерфейса

    entry['validate'] = 'key'
    vcmd = (entry.register(validate_input), '%P')
    entry['validatecommand'] = vcmd

    sort_combobox = ttk.Combobox(root, values=["Ascending", "Descending"], state="readonly", font=large_font)
    sort_combobox.current(0)
    sort_combobox.pack()

    start_button = ttk.Button(root, text="Start", command=sort_sequence, style="C.TButton")
    start_button.pack(pady=10)

    style = ttk.Style()
    style.configure("C.TButton", foreground="black", background="turquoise", font=large_font)

    result_label = tk.Label(root, text="RESULTING SEQUENCE:", font=large_font, fg="blue")
    result_label.pack()

    result_text = tk.Text(root, height=5, width=50, wrap="word")
    result_text.pack()

    time_label = tk.Label(root, text="SORTING TIME: ", font=large_font, fg="blue")
    time_label.pack()

    root.mainloop()


if __name__ == "__main__":
    run_gui()
