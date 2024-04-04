from pathlib import Path

def sign_guest_book():

    """Collects and stores users names."""

    flag = True
    guest_book_log = ''

    while flag:

        sign_in = input("Enter your first and last name to sign in: "
                        "(enter 'q' to quit): ")  
        
        if sign_in != 'q':
            guest_book_log += f"{sign_in}\n"

        else: 
            flag = False

    return guest_book_log

book_entries = sign_guest_book()

path = Path('text_files/guest_book.txt')
path.write_text(book_entries)

