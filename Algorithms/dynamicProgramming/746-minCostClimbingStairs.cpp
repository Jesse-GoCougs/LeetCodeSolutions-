#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();

        // Initialize base cases for steps 0 and 1
        int first = cost[0];
        int second = cost[1];

        // Loop through each step starting from the third step
        for (int i = 2; i < n; i++) {
            int current = min(first, second) + cost[i];
            first = second;  // Move the first pointer up by one step
            second = current;  // Move the second pointer up by one step
        }

        // Return the minimum cost to reach the top of the floor
        return min(first, second);
    }
};