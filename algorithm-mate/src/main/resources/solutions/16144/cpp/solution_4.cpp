#include <iostream>
using namespace std;

int n, arr[100];

bool test_1(int x, int y);
bool test_2(int x, int y);

int main()
{
    ios::sync_with_stdio(false), cin.tie(0);
    int i, j;
    cin >> n;
    for (i = 0; i < n; i++)
        cin >> arr[i];
    for (i = 1; i < n; i++)
        if (arr[i] < arr[i - 1])
        {
            cout << "fail";
            return 0;
        }
    for (i = 0; i < n; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (test_1(i, j) || test_2(i, j))
            {
                cout << "pass";
                return 0;
            }
        }
    }

    cout << "fail";
    return 0;
}

bool test_1(int x, int y)
{
    int a = arr[y] - arr[x], b = y - x, i;
    for (i = 0; i < n; i++)
    {
        if (b * arr[i] <= arr[x] * b + a * (i - x) && arr[x] * b + a * (i - x) < b * (arr[i] + 1))
            continue;
        return false;
    }
    return true;
}

bool test_2(int x, int y)
{
    int a = arr[y] + 1 - arr[x], b = y - x, i, tmp[4] = {999, -1, 999, -1};
    for (i = 0; i < x; i++)
    {
        if (b * arr[i] <= arr[x] * b + a * (i - x) && arr[x] * b + a * (i - x) < b * (arr[i] + 1))
            continue;
        return false;
    }
    for (i++; i < y; i++)
    {
        if (b * arr[i] < arr[x] * b + a * (i - x) && arr[x] * b + a * (i - x) < b * (arr[i] + 1))
            continue;
        if (b * arr[i] == arr[x] * b + a * (i - x))
            tmp[0] = min(i, tmp[0]), tmp[1] = max(i, tmp[1]);
        else if (arr[x] * b + a * (i - x) == b * (arr[i] + 1))
            tmp[2] = min(i, tmp[2]), tmp[3] = max(i, tmp[3]);
        else
            return false;
    }
    if (tmp[1] != -1 && tmp[3] != -1 && ((tmp[0] < tmp[2] && tmp[2] < tmp[1]) || (tmp[2] < tmp[0] && tmp[0] < tmp[3])))
        return false;
    for (i++; i < n; i++)
    {
        if (b * arr[i] < arr[x] * b + a * (i - x) && arr[x] * b + a * (i - x) <= b * (arr[i] + 1))
            continue;
        return false;
    }

    return true;
}