# Docstrings to document functions:

def format_name(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the full name."""
    
    if f_name == "" or l_name == "":
        return "Invalid input"
    return f"{f_name.title()} {l_name.title()}"

print(format_name(input("First name: "), input("Last name: ")))
