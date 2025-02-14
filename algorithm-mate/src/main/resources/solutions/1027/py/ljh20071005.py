def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

n = int(input())
h = list(map(int, input().split()))

max_visible = 0
for i, y1 in enumerate(h):
    x1 = i + 1

    curr_slope_right = None
    vis_right = 0
    for j in range(i + 1, n):
        x2 = j + 1
        y2 = h[j]
        slope_right = slope(x1, y1, x2, y2)
        if curr_slope_right is None or curr_slope_right < slope_right:
            curr_slope_right = slope_right
            vis_right += 1

    curr_slope_left = None
    vis_left = 0
    for j in range(i - 1, -1, -1):
        x2 = j + 1
        y2 = h[j]
        slope_left = slope(x1, y1, x2, y2)
        if curr_slope_left is None or curr_slope_left > slope_left:
            curr_slope_left = slope_left
            vis_left += 1

    max_visible = max(max_visible, vis_left + vis_right)

print(max_visible)
