'''import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = []
    for i in dates:
        dt = datetime.datetime.strptime(i, "%Y-%m-%dT%H:%M:%S")
        months.append(dt.month)

    dic = Counter(months)
    most_common = dic.most_common(n)

    result = [i for i,j in most_common]
    return result


dates=["2023-01-01T23:59:59", "2023-01-01T23:59:59", "2023-02-01T23:59:59"]
print(most_common_months(dates, 2))'''

from collections import deque
from typing import List


def rotate_list(nums: List[int], n: int):
   lst = deque(nums)
   lst.rotate(n)
   return list(lst)

print(rotate_list([1,2,3,4], 2))