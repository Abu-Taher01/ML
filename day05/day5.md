# 🏛️ INTELLIGENCE ACADEMY
## The Data Scientist's Bootcamp: Phase 1
### Week 1 Handbook: Python Fundamentals Logic

---

## ▶ Day 5 Dictionaries (Hash Maps)

### 📚 DEEP DIVE: Theory: Hash Tables

A Dictionary is a Key-Value store. It is optimized for **O(1) Lookup**.
When you search a List, Python scans left-to-right ($O(N)$). When you search a Dictionary, Python uses a "Hash Function" to calculate exactly where the data is in memory. It is instant, even with 1 million items.

```python
user = {"id": 1, "name": "Admin"}

# Safe Access (.get)
# Returns None if key missing, prevents crash
email = user.get("email", "No Email Found")

# Iteration
for key, val in user.items():
	print(f"{key}: {val}")
```

---

### 📚 DEEP DIVE: Micro-Challenge: The Speed Trap (Lookup)

**Goal:** Create a list of 1 million numbers. Create a set (hash table) of the same numbers. Check if the number -1 exists in both.
**Constraint:** You don’t need to actually run 1M items, but explain why the Set/Dict is faster.
**The Mechanics:**

- **List Search ($O(N)$):** Python must scan item 1, item 2, item 3... until the end.
- **Dict/Set Search ($O(1)$):** Python runs `hash(-1)`, gets a memory address (e.g., 0x99), and looks only at that spot. It is instant.

---
