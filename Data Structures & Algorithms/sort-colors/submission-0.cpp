class Solution {
public:
    void sortColors(vector<int>& a) {
        int n = a.size()-1;
        int mid =0, low =0, high =n;

    while (mid<=high){
            if(a[mid]==0){
                swap(a[mid],a[low]);
                low++;
                mid++;
            }else if( a[mid]==1){
                mid++;
            }
            else{
                swap(a[mid],a[high]);
                high--;
            }
        }
    }
};