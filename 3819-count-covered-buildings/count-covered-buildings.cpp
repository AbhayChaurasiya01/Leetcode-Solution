class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        unordered_map<int, int> leftmost, rightmost;
        unordered_map<int, int> topmost, bottommost;

        // Initialize boundaries
        for (auto& b : buildings) {
            int r = b[0], c = b[1];

            if (!leftmost.count(r) || c < leftmost[r]) leftmost[r] = c;
            if (!rightmost.count(r) || c > rightmost[r]) rightmost[r] = c;

            if (!topmost.count(c) || r < topmost[c]) topmost[c] = r;
            if (!bottommost.count(c) || r > bottommost[c]) bottommost[c] = r;
        }

        int covered = 0;

        for (auto& b : buildings) {
            int r = b[0], c = b[1];

            bool hasLeft = (c > leftmost[r]);
            bool hasRight = (c < rightmost[r]);
            bool hasTop = (r > topmost[c]);
            bool hasBottom = (r < bottommost[c]);

            if (hasLeft && hasRight && hasTop && hasBottom)
                covered++;
        }

        return covered;
    }
};
