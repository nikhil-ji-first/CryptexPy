def write_to_file(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(data)

def read_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found.")
        return None
