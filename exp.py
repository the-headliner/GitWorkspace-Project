"""
Simple CLI Notes App
We’ll use this small project to practice Git commands.
"""

notes = []

def add_note(note):
    notes.append(note)
    print(f" Note added: {note}")

def delete_note(note):
    if note in notes:
        notes.remove(note)
        print(f" Note deleted: {note}")
    else:
        print(f" Note not found: {note}")

def list_notes():
    if notes:
        print(" Your Notes:")
        for i, note in enumerate(notes, start=1):
            print(f"{i}. {note}")
    else:
        print(" No notes found.")









# --- CLI Menu ---
if __name__ == "__main__":
    while True:
        print("\n--- Notes App ---")
        print("1. Add Note")
        print("2. Delete Note")
        print("3. List Notes")
        print("4. Exit")
        print("5.Count Notes")
        print("6.Duplicate note")


        
        choice = input("Choose an option: ")

        if choice == "1":
            note = input("Enter note: ")
            add_note(note)
        elif choice == "2":
            note = input("Enter note to delete: ")
            delete_note(note)
        elif choice == "3":
            list_notes()
        elif choice == "4":
            print(" Goodbye!")
            break
        # elif choice == "5":
        #     print(f" You have {count_notes()} notes.")
        # elif choice == "5":
        #     note = input("Enter note to duplicate: ")
        #     duplicate_note(note)

        else:
            print(" Invalid choice")
