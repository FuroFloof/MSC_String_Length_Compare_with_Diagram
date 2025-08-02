#!/usr/bin/env python3
"""
size_visualizer.py

Ask the user for two strings, measure their sizes (bytes, not characters),
and pop up a window that shows how much of the total each one occupies.
"""

import matplotlib.pyplot as plt

def main() -> None:
    # --- 1. Collect the two substrings --------------------------------------
    s1 = input("Enter the FIRST string  ➜ ")
    s2 = input("Enter the SECOND string ➜ ")

    # --- 2. Measure their size in *bytes* (safer than len(str) for non-ASCII) -
    len1 = len(s1.encode("utf-8"))
    len2 = len(s2.encode("utf-8"))
    total = len1 + len2 or 1            # avoid division-by-zero if both empty

    # --- 3. Build one quick visual ------------------------------------------
    sizes  = [len1, len2]
    labels = [
        f"String 1 – {len1} B ({len1/total:.1%})",
        f"String 2 – {len2} B ({len2/total:.1%})",
    ]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(
        sizes,
        labels=labels,
        autopct=lambda pct: f"{pct:.1f} %",
        startangle=90,
    )
    ax.set_title(f"Relative size (Total {total} bytes)")
    ax.axis("equal")                    # keep the pie a circle
    plt.show()

if __name__ == "__main__":
    main()
