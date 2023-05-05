def solution(dots):
    def slope(dot1, dot2):
        return (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
    a, b, c, d = dots
    return int(slope(a, b) == slope(c, d) or slope(a, c) == slope(b, d))