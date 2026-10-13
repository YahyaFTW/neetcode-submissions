class Solution {
public:
    bool cond(vector<int> &s,vector<int> &t ){
        for(int i=0;i<256;i++){
            if(t[i]>s[i]){
                return false;
            }
        }
            return true;
    }

    string minWindow(string s, string t) {
        vector<int> s_array(256,0);
        vector<int> t_array(256,0);

        int high=0, low=0, res = INT_MAX;
        int n= s.size(), m=t.size();
        for(int i=0;i<m;i++){
            t_array[t[i]]++;
        }
            int start =0;
            int len=0;
        for(;high<n;high++){
            
            s_array[s[high]]++;
            while(cond(s_array, t_array)){
                len = high - low +1 ;
                if(len<res){
                    res=len;
                    start = low;
                }
                s_array[s[low]]--;
                low++;
            }
            // res=min(len,res);

        }
        if(res==INT_MAX)
        return "";
        return s.substr(start,res);
    }
};