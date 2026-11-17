class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq = new int[26];
        for (char task: tasks) {
            freq[task-'A']++;
        }

        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int count: freq) {
            if (count>0) {
                maxHeap.offer(count);
            }
        }

        Queue<int[]> cooldownQueue = new ArrayDeque();
        int time = 0;

        while (!maxHeap.isEmpty() || !cooldownQueue.isEmpty()) {
            if (!maxHeap.isEmpty()) {
                time++;
                int remaining = maxHeap.poll()-1;
                if (remaining>0) {
                    cooldownQueue.offer(new int[]{remaining, time+n});
                }
            } else {
                time = cooldownQueue.peek()[1];
            }
            if (!cooldownQueue.isEmpty() && cooldownQueue.peek()[1]==time) {
                maxHeap.offer(cooldownQueue.poll()[0]);
            }
        }
        return time;
    }
}
