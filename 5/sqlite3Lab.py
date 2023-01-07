import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        if name != '' and priority > 0 and self.find_task(name) is None:
            self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
            self.conn.commit()

    def find_task(self, name):
        for row in self.c.execute('SELECT * FROM tasks'):
            if row[1] == name:
                return row
        return None

    def show_tasks(self):
        self.c.execute('SELECT * FROM tasks')
        print(self.c.fetchall())


app = Todo()
app.add_task()
app.show_tasks()
