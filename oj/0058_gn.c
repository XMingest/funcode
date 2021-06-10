/*
#题目描述
Saya喜欢数学，因为她相信数学使人更有智慧<br>
有一天Kudo提出一个非常简单的游戏：<br>
	给出N个整数，然后玩家从中选择不超过四个可重复的数，将其相加，和更大者胜利，这看上去很简单，但这里还有一个条件，和不能超过M<br>
Saya对此很感兴趣，她说既然给出的数有限，便可以考虑所有情况，找出最大的和，她称之为GN。在一段时间后，Saya给出了GN<br>
Kudo想知道Saya的答案是否是最大的，因此她来找你寻求帮助<br>
你能帮助她计算GN吗
#输入输出
输入包含多个例子<br>
每个例子的第一行包含两个数N\in(0,1000]和M\in(0,1000000000]<br>
接下去的N行各包含一个整数<br>
最后一个例子后会跟着两个零<br>
对每个例子输出Case空格加序号，冒号空格与GN<br>
通常在两个例子之间输出一个空行
##样例
```
#IN
2 10
100
2
0 0
#OUT
Case 1: 8
```
*/
#include <stdio.h>
#include <stdlib.h>

char line[32] = "";
int line_i = 0;

int next_int()
{
    int result = 0;
    while (line[line_i] < '0' || line[line_i] > '9')
    {
        if (line[line_i])
        {
            ++line_i;
        }
        else
        {
            gets(line);
            line_i = 0;
        }
    }
    while (line[line_i] >= '0' && line[line_i] <= '9' && line[line_i]) result = result * 10 + line[line_i++] - '0';
    return result;
}

void quick_sort(int *arr, int il, int ir)
{
    if (il < ir)
    {
        int l = il, r = ir, tmp = arr[il];
        while (l != r)
        {
            while (arr[r] >= tmp && r > l) r--;
            while (arr[l] <= tmp && l < r) l++;
            if (l < r)
            {
                arr[l] += arr[r];
                arr[r] = arr[l] - arr[r];
                arr[l] -= arr[r];
            }
        }
        arr[il] = arr[l];
        arr[l] = tmp;
        quick_sort(arr, il, l - 1);
        quick_sort(arr, l + 1, ir);
    }
}

int main(int argc, char *argv[])
{
    int case_i = 1, case_l, case_num, *case_nums, i, j, m, max_sum, n;

    for (n = next_int(), m = next_int(); n > 0 && m > 0; n = next_int(), m = next_int(), ++case_i)
    {
        case_nums = (int *)malloc(sizeof(int) * (n + 3) * n / 2);

        for (case_l = i = 0; i < n; i++)
        {
            case_num = next_int();
            if (case_num <= m) case_nums[case_l++] = case_num;
        }

        n = case_l;
        for (i = 0; i < n; i++)
            for (j = i; j < n; j++)
            {
                case_num = case_nums[i] + case_nums[j];
                if (case_num <= m) case_nums[case_l++] = case_num;
            }

        j = case_l - 1;
        quick_sort(case_nums, 0, j);
        for (max_sum = case_nums[j]; max_sum > m; max_sum = case_nums[--j]);
        for (i = 0; i <= j; i++)
		{
            for (case_num = case_nums[i] + case_nums[j]; case_num > m && i <= j; case_num = case_nums[i] + case_nums[--j]);
            if (case_num > max_sum) max_sum = case_num;
        }

        printf("Case %d: %d\n\n", case_i, max_sum);
        free(case_nums);
    }

    return 0;
}
