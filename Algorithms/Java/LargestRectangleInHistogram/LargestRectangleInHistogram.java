class Solution {
    public int largestRectangleArea(int[] arr) {
        int n=arr.length;
        int[]left=new int[n];
        int[]right=new int[n];

        for(int i=0;i<n;i++){
            int p=i-1;
            while(p>=0&&arr[p]>=arr[i])p=left[p];
            left[i]=p;
        }
        for(int i=n-1;i>=0;i--){
            int p=i+1;
            while(p<n&&arr[p]>=arr[i])p=right[p];
            right[i]=p;
        }
        int ans=0;
        for(int i=0;i<n;i++){
            ans=Math.max(ans,(right[i]-left[i]-1)*arr[i]);
        }
        return ans;
    }
}