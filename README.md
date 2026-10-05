# SLE-2: Empirical Performance Analysis Report
---

## 1. Algorithms Used
- **Algorithm A:** BFS (Breadth-First Search)
- **Algorithm B:** DFS (Depth-First Search)
- **Problem Configuration:** Graph with 100 nodes (Start Node = 0, Goal Node = 99)

---

## 2. Profiling Method
The performance of BFS and DFS was measured using Python's `timeit` module and a manual node-expansion counter.
1. A graph with 100 nodes was constructed programmatically.
2. BFS and DFS were evaluated on three test cases: Best Case (Goal = 1), Average Case (Goal = 50), and Worst Case (Goal = 99).
3. Execution time was measured across 3 runs for each test case, and average execution time in milliseconds (ms) was computed.
4. Nodes expanded were recorded for each traversal.

---

## 3. Experimental Results

| Case | Algorithm | Goal | Average Time (ms) | Nodes Expanded | Better ? |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Best** | BFS | 1 | 0.18633 | 2 | **DFS** |
| **Best** | DFS | 1 | 0.14717 | 2 | **DFS** |
| **Average** | BFS | 50 | 2.45097 | 51 | **DFS** |
| **Average** | DFS | 50 | 1.03097 | 21 | **DFS** |
| **Worst** | BFS | 99 | 5.32800 | 100 | **DFS** |
| **Worst** | DFS | 99 | 2.12863 | 43 | **DFS** |

### Short Observation:
DFS showed lower measured execution time than BFS in all three selected cases. In the average and worst cases, DFS also expanded fewer nodes than BFS. Both algorithms successfully found the goal node.

---

## 4. Justification & Analysis
The profiling results show that DFS performed faster than BFS for the selected graph and test cases. 
- In the **Best Case** (Goal = 1), both algorithms expanded 2 nodes, while DFS had a lower average execution time of `0.14717 ms` compared to BFS at `0.18633 ms`.
- In the **Average Case** (Goal = 50), BFS took `2.45097 ms` and expanded 51 nodes, whereas DFS took `1.03097 ms` and expanded 21 nodes.
- In the selected **Worst Case** (Goal = 99), BFS took `5.32800 ms` and expanded 100 nodes, while DFS took `2.12863 ms` and expanded 43 nodes.

Thus, for this particular graph structure and traversal order, DFS showed lower measured execution time and fewer expanded nodes in the average and worst cases.

---

## 5. AI Contribution Note
- **AI Tools Used:** Gemini
- **What AI helped with:** AI helped in preparing the BFS and DFS profiling code, setting up `timeit` execution-time measurement, adding node counting, and organizing the report.
- **What I did myself:** I executed the program, ran BFS and DFS three times, collected the actual results, and performed the comparison and analysis based on the measured values.

---

## 6. Conclusion
This profiling exercise helped me understand the practical performance difference between BFS and DFS. I learned how `timeit` can be used to measure execution time and how node expansion can be used for comparison. For the selected graph and test cases, DFS showed lower measured execution time than BFS. The experiment also showed that profiling results depend on the graph structure and traversal order.