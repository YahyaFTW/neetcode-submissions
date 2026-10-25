class Solution {
public:
    int pivotIndex(vector<int>& a) {
        // int sum =0;
        int n = a.size();
        
        vector<int> suf(n);
        vector<int> pre(n);
        pre[0]=a[0];
        suf[n-1]=a[n-1];
        for(int i=1,j=n-2; i<n && j>=0;i++,j--){
            pre[i]=pre[i-1]+a[i];
            suf[j]=suf[j+1]+a[j];
        }

        for(int i=0;i<n;i++){
            if(pre[i]==suf[i]){
                return i;
            }
            // else return -1;
        }
        return -1;

    }
};