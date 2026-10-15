class CountSquares:

    def __init__(self):
        self.pts_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts_count[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total_squares = 0

        for (x, y), count in self.pts_count.items():
            if abs(qx-x)!=abs(qy-y) or qx==x:
                continue
            
            p1 = (x, qy)
            p2 = (qx, y)
            if p1 in self.pts_count and p2 in self.pts_count:
                total_squares += count*self.pts_count[p1]*self.pts_count[p2]

        return total_squares
        
