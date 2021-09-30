from .interpolation import interpolation

class Geometric:
    def __init__(self):
        pass

    def forward_rotate(self, image, theta):
        """Computes the forward rotated image by and angle theta
                image: input image
                theta: angle to rotate the image by (in radians)
                return the rotated image"""

        dimension = np.shape(image)
        tl = [0, 0]
        tr = [dimension[1], 0]
        br = [0, dimension[0]]
        bl = [dimension[0], dimension[1]]

        def my_Coordinates(x, y, theta):
            x1 = (x * math.cos(theta)) - (y * math.sin(theta))
            y1 = (x * math.sin(theta)) + (y * math.cos(theta))
            z = [math.floor(x1), math.floor(y1)]
            return z

        tr_new = my_Coordinates(tr[0], tr[1], theta)
        br_new = my_Coordinates(br[0], br[1], theta)
        bl_new = my_Coordinates(bl[0], bl[1], theta)
        tl_new = my_Coordinates(tl[0], tl[1], theta)
        box1 = min(tl_new[0], tr_new[0], br_new[0], bl_new[0])
        box2 = min(tl_new[1], tr_new[1], br_new[1], bl_new[1])
        box3 = max(tl_new[0], tr_new[0], br_new[0], bl_new[0])
        box4 = max(tl_new[1], tr_new[1], br_new[1], bl_new[1])
        r = box3 - box1
        c = box4 - box2
        forwardrotated_image = np.zeros((r, c))

        array = []
        minx, miny = float("inf"), float("inf")

        for i in range(0, dimension[0]):
            array1 = []
            for j in range(0, dimension[1]):
                cr_new = my_Coordinates(i, j, theta)
                array1.append(cr_new)
                if cr_new[0] < minx:
                    minx = cr_new[0]
                if cr_new[1] < miny:
                    miny = cr_new[1]
            array.append(array1)

        for i in range(0, dimension[0]):
            for j in range(0, dimension[1]):
                array[i][j][0] -= minx
                array[i][j][1] -= miny

        for i in range(0, dimension[0]):
            for j in range(0, dimension[1]):
                pixel = image[i][j]
                cr_new = array[i][j]
                forwardrotated_image[cr_new[0], cr_new[1]] = pixel

        return forwardrotated_image

    def reverse_rotation(self, rotated_image, theta, origin, original_shape):
        """Computes the reverse rotated image by and angle theta
                rotated_image: the rotated image from previous step
                theta: angle to rotate the image by (in radians)
                Origin: origin of the original image with respect to the rotated image
                Original shape: Shape of the orginal image
                return the original image"""

        def my_Coordinates(x, y, theta):
            m = (x * math.cos(theta)) + (y * math.sin(theta))
            n = -(x * math.sin(theta)) + (y * math.cos(theta))
            z = [math.floor(m), math.floor(n)]
            return z

        new_image = np.zeros(original_shape)

        dimensions = np.shape(rotated_image)

        for i in range(0, dimensions[0]):
            for j in range(0, dimensions[1]):
                a, b = my_Coordinates((i - origin[0]), (j - origin[1]), theta)
                if 0 <= a < original_shape[0] and 0 <= b < original_shape[1]:
                    new_image[a][b] = rotated_image[i][j]

        return new_image

    def rotate(self, image, theta, interpolation_type):
        """Computes the reverse rotated image by and angle theta
                image: the input image
                theta: angle to rotate the image by (in radians)
                interpolation_type: type of interpolation to use (nearest_neighbor, bilinear)
                return the original image"""

        return image


