from collections import deque

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, colour: int) -> List[List[int]]:
        pixelQ = deque()
        visited = set()
        pixelQ.append([sr, sc])
        fillCol = image[sr][sc]
        while len(pixelQ) > 0:
            pixel = pixelQ.popleft()
            sr = pixel[0]
            sc = pixel[1]

            #set pixel colour
            if image[sr][sc] == fillCol:
                image[pixel[0]][pixel[1]] = colour

            # add next pixels, must check that all 4 are valid pixels
                if sr - 1 >= 0 and f"[{sr-1}, {sc}]" not in visited:
                    pixelQ.append([sr-1, sc])
                    visited.add(f"[{sr-1}, {sc}]")
                if sr + 1 < len(image) and f"[{sr+1}, {sc}]" not in visited:
                    pixelQ.append([sr+1, sc])
                    visited.add(f"[{sr+1}, {sc}]")
                if sc - 1 >= 0 and f"[{sr}, {sc-1}]" not in visited:
                    pixelQ.append([sr, sc-1])
                    visited.add(f"[{sr}, {sc-1}]")
                if sc + 1 < len(image[0]) and f"[{sr}, {sc+1}]" not in visited:
                    pixelQ.append([sr, sc+1])
                    visited.add(f"[{sr}, {sc+1}]")

        return image

if __name__ == "__main__":
    image = [[0,0,0], [0,0,0]]
    sr = 0
    sc = 0
    colour = 0
    sol = Solution()
    result = sol.floodFill(image, sr, sc, colour)
    print(result)

