/*
 * @lc app=leetcode.cn id=745 lang=cpp
 *
 * [745] 前缀和后缀搜索
 */

// @lc code=start
#define TRIEN 29
int mydata[2500*TRIEN]={0},cnt;
class WordFilter {
    void reset(){
        memset(mydata,0,sizeof(mydata));
        cnt=1;
    }
    int* operator[](int i){
        return mydata+i*TRIEN;
    }
    void insert(const string&word,int _signal=1) {
        int cur=0,i=0,j=1<<word.size();
        while(word[i]){
            (*this)[cur][27]=_signal;
            (*this)[cur][28]|=j;
            int&next=(*this)[cur][word[i]-'a'];
            if(!next){
                next=cnt++;
                (*this)[next][26]=-1;
            }
            cur=next;
            i++;
            j>>=1;
        }
        (*this)[cur][26]=(*this)[cur][27]=_signal;
        (*this)[cur][28]|=j;
    }
    void fun(int cur,string&prefix,int i,string&suffix,int j,int&res){
        if((*this)[cur][27]<=res)return;
        if(!((*this)[cur][28]>>(suffix.size()-j)))return;
        if(j&&!((*this)[cur][28]&(1<<(suffix.size()-j))))return;
        if(prefix[i]){
            int next=(*this)[cur][prefix[i]-'a'];
            if(!next)return;
            if(prefix[i]==suffix[j]&&suffix.size()+i>=prefix.size()){
                fun(next,prefix,i+1,suffix,j+1,res);
            }
            if(!j)fun(next,prefix,i+1,suffix,0,res);
        }
        else if(suffix.empty()){
            res=max(res,(*this)[cur][27]);
        }
        else{
            if(!suffix[j])res=max(res,(*this)[cur][26]);
            for(int k=0;k<26;k++){
                int next=(*this)[cur][k];
                if(next){
                    if(k==suffix[j]-'a')fun(next,prefix,i,suffix,j+1,res);
                    fun(next,prefix,i,suffix,0,res);
                }
            }
        }
    }
public:
    WordFilter(vector<string>& words){
        reset();
        for(int i=0;i<words.size();i++){
            insert(words[i],i);
        }
    }
    int f(string&&prefix, string&&suffix) {
        int res=-1;
        fun(0,prefix,0,suffix,0,res);
        return res;
    }
};
//IO
int _IO=[](){
	ios::sync_with_stdio(0);
	cin.tie(0); //cout.tie(0);
	return 0;
}();

/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter* obj = new WordFilter(words);
 * int param_1 = obj->f(prefix,suffix);
 */
// @lc code=end

