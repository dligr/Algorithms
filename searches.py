def binSearch(A, elem):
    if (len(A) < 1):
        return

    if elem < A[0] or elem > A[len(A) - 1]:
        print("None")
        return

    sequence = []

    binSearchRec(A, elem, 0, len(A) - 1, sequence)

    return sequence

def binSearchRec(A, elem, lo, hi, sequence):
    if elem < A[lo] or elem > A[hi]:
        return

    if hi < lo:
        return

    midID = (hi + lo) // 2
    mid = A[midID]

    if mid == elem:
        sequence.append(elem)
        print(elem)
        return

    sequence.append(mid)
    print(mid, end=" ")

    if mid < elem:
        binSearchRec(A, elem, midID + 1, hi, sequence)
    else:
        binSearchRec(A, elem, lo, midID - 1, sequence)

def interpolSearch(A, elem):
    if len(A) < 1:
        return

    if elem < A[0] or elem > A[len(A) - 1]:
        print("None")
        return

    sequence = []

    interpolSearchRec(A, elem, 0, len(A) - 1, sequence)

    return sequence

def interpolSearchRec(A, elem, lo, hi, sequence):
    if hi < lo:
        return

    if elem < A[lo]:
        return

    if elem > A[hi]:
        return

    midID = -1

    if lo == hi:
        midID = lo
    else:
        midID = lo + int(round((elem - A[lo]) * (hi - lo)) / (A[hi] - A[lo]))

    if midID < lo or midID > hi:
        return

    mid = A[midID]

    print(mid, end=" ")
    sequence.append(mid)

    if mid == elem:
        return

    if mid > elem:
        interpolSearchRec(A, elem, lo, midID - 1, sequence)
    else:
        interpolSearchRec(A, elem, midID + 1, hi, sequence)

def fibSearch(A, elem):
    if elem < A[0] or elem > A[len(A) - 1]:
        print("None")
        return

    sequence = []

    a = 0
    b, c = 1, 1
    while c < len(A):
        a, b = b, c
        c = a + b

    fibSearchRec(A, elem, 0, b, c, len(A), sequence)

    return sequence

def fibSearchRec(A, elem, lo, fKm1, fK, n, sequence):
    if fK == 0 or (fK == 1 and A[lo] != elem):
        print(A[lo])
        return
    if fK == 1 and A[lo] == elem:
        print(elem)
        sequence.append(elem)
        return

    fKm2 = fK - fKm1

    midID = min(lo + fKm2 - 1, n - 1)

    mid = A[midID]

    print(mid, end=" ")
    sequence.append(mid)

    if mid == elem:
        return
    elif mid > elem:
        fibSearchRec(A, elem, lo, fKm1 - fKm2, fKm2, n, sequence)
    else:
        fibSearchRec(A, elem, lo + fKm2, fKm2, fKm1, n, sequence)