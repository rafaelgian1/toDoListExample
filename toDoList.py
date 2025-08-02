# todo.py

import json
import os

TODO_FILE = "todos.json"


def load_tasks():
    """Φορτώνει τις εργασίες από το αρχείο JSON, αν υπάρχει."""
    if not os.path.exists(TODO_FILE):
        return []

    with open(TODO_FILE, "r") as f:  # r για να
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


def delete_tasks(tasks, index):
    """Διαγράφει μια εγγεγραμμένη λειτουργία."""
    if index < 0 or index >= len(tasks):
        print("🔹 Δεν υπάρχει καταχωρημένη εργασία")
        return
    else:
        tasks.pop(index)
        save_tasks(tasks)
        print("Διαγράφηκε με επιτυχία η εργασία:")


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
        print("\n1. Προσθήκη\n2. Ολοκλήρωση\n3. Διαγραφή Εργασίας\n4. Έξοδος")
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

        elif choice == "4":
            print("👋 Έξοδος.")
            break

        elif choice == "3":
            try:
                index = int(input("Αριθμός εργασίας προς διαγραφή: ")) - 1
                delete_tasks(tasks, index)
            except ValueError:
                print("❌ Μη έγκυρη εισαγωγή.")
        else:
            print("❌ Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()
