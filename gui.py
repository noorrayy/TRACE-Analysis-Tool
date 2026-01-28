import tkinter as tk
from tkinter import filedialog, messagebox
from src.analysis import read_trace, summarize_trace
from src.plot import plot_summary
from src.report import save_report

def run_gui_analysis():
    trace_file = filedialog.askopenfilename(filetypes=[("Trace Log","*.txt")])
    if not trace_file:
        return
    df = read_trace(trace_file)
    summary = summarize_trace(df)
    plot_summary(summary)
    save_report(df, summary)
    messagebox.showinfo("Done", "✅ TRACE Analysis Complete! Check results folder")

root = tk.Tk()
root.title("TRACE Analysis Tool Advanced")
root.geometry("400x200")

label = tk.Label(root, text="TRACE Analysis Tool - Advanced", font=("Arial",16))
label.pack(pady=20)

button = tk.Button(root, text="Select Trace Log & Analyze", command=run_gui_analysis)
button.pack(pady=20)

root.mainloop()
