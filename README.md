# To-Do List (Python)

A command-line to-do list app written in Python. It uses only the standard library, so there is nothing to install.

## Features

- Add, edit, complete and delete tasks
- Priorities: `high`, `medium`, `low`
- Optional due dates, with an automatic `(OVERDUE)` flag
- Search tasks by title
- Sort by priority or due date (completed tasks go last)
- Clear all completed tasks
- Stats: total tasks, percent done, overdue count
- Input validation: bad menu choices, task numbers and dates do not crash the app

## Requirements

Python 3.10 or newer (the code uses the `date | None` type hint).

## Run

```bash
python todolist.py
```

## Menu

| Key | Action | What it does |
|-----|--------|--------------|
| 1 | Show | List all tasks |
| 2 | Add | Add a task (title, priority, optional due date) |
| 3 | Complete | Mark a task as done |
| 4 | Edit | Change title, priority or due date (press Enter to keep the current title or priority) |
| 5 | Delete | Remove a task |
| 6 | Search | Find tasks whose title contains some text |
| 7 | Sort | Sort by `p` (priority) or `d` (due date) |
| 8 | Clear done | Remove all completed tasks |
| 9 | Stats | Show totals, percent done and overdue count |
| 0 | Quit | Exit the program |

Task format: `[ ]` means open, `[x]` means done, followed by the title, `<priority>` and the due date.

## Examples

Each example below is real output from the program. Lines after a prompt (for example `> 2`) are what the user typed.

### 1. Add and show a task

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 1
Nothing to show.

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: 2+3
Priority (high/medium/low) [medium]: low
Due date YYYY-MM-DD (blank = none): 2026-11-16

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 1
1. [ ] 2+3 <low> | due 2026-11-16

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 2. Add several tasks, then complete one

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Buy milk
Priority (high/medium/low) [medium]: low
Due date YYYY-MM-DD (blank = none): 2026-12-01

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Finish report
Priority (high/medium/low) [medium]: high
Due date YYYY-MM-DD (blank = none): 2026-11-30

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 3
1. [ ] Buy milk <low> | due 2026-12-01
2. [ ] Finish report <high> | due 2026-11-30
Task number: 1

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 1
1. [x] Buy milk <low> | due 2026-12-01
2. [ ] Finish report <high> | due 2026-11-30

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 3. Edit a task

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Call mom
Priority (high/medium/low) [medium]: 
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 4
1. [ ] Call mom <medium>
Task number: 1
Title [Call mom]: Call mom tonight
Priority (high/medium/low) [medium]: high
Due date YYYY-MM-DD (blank = none): 2026-11-20

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 1
1. [ ] Call mom tonight <high> | due 2026-11-20

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 4. Delete a task

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Old task
Priority (high/medium/low) [medium]: 
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 5
1. [ ] Old task <medium>
Task number: 1
Deleted: Old task

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 1
Nothing to show.

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 5. Search

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Buy milk
Priority (high/medium/low) [medium]: 
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Buy bread
Priority (high/medium/low) [medium]: 
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Call mom
Priority (high/medium/low) [medium]: 
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 6
Search: buy
1. [ ] Buy milk <medium>
2. [ ] Buy bread <medium>

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 6. Sort by priority and by due date

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Low one
Priority (high/medium/low) [medium]: low
Due date YYYY-MM-DD (blank = none): 2026-12-20

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: High one
Priority (high/medium/low) [medium]: high
Due date YYYY-MM-DD (blank = none): 2026-12-31

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Medium one
Priority (high/medium/low) [medium]: medium
Due date YYYY-MM-DD (blank = none): 2026-12-05

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 7
Sort by (p)riority or (d)ue date: p
1. [ ] High one <high> | due 2026-12-31
2. [ ] Medium one <medium> | due 2026-12-05
3. [ ] Low one <low> | due 2026-12-20

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 7
Sort by (p)riority or (d)ue date: d
1. [ ] Medium one <medium> | due 2026-12-05
2. [ ] Low one <low> | due 2026-12-20
3. [ ] High one <high> | due 2026-12-31

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 7. Overdue tasks and stats

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Pay bill
Priority (high/medium/low) [medium]: high
Due date YYYY-MM-DD (blank = none): 2026-11-10

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Read book
Priority (high/medium/low) [medium]: low
Due date YYYY-MM-DD (blank = none): 2026-12-25

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Clean room
Priority (high/medium/low) [medium]: medium
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 3
1. [ ] Pay bill <high> | due 2026-11-10 (OVERDUE)
2. [ ] Read book <low> | due 2026-12-25
3. [ ] Clean room <medium>
Task number: 3

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 9
Total: 3 | Done: 1 (33%) | Overdue: 1

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 8. Clear completed tasks

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Task A
Priority (high/medium/low) [medium]: 
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Task B
Priority (high/medium/low) [medium]: 
Due date YYYY-MM-DD (blank = none): 

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 3
1. [ ] Task A <medium>
2. [ ] Task B <medium>
Task number: 1

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 8
Removed 1 completed task(s).

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 1
1. [ ] Task B <medium>

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

### 9. Invalid input is handled

```text
1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> x
Invalid choice.

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 3
Nothing to show.
Task number: abc
Invalid number.

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 2
Task: Bad date task
Priority (high/medium/low) [medium]: urgent
Due date YYYY-MM-DD (blank = none): not-a-date
Bad date, ignoring.

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 1
1. [ ] Bad date task <medium>

1) Show  2) Add  3) Complete  4) Edit  5) Delete
6) Search  7) Sort  8) Clear done  9) Stats  0) Quit
> 0
```

## Notes

- Tasks are kept in memory only. They are lost when you quit.
- The `(OVERDUE)` flag compares the due date with today's date, so the same task may or may not be overdue depending on when you run the program.
- A task title is plain text. Typing `2+3` as a title stores the text `2+3`; it does not calculate anything.
