from typing import List

def prefixesDivBy5(nums: List[int]) -> List[bool]:
    length_of_nums: int = len(nums)
    string_nums: List[str] = [str(i) for i in nums]
    bool_nums: List[bool] = [False for _ in range(length_of_nums)]
    for i in range(length_of_nums):
        actual_number: str = "".join(string_nums[:i+1])
        decimal: int = int(actual_number,2)
        if decimal % 5 == 0:
            bool_nums[i] = True
    return bool_nums

def main() -> None:
    print(prefixesDivBy5([1,0,1]))

if __name__ == "__main__":
    main()