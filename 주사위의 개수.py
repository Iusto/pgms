def solution(box, n):
    w,h,d = box[0]//n, box[1]//n, box[2]//n
    return w*h*d