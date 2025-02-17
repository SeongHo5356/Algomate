# https://www.acmicpc.net/problem/1032

def solution(stdin: str) -> str:
    it = iter(stdin.split("\n"))
    next = it.__next__
    result = []

    patterns = [next().strip() for _ in range(int(next()))]
    for idx in range(len(patterns[0])):
        if all(patterns[0][idx] == pattern[idx] for pattern in patterns[1:]):
            result.append(patterns[0][idx])
        else:
            result.append("?")

    return "".join(map(str, result))

if __name__ == "__main__":
    print(solution(open(0).read()))
