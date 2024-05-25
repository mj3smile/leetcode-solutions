/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize=2;
    int *result = malloc(2 * sizeof(int));

    for (int i = 0; i < numsSize; i++)
    {
        for (int j = 1 + i; j < numsSize; j++)
        {
            if (nums[i] + nums[j] == target)
            {
                result[0]=i;
                result[1]=j;
                return result;
            }
        }
    }

    return result;
}