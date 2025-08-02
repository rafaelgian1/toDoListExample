# todo.py

import json
import os

TODO_FILE = "todos.json"


def load_tasks():
    """Φορτώνει τις εργασίες από το αρχείο JSON, αν υπάρχει."""
    if not os.path.exists(TODO_FILE):
        return []

    with open(TODO_FILE, "r") as f: # r για να 
        return json.load(f)


def save_tasks(tasks):
    """Αποθηκεύει τις εργασίες σε JSON αρχείο."""
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def list_tasks(tasks):
    """Εμφανίζει όλες τις εργασίες με αριθμούς."""
    if not tasks:
        print("🔹 Δεν υπάρχουν καταχωρημένες εργασίες.")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. [{'x' if task['done'] else ' '}] {task['title']}")


def add_task(tasks, title):
    """Προσθέτει νέα εργασία."""
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("✅ Προστέθηκε:", title)


def mark_done(tasks, index):
    """Σημειώνει μια εργασία ως ολοκληρωμένη."""
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"✔️ Ολοκληρώθηκε: {tasks[index]['title']}")
    else:
        print("❌ Μη έγκυρος αριθμός εργασίας.")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO DO LIST ---")
        list_tasks(tasks)
        print("\n1. Προσθήκη\n2. Ολοκλήρωση\n3. Έξοδος")
        choice = input("Επιλογή: ")

        if choice == "1":
            title = input("Τίτλος εργασίας: ")
            add_task(tasks, title)
        elif choice == "2":
            try:
                index = int(input("Αριθμός εργασίας για ολοκλήρωση: ")) - 1
                mark_done(tasks, index)
            except ValueError:
                print("❌ Μη έγκυρη εισαγωγή.")
        elif choice == "3":
            print("👋 Έξοδος.")
            break
        else:
            print("❌ Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()