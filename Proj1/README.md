# Libraries

If you do not have any of the following libraries installed, please run the command:

|     Name    |   Command   |
| ----------- | ----------- |
| mathplotlib | `pip install mathplotlib`|
| numpy       | `pip install numpy` |

# File structure

- Dataset files are located at [input](input/) 
- Implementation of the algorithms is done at [algos](algos/)
- Neighbourhood generation and evaluation functions are developped at [solution](formulationsolution.py)
- Logic for reading from dataset and structuring classses is at [utils](utils/utils.py)

# Compilation and Execution

Run `python3 -B main.py` or `py -B main.py` on the terminal.

# Usage

After running any of the commands above, you should be presented with some instructions on how to run the program:

1. You should input the dataset letter without extension( from 'a' to 'c').
2. After that, you should choose the cooling algorithm to be used for the Simulated Annealing.
3. Choose the size of the population to be used in the Genetic Algorithm
4. Choose a selection method for the Genetic Algorithm, either tournament or roulette.
5. Choose a crossover function for the Genetic Algorithm

# Results and Plots

After following the steps mentioned above, the solution for each algorithm is going to be shown in the terminal, with the following syntax:

```
[[0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
```

The team is composed by 4 members and has been assigned 3 projects. The first one could not be completed due to lack of skills from the members. Member number 2 has been assigned to both second and third projects, while member number 1 has been also assigned to the third project.

Two plots are presented:
- [iterations](output/iterations.png) details the evalution of each algorithm throughout the many iterations. 
- [best_evaluation](output/best_evaluation.png) is a bar chart that has the best evaluation that each of the algorithms manage to hit.

