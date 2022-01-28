class Solution {
    public int findMaximumXOR(int[] arr) {
        int maxx = 0, mask = 0;
        int n = arr.length;

        HashSet<Integer> se = new HashSet<Integer>();

        for (int i = 30; i >= 0; i--){
            mask |= (1 << i);

            for (int j = 0; j < n; ++j){
                se.add(arr[j] & mask);
            }

            int newMaxx = maxx | (1 << i);

            for (int prefix : se){
                if (se.contains(newMaxx ^ prefix)){
                    maxx = newMaxx;
                    break;
                }
            }
            se.clear();
        }
        return maxx;
    }
}