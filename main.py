def custom_write(file_name, strings):
    """
    Writes strings to a file and returns a dictionary with the position details.

    Args:
        file_name (str): Name of the file to write to.
        strings (list): List of strings to write to the file.

    Returns:
        dict: A dictionary where keys are tuples (line_number, byte_offset) and values are the written strings.
    """
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for line_number, string in enumerate(strings, start=1):
            byte_offset = file.tell()
            file.write(string + '\n')
            strings_positions[(line_number, byte_offset)] = string

    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)