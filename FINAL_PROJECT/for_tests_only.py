import time
import re


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


def sort_sequence(sequence, sort_order):
    try:
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
        if sort_order == "Ascending":
            sorted_sequence.sort()
        elif sort_order == "Descending":
            sorted_sequence.sort(reverse=True)
        end_time = time.time()
        joined_sequence = ', '.join(map(str, sorted_sequence))
        time_taken = end_time - start_time
        final_time = "{:.6f}".format(time_taken)

        save_results(sequence, joined_sequence, final_time)

    except ValueError as e:
        print("Error: ", e)
    except Exception as e:
        print("An error occurred: ", e)


def run_sorting_program():
    print("Welcome to sorting program!")
    sequence = input("Enter numbers separated by commas: ")
    sort_order = input("Enter sort order (Ascending/Descending): ")
    sort_sequence(sequence, sort_order)
    print("Sorting completed. Results have been saved in 'results.txt' file.")


if __name__ == "__main__":
    run_sorting_program()
