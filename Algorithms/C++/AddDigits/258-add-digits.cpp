class Solution {
public:
    int addDigits(int num) {
        if (num == 0)
            return 0;

        if (num % 10 == num)
            return num;

        return addDigits(num % 10 + int(num/10));
    }
};