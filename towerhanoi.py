step_count = 0


def tower_of_hanoi(n, source, destination, auxiliary,):
    global step_count
    if n == 0:
        return
    tower_of_hanoi(n-1, source, auxiliary, destination, )
    step_count += 1
    print(f"Step {step_count}: Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, destination, source, )

n = 5
tower_of_hanoi(n, 'A', 'C','B')

