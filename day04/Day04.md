# 🏛️ INTELLIGENCE ACADEMY
## The Data Scientist's Bootcamp: Phase 1
### Week 1 Handbook: Python Fundamentals Logic

---

## ▶ Day 4 Lists (Data Structures I)

### 📚 DEEP DIVE: Theory: Mutability Memory

Lists are **Mutable**. This means they can be changed in place.

**The Aliasing Trap:** `A = [1,2], B = A` This does NOT copy the list. It creates a second name for the same list. Modifying B will destroy A.

**Solution:** Always use `B = A.copy()`.

#### Code Examples:

```python
data = [10, 20, 30, 40, 50]

# Slicing (Start:Stop:Step)
subset = data[1:4]  # [20, 30, 40]
reverse = data[::-1]  # [50, 40, 30, 20, 10]

# List Comprehension
# (Action for Item in List if Condition)
squares = [x**2 for x in data]
```

---

### 📚 DEEP DIVE: Micro-Challenge: The Reference Trap

**Goal:** Create a list `a = [1, 2, 3]`. Set `b = a`. Change the first item of b to 99. Print a.

**Observation:** a also changes to [99, 2, 3].

**The Mechanics:** Lists are **"Mutable Objects"**. When you write `b = a`, you are copying the **Reference (Memory Address)**, not the data. Both a and b point to the exact same memory block.

**Fix:** Use `b = a.copy()` or `b = a[:]` to force Python to allocate a new list in memory.
