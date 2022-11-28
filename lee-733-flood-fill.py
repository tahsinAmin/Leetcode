def floodFill(image, sr, sc, newColor):
    if image == None or image[sr][sc] == newColor:
        return image
    return fill(image, sr, sc, image[sr][sc], newColor)


def fill(image, r, c, initialColor, newColor):
    if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != initialColor:
        print(f"Inside with r as {r}")
        return image
    image[r][c] = newColor
    image = fill(image, r-1, c, initialColor, newColor)
    image = fill(image, r+1, c, initialColor, newColor)
    image = fill(image, r, c-1, initialColor, newColor)
    image = fill(image, r, c+1, initialColor, newColor)

    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

print(floodFill(image, sr, sc, color))


# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
#         if image == None or image[sr][sc] == color:
#             return image
#         image = self.fill(image, sr, sc, image[sr][sc], color)
#         return image

#     def fill(self, image, r, c, initialColor, newColor):
#         if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != initialColor:
#             return

#         image[r][c] = newColor
#         self.fill(image, r+1, c, initialColor, newColor)
#         self.fill(image, r-1, c, initialColor, newColor)
#         self.fill(image, r, c+1, initialColor, newColor)
#         self.fill(image, r, c-1, initialColor, newColor)

#         return image
