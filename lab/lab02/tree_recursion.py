def cascade(n):
    if n < 10:
        print("0",n)
    else:
        print("1",n)
        cascade(n//10)
        print("2",n)

def move_disk(disk_number, from_peg, to_peg):
    print("Move disk " +str(disk_number) + " from peg " \
          + str(from_peg) + " to peg " +str(to_peg) + ".")

def solve_hanoi(n, start_peg, end_peg):
     if  n == 1:
         move_disk(n, start_peg, end_peg)
     else:
         spare_peg = 6 - start_peg - end_peg
         solve_hanoi(n - 1, start_peg, spare_peg)
         move_disk(n, start_peg, end_peg)
         solve_hanoi(n-1, spare_peg, end_peg)