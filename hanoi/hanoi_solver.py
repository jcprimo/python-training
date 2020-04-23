from hanoi import towers_manipulation
import os
from hanoi import hanoi_ascii
import time


# Plain and simple on how to create a tower
# Creates each row to draw on the screen
def create_hanoi_tower(tower_size):
    res_tower = []
    for i in range(1, tower_size + 1):
        res_tower.append(i)
    return res_tower


# This is the guts and main algorithm of the solver
def hanoi_solver_aux(tower, dep, arr, mid, solution):
    tower_size = len(tower)

    # Base Case
    if tower_size == 1:
        solution.append((tower[0], dep, arr))
    else:
        last_ring = len(tower) - 1
        new_tower = tower[:last_ring]
        temp_solution = hanoi_solver_aux(new_tower, dep, mid, arr, solution)
        temp_solution.append((tower[last_ring], dep, arr))
        solution = hanoi_solver_aux(new_tower, mid, arr, dep, temp_solution)
    return solution


# What is it returning?
def hanoi_solver(tower_size):
    # Passing the three towers and an empty solution
    return hanoi_solver_aux(create_hanoi_tower(tower_size), "A", "B", "C", [])


def print_solution(solution_list):
    list_max_index = len(solution_list)
    for i in range(0, list_max_index):
        print(solution_list[i])


def solution_animation_speed(difficulty_level):
    return {"1": 1,
            "2": 1,
            "3": 1,
            "4": 0.75,
            "5": 0.75,
            "6": 0.1,
            "7": 0.01}[difficulty_level]


def play_solution(tower_size, speed):
    tower1 = create_hanoi_tower(tower_size)
    tower2 = towers_manipulation.create_no_ring_hanoi_tower(tower_size)
    tower3 = towers_manipulation.create_no_ring_hanoi_tower(tower_size)
    towers = [tower1, tower2, tower3]

    # 2 * n -1 where n is towers
    solution_length = 2 ** tower_size - 1  # so 5 is the solution length?

    # Here is where the solution begins
    solution_recipe = hanoi_solver(tower_size)

    os.system("clear")
    print("\n")
    hanoi_ascii.print_towers(towers)
    print("")
    time.sleep(speed)
    os.system("clear")

    for i in range(solution_length):
        if i == solution_length - 1:
            move_and_print(2, solution_recipe, towers, i)
        else:
            move_and_print(speed, solution_recipe, towers, i)


def move_and_print(speed, solution_recipe, towers, index):
    targeted_tower = towers_manipulation.translate_tower_index(solution_recipe[index][2])
    ring_move = [solution_recipe[index][0], targeted_tower]
    towers_manipulation.move_ring(ring_move, towers)
    print("\n")
    hanoi_ascii.print_towers(towers)
    print("")
    time.sleep(speed)
    os.system("clear")
