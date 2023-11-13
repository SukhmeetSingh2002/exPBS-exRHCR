
file_path = './fallback_count.txt'

# Function to modify the shared variable
def set_fallback_count(value):
    with open(file_path, 'w') as file:
        file.write(str(value))

def read_fallback_count():
    with open(file_path, 'r') as file:
        return int(file.read())
