def to_csv_file(filename, headers, rows, delimiter=",", new_line="\n"):
    with open(filename, "w") as file:
        # Записываем заголовки
        file.write(delimiter.join(headers) + new_line)

        # Записываем строки с данными
        for row in rows:
            file.write(delimiter.join(row) + new_line)
headers_list = ["Name", "Age", "City"]
data = [["John", "25", "New York"], ["Alice", "30", "London"], ["Bob", "35", "Paris"]]

to_csv_file("output.csv", headers_list, data)