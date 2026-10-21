constexpr int nn=317, N=1e5;
bitset<N> sieve;
vector<int> prime={2,3,5,7,11,13,17};
void Sieve(){
    if (prime.back()!=17) return ;
    sieve[0]=sieve[1]=1;
    for(int p: prime){
        for(int j=p*p; j<nn; j+=p) sieve[j]=1;
    }
    for(int p=19; p<nn; p+=2){
        if(!sieve[p]) prime.push_back(p);
    }
//    cout<<prime.size();
}
int inc2[N];
using int2=pair<int, int>; 
class Solution {
public:
    static vector<int2> factorize(int x) {
        vector<int2> ans;
        int y=x;
        for (int p : prime) {
            if (p*p>y) break;
            if (y%p==0) {
                int e=0;
                for (; y%p == 0; y/=p, e++);
                ans.push_back({p, e});
            }
        }
        if (y>1) ans.push_back({y, 1});
        return ans;
    }
    static void get_divs(int idx, int cur, const vector<int2>& Div, vector<int>& divs) {
        if (idx==Div.size()) {
            divs.push_back(cur);
            return;
        }
        auto [p, e]=Div[idx];
        int pp=1;
        for (int i=0; i<=e; i++) {
            get_divs(idx+1, cur*pp, Div, divs);
            pp*=p;
        }
    }

    // return minmax for this interval if possible to make increasing
    // by cyclic rotations
    static int2 cyclic_rot(int l, int r, vector<int>& nums){
        if (inc2[l]>=r) return {nums[l], nums[r]};// increasing
        int m=inc2[l], r2=inc2[m+1];
        if (r2<r) return {-1, -1}; // impossible to make increasing
        if (nums[r]<=nums[l]) return {nums[m+1], nums[m]};
        return {-1, -1}; // impossible
    }
    static int sortableIntegers(vector<int>& nums) {
        Sieve();
        const int n=nums.size();
        int t=nums[n-1], idx=n-1;
        inc2[n-1]=n-1;
        for(int i=n-2; i>=0; i--){
            inc2[i]=(nums[i]<=nums[i+1])? inc2[i+1] : i;
        }
        vector<int2> Div=factorize(n);
        vector<int> divs;
        get_divs(0, 1, Div, divs);

        int sum=0;
        for (int k : divs) {
            bool ok=1;
            int prev_max=-1;

            for (int i=0; i<n; i+=k) {
                int l=i, r=i+k-1;
                auto [mn, mx]=cyclic_rot(l, r, nums);
                if (mn==-1 || prev_max>mn) {
                    ok=0;
                    break;
                }
                prev_max=mx;
            }
            if (ok) sum+=k;
        }
        return sum;
    }
};