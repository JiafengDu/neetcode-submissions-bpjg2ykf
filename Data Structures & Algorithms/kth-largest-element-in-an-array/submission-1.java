class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int num:nums) {
            minHeap.offer(num);
            if (minHeap.size() > k) {
                minHeap.poll(); // evict the min point, so max points are left
            }
        }

        return minHeap.peek();
    }
}
