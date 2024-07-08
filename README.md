Overview: This project focuses on applying AI search and optimization techniques to solve a 3D Traveling Salesman Problem (TSP). The goal is to develop a genetic algorithm that finds the shortest path for a student to run errands across a campus, visiting each location exactly once and returning to the starting point.

Locations: Represented as 3D coordinates (x, y, z) indicating points on a grid.

Objective: Find the shortest path that visits each location once and returns to the start.

Initial Population: Generate an initial set of random or heuristically determined paths.

Parent Selection: Implement a Roulette wheel selection method to choose parents for breeding based on fitness scores.

Crossover: Use a two-point crossover method to create a child path by combining segments from two parent paths, ensuring each city is visited once.

Mutation: Introduce random changes to paths to maintain genetic diversity.

Fitness Function: Calculate the total distance of the path to evaluate its fitness.

Performance Metrics: Evaluate the quality of the paths based on the total distance.
