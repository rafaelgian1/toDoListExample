import unittest
from toDoList import add_task, delete_tasks


class TestTodo(unittest.TestCase):
    def test_add_task(self):
        tasks = []
        add_task(tasks, "Διάβασμα")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Διάβασμα")
        self.assertFalse(tasks[0]["done"])

    def test_delete_task(self):
        tasks = [{"title": "Γυμναστήριο", "done": False}]
        delete_tasks(tasks, 0)
        self.assertEqual(len(tasks), 0)


if __name__ == "__main__":
    unittest.main()
