class Solution {
 public:
  vector<int> findXSum(vector<int>& nums, int k, int x) {
    vector<int> ans;
    long windowSum = 0;
    unordered_map<int, int> count;
    multiset<pair<int, int>> top;  // the top x elements
    multiset<pair<int, int>> bot;  // the rest of the elements
class Solution {
public:
    vector<long long> findXSum(vector<int>& nums, int k, int x) {
        int n = nums.size();
        vector<long long> ans;
        ans.reserve(n - k + 1);

        unordered_map<int,int> cnt; // frequency map
        multiset<pair<int,int>> bot, top; // (freq, value)
        long long sumTop = 0;

        auto removeOld = [&](int val) {
            int c = cnt[val];
            if (c > 0) {
                auto itB = bot.find({c, val});
                if (itB != bot.end()) {
                    bot.erase(itB);
                } else {
                    auto itT = top.find({c, val});
                    if (itT != top.end()) {
                        top.erase(itT);
                        sumTop -= 1LL * c * val;
                    }
                }
            }
        };

        auto addNew = [&](int val) {
            int c = cnt[val];
            if (c > 0) bot.insert({c, val});
        };

        for (int i = 0; i < n; i++) {
            removeOld(nums[i]);
            cnt[nums[i]]++;
            addNew(nums[i]);

            if (i >= k) {
                int outv = nums[i - k];
                removeOld(outv);
                cnt[outv]--;
                if (cnt[outv] > 0) addNew(outv);
            }

            if (i >= k - 1) {
                while (!bot.empty() && (int)top.size() < x) {
                    auto it = prev(bot.end());
                    auto p = *it;
                    bot.erase(it);
                    top.insert(p);
                    sumTop += 1LL * p.first * p.second;
                }

                while (!bot.empty() && !top.empty() && *prev(bot.end()) > *top.begin()) {
                    auto pb = *prev(bot.end());
                    auto pt = *top.begin();
                    bot.erase(prev(bot.end()));
                    top.erase(top.begin());
                    bot.insert(pt);
                    top.insert(pb);
                    sumTop += 1LL * pb.first * pb.second;
                    sumTop -= 1LL * pt.first * pt.second;
                }

                ans.push_back(sumTop);
            }
        }

        return ans;
    }
};

    // Updates the count of num by freq and the window sum accordingly.
    auto update = [&count, &top, &bot, &windowSum](int num, int freq) -> void {
      if (count[num] > 0) {  // Clean up the old count.
        if (auto it = bot.find({count[num], num}); it != bot.end()) {
          bot.erase(it);
        } else {
          it = top.find({count[num], num});
          top.erase(it);
          windowSum -= num * count[num];
        }
      }
      count[num] += freq;
      if (count[num] > 0)
        bot.insert({count[num], num});
    };

    for (int i = 0; i < nums.size(); ++i) {
      update(nums[i], 1);
      if (i >= k)
        update(nums[i - k], -1);
      // Move the bottom elements to the top if needed.
      while (!bot.empty() && top.size() < x) {
        const auto [countB, b] = *bot.rbegin();
        bot.erase(--bot.end());
        top.insert({countB, b});
        windowSum += b * countB;
      }
      // Swap the bottom and top elements if needed.
      while (!bot.empty() && *bot.rbegin() > *top.begin()) {
        const auto [countB, b] = *bot.rbegin();
        const auto [countT, t] = *top.begin();
        bot.erase(--bot.end());
        top.erase(top.begin());
        bot.insert({countT, t});
        top.insert({countB, b});
        windowSum += b * countB;
        windowSum -= t * countT;
      }
      if (i >= k - 1)
        ans.push_back(windowSum);
    }

    return ans;
  }
};

