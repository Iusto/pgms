def solution(bin1, bin2):
    bin3 = int(bin1,2) + int(bin2,2)
    return bin(bin3)[2:]