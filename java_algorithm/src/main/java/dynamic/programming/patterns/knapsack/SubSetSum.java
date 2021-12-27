package dynamic.programming.patterns.knapsack;

public class SubSetSum {

    static boolean canPartition(int[] num, int sum) {
        return canPartitionBySubArray(num, sum, 0);
    }

    private static boolean canPartitionBySubArray(int[] num, int sum, int i) {
        if (i == num.length) {
            return sum == 0;
        }
        if (num[i] > sum) {
            return canPartitionBySubArray(num, sum, i + 1);
        } else {
            return canPartitionBySubArray(num, sum, i + 1) || canPartitionBySubArray(num, sum - num[i], i + 1);
        }
    }

    public static void main(String[] args) {
//        int[] num = {2, 3, 6, 1, 8};
//        int sum = 10;
//        int[] num = {1, 2, 3, 7};
//        int sum = 6;
//        int[] num = {1, 2, 7, 1, 5};
//        int sum = 10;
        int[] num = {1, 3, 4, 8};
        int sum = 6;
        System.out.println(canPartition(num, sum));
    }
}
