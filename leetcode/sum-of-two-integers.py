class Solution {
    public int getSum(int a, int b) {
        // Keep looping until there is no carry left
        while (b != 0) {
            // temp holds the carry:
            // (a & b) finds all bits where both a and b have 1s
            // << 1 shifts the carry left by one bit
            int temp = (a & b) << 1;

            // XOR gives the sum without carrying:
            // like binary addition without handling carries
            a = a ^ b;

            // set b to carry (temp), so it will be added in the next iteration
            b = temp;
        }
        // When carry becomes 0, 'a' contains the final sum
        return a;
    }
}