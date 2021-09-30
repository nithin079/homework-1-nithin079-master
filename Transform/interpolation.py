class interpolation:

    def linear_interpolation(self):
        """Computes the linear interpolation at location pti using pt1 and pt2 as input.
        1. Please change the function definition to add the the required arguments as needed.
        2. This function performs linear interpolation between two one dimensional points and returns the interpolated value.        
        This function will require the following values
        pt1: Location of point pt1 (z1)
        I1: Intensity at the location pt1
        pt2: Location of point pt2 (z2)
        I2: Intensity at the location pt2
        pti: Location at which to detemine the interploated value (z)
        return Ii or interploated intentity at location pti"""

        # Write your code for linear interpolation here
        try:

            intensity = ((pt2[0] - unknown[0]) / (pt2[0] - pt1[0])) * pt1[2] + (
                    (unknown[0] - pt1[0]) / (pt2[0] - pt1[0])) * pt2[2]
        except:

            intensity = pt2[2]

        return intensity

    def bilinear_interpolation(self):
        """Computes the bilinear interpolation at location pti using pt1, pt2, pt3, and pt4 as input
        1. Please change the function definition to add the the required arguments as needed.
        2. This function performs bilinear interpolation between four two dimensional points and returns the interpolated value.        
        3. This is accomplished by performing linear interpolation three times. Reuse or call linear interpolation method above to compute this task.
        This function will require the following values
        pt1: Location of the point pt1 (x1, y1)
        I1: Intensity at location pt1
        pt2: Location of the point pt2 (x2, y2)
        I2: Intensity at location pt2
        pt3: Location of the point pt3 (x3, y3)
        I3: Intensity at location pt3
        pt4: Location of the point pt4 (x4, y4)
        I4: Intensity at location pt4
        pti: Location at which to detemine the interploated value (x, y)
        return Ii or interploated intentity at location pti"""

        # Write your code for bilinear interpolation here
        try:

            intensity1 = self.linear_interpolation(pt1, pt2, unknown)
            intensity2 = self.linear_interpolation(pt3, pt4, unknown)

            intensity = ((pt4[1] - unknown[1]) / (pt4[1] - pt3[1])) * intensity1 + (
                    (unknown[1] - pt3[1]) / (pt4[1] - pt3[1])) * intensity2
        except:
            intensity = pt1[2]

        return intensity
