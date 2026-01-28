from src.analysis import read_trace, summarize_trace
from src.plot import plot_summary
from src.report import save_report

# Run example program first, then analyze
trace_file = "results/trace_log.txt"
df = read_trace(trace_file)
summary = summarize_trace(df)
plot_summary(summary)
save_report(df, summary)

print("✅ TRACE Analysis Complete! Check results folder")
