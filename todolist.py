from dataclasses import dataclass
from datetime import date, datetime

PRIORITY = {"high": 0, "medium": 1, "low": 2}


@dataclass
class Task:
    title: str
    priority: str = "medium"
    due: date | None = None
    done: bool = False

    def __str__(self):
        mark = "x" if self.done else " "
        due = ""
        if self.due:
            due = f" | due {self.due}"
            if not self.done and self.due < date.today():
                due += " (OVERDUE)"
        return f"[{mark}] {self.title} <{self.priority}>{due}"


def ask_priority(default="medium"):
    p = input(f"Priority (high/medium/low) [{default}]: ").strip().lower()
    return p if p in PRIORITY else default


def ask_due(default=None):
    s = input("Due date YYYY-MM-DD (blank = none): ").strip()
    if not s:
        return default
    try:
        return datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        print("Bad date, ignoring.")
        return default


def show(tasks, indices=None):
    indices = range(len(tasks)) if indices is None else indices
    if not indices:
        print("Nothing to show.")
    for i in indices:
        print(f"{i + 1}. {tasks[i]}")


def pick(tasks):
    show(tasks)
    try:
        n = int(input("Task number: ")) - 1
        if 0 <= n < len(tasks):
            return n
    except ValueError:
        pass
    print("Invalid number.")
    return None


def main():
    tasks = []
    menu = (
        "\n1) Show  2) Add  3) Complete  4) Edit  5) Delete\n"
        "6) Search  7) Sort  8) Clear done  9) Stats  0) Quit"
    )
    while True:
        print(menu)
        c = input("> ").strip()

        if c == "1":
            show(tasks)

        elif c == "2":
            title = input("Task: ").strip()
            if title:
                tasks.append(Task(title, ask_priority(), ask_due()))

        elif c in ("3", "4", "5"):
            n = pick(tasks)
            if n is None:
                continue
            if c == "3":
                tasks[n].done = True
            elif c == "4":
                t = tasks[n]
                t.title = input(f"Title [{t.title}]: ").strip() or t.title
                t.priority = ask_priority(t.priority)
                t.due = ask_due(t.due)
            else:
                print(f"Deleted: {tasks.pop(n).title}")

        elif c == "6":
            q = input("Search: ").strip().lower()
            show(tasks, [i for i, t in enumerate(tasks) if q in t.title.lower()])

        elif c == "7":
            by = input("Sort by (p)riority or (d)ue date: ").strip().lower()
            if by == "p":
                tasks.sort(key=lambda t: (t.done, PRIORITY[t.priority]))
            elif by == "d":
                tasks.sort(key=lambda t: (t.done, t.due or date.max))
            show(tasks)

        elif c == "8":
            before = len(tasks)
            tasks = [t for t in tasks if not t.done]
            print(f"Removed {before - len(tasks)} completed task(s).")

        elif c == "9":
            done = sum(t.done for t in tasks)
            overdue = sum(
                1 for t in tasks if t.due and not t.done and t.due < date.today()
            )
            pct = done / len(tasks) * 100 if tasks else 0
            print(
                f"Total: {len(tasks)} | Done: {done} ({pct:.0f}%) | Overdue: {overdue}"
            )

        elif c == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
