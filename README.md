# solving-subset-sum-problem-using-quantum-annealing
Quantum annealing for solving subset sum problem

# Usage

1. You need to get D-Wave Token from [Dwave System](https://www.dwavesys.com/).

2. git clone and change directory as below.

   ```
   git clone https://github.com/428lab/solving-subset-sum-problem-using-quantum-annealing.git
   cd solving-subset-sum-problem-using-quantum-annealing
   ```

3. create .env file and write your token as below.

   ```
   D_WAVE_TOKEN='YOUR_TOKEN'
   ```

4. run solver

   ```
   python solver.py --annealing-time 40 --penalty-scale 10
   ```

   You may need to adjust parameters.

5. You may see following output in standard out. 

   ```
   Found exact solution: [1, 2, 10, 17, 18, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [2, 3, 8, 17, 18, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [1, 6, 14, 15, 17, 18, 20, 21, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [8, 9, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [1, 2, 6, 8, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [1, 2, 6, 8, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [2, 14, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49]
   Found exact solution: [3, 6, 8, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [5, 8, 17, 18, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [4, 8, 9, 15, 17, 18, 20, 21, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found exact solution: [2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49]
   Found solution with deviation: [1, 14, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 2, 3, 9, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [14, 17, 18, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [7, 8, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 2, 14, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [15, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 2, 14, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 9, 17, 18, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [8, 9, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [8, 14, 15, 17, 18, 20, 21, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [15, 17, 20, 21, 24, 25, 30, 33, 38, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [2, 6, 8, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 8, 9, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [2, 6, 8, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   Found solution with deviation: [1, 8, 9, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 6, 8, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 2, 14, 15, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [14, 17, 18, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 501
   Found solution with deviation: [1, 3, 4, 8, 14, 17, 20, 21, 23, 24, 25, 30, 33, 42, 44, 46, 47, 48, 49] Sum: 499
   
   ```

   
