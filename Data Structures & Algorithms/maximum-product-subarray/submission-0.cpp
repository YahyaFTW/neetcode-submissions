class Solution {
public:
    int maxProduct(vector<int>& a) {
int bestMax = 1,bestMin=1, ans = a[0];
        for(int i=0;i<a.size();i++){
            int v1=a[i];
            int v2=a[i]*bestMax;
            int v3=a[i]*bestMin;
            bestMax = max(v1, max(v3,v2));
            bestMin = min(v1, min(v3,v2));

            ans = max(ans,max(bestMax, bestMin));
        }
        return ans;
    }
};
