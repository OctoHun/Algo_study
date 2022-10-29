from sys import stdin

number_of_samples = stdin.readline()
samples = sorted(map(int, stdin.readline().split()))
number_of_targets = stdin.readline()
targets = map(int, stdin.readline().split())

def binary(target, samples, start, end):
    if start > end:
        return 0
    location = (start + end) // 2
    if target == samples[location]:
        return 1
    elif target < samples[location]:
        return binary(target, samples, start, location - 1)
    else:
        return binary(target, samples, location + 1, end)

for target in targets:
    start = 0
    end = len(samples) - 1
    print(binary(target, samples, start, end))