class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        size=len(image)
        for img in image:
            img.reverse()

        for row in range(size):
            for col in range(size):
                if image[row][col]:
                   image[row][col]=0
                else:
                    image[row][col]=1
        return image 
