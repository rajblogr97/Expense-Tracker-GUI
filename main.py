import tkinter as tk
from tkinter import messagebox

# ================= DATA =================
expense_list = []

# ================= WINDOW =================
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("900x600")
root.config(bg="#090b0b")

# ================= TITLE =================
title = tk.Label(
    root,
    text= "💰 Expense Tracker", 
    font=("Arial", 30, "bold"),
    bg="#060202",
    fg="white",
    pady=15
)
title.pack(fill="x")

# ================= FORM FRAME =================
form = tk.Frame(root, bg="#070202", bd=3, relief="ridge")
form.pack(pady=20)

tk.Label(form, text="Date", font=("Arial", 14), bg="white").grid(row=0, column=0, padx=10, pady=5)
tk.Label(form, text="Category", font=("Arial", 14), bg="white").grid(row=1, column=0, padx=10, pady=5)
tk.Label(form, text="Description", font=("Arial", 14), bg="white").grid(row=2, column=0, padx=10, pady=5)
tk.Label(form, text="Amount (₹)", font=("Arial", 14), bg="white").grid(row=3, column=0, padx=10, pady=5)

date_entry = tk.Entry(form, font=("Arial", 14))
cat_entry = tk.Entry(form, font=("Arial", 14))
desc_entry = tk.Entry(form, font=("Arial", 14))
amt_entry = tk.Entry(form, font=("Arial", 14))

date_entry.grid(row=0, column=1, padx=10)
cat_entry.grid(row=1, column=1, padx=10)
desc_entry.grid(row=2, column=1, padx=10)
amt_entry.grid(row=3, column=1, padx=10)

# ================= OUTPUT BOX =================
output = tk.Text(root, height=10, font=("Consolas", 12))
output.pack(pady=15, fill="x", padx=20)

# ================= FUNCTIONS =================
def add_expense():
    try:
        expense = {
            "date": date_entry.get(),
            "category": cat_entry.get(),
            "description": desc_entry.get(),
            "amount": float(amt_entry.get())
        }
        expense_list.append(expense)
        messagebox.showinfo("Success", "Expense Added Successfully ✅")

        date_entry.delete(0, "end")
        cat_entry.delete(0, "end")
        desc_entry.delete(0, "end")
        amt_entry.delete(0, "end")

    except:
        messagebox.showerror("Error", "Please enter valid data")

def view_all():
    output.delete("1.0", "end")
    if not expense_list:
        output.insert("end", "No expenses recorded\n")
    else:
        for i, e in enumerate(expense_list, start=1):
            output.insert("end", f"{i}. {e['date']} | {e['category']} | {e['description']} | ₹{e['amount']}\n")

def total_spending():
    total = 0
    for e in expense_list:
        total += e["amount"]
    messagebox.showinfo("Total Spending", f"💰 Total = ₹{total}")

def category_summary():
    summary = {}
    for e in expense_list:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]

    output.delete("1.0", "end")
    for cat, amt in summary.items():
        output.insert("end", f"{cat} : ₹{amt}\n")

# ================= BUTTONS =================
btn_frame = tk.Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

def colorful_button(text, cmd, color):
    return tk.Button(
        btn_frame,
        text=text,
        font=("Arial", 14, "bold"),
        bg="#060414",
        fg="white",
        activebackground="#000000",
        cursor="hand2",
        width=18,
        command=cmd
    )

colorful_button("➕ Add Expense", add_expense, "#4caf50").grid(row=0, column=0, padx=10, pady=5)
colorful_button("📄 View Expenses", view_all, "#2196f3").grid(row=0, column=1, padx=10, pady=5)
colorful_button("💰 Total Spending", total_spending, "#ff9800").grid(row=1, column=0, padx=10, pady=5)
colorful_button("📊 By Category", category_summary, "#9c27b0").grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
