import latinsq
import numpy as np

N = 4
N_AS_FLOAT_LIST = [float(i) for i in range(1, N)]

def check_valid(candidate_cube: np.array) -> bool:
    for i in range(N):
        for j in range(N):
            col_check = candidate_cube[i, j, :]
            unique_numbers = np.unique(col_check)
            if unique_numbers.size != col_check.size:
                return False
    return True

def finalize_cube(candidate_cube: np.array) -> np.array:
    last_slice = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            col_check = candidate_cube[i, j, :]
            missing_number = set(range(1, N+1)) - set(col_check)
            last_slice[i][j] = missing_number.pop()
    return np.concatenate(
        (candidate_cube, last_slice[:, :, np.newaxis]), 
        axis=2
    )

def generate_latin_square():
    return latinsq.LatinSquare.random(n=N).square

def generate_latin_cube():
    cube = np.zeros((N, N, 0))
    for _ in range(N - 1):
        valid_slice = False
        while not valid_slice:
            candidate_slice = generate_latin_square()
            candidate_cube = np.concatenate(
                (cube, candidate_slice[:, :, np.newaxis]), 
                axis=2
            )
            if check_valid(candidate_cube=candidate_cube):
                cube = candidate_cube
                valid_slice = True
    
    cube = finalize_cube(candidate_cube=cube)
    return cube