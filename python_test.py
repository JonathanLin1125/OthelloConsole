'''
Created on May 17, 2017

@author: jonathanlin
'''
import othello

obj = othello.Othello(3, 5, "B", ">", [". . . . . .",
                                       "B W W W W .", 
                                       ". . . . . .", 
                                       ". . . . . ."])
try:
    coord = obj._check_left(1, 5)
    assert( coord == (1, 0))
    print("Left 1 Passed")
except:
    print("Left 1 Failed")
    
    
obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       "B W W .", 
                                       ". . . .", 
                                       ". . . .",
                                       ". . . .",
                                       ". . . ."])

try:
    coord = obj._check_left(1, 3)
    assert( coord == (1, 0))
    print("Left 2 Passed")
except:
    print("Left 2 Failed")
    
obj = othello.Othello(3, 5, "B", ">", [". . . . . .",
                                       ". W W W W B", 
                                       ". . . . . .", 
                                       ". . . . . ."])
try:
    coord = obj._check_right(1, 0)
    assert( coord == (1, 5))
    print("Rigt 1 Passed")
except:
    print("Rigt 1 Failed")
    
obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       ". W W B", 
                                       ". . . .", 
                                       ". . . .",
                                       ". . . .",
                                       ". . . ."])

try:
    coord = obj._check_right(1, 0)
    assert( coord == (1, 3))
    print("Rigt 2 Passed")
except:
    print("Rigt 2 Failed")
    
obj = othello.Othello(3, 5, "B", ">", [". . B . . .",
                                       ". . W . . .", 
                                       ". . W . . .", 
                                       ". . . . . ."])
try:
    coord = obj._check_up(3, 2)
    assert( coord == (0, 2))
    print("Up__ 1 Passed")
except:
    print("Up__ 1 Failed")
    
obj = othello.Othello(5, 3, "B", ">", [". . B .",
                                       ". . W .", 
                                       ". . W .", 
                                       ". . W .",
                                       ". . W .",
                                       ". . . ."])

try:
    coord = obj._check_up(5, 2)
    assert( coord == (0, 2))
    print("Up__ 2 Passed")
except:
    print("Up__ 2 Failed")
    
obj = othello.Othello(3, 5, "B", ">", [". . . . . .",
                                       ". . W . . .", 
                                       ". . W . . .", 
                                       ". . B . . ."])
try:
    coord = obj._check_down(0, 2)
    assert( coord == (3, 2))
    print("Down 1 Passed")
except:
    print("Down 1 Failed")
    
obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       ". . W .", 
                                       ". . W .", 
                                       ". . W .",
                                       ". . W .",
                                       ". . B ."])

try:
    coord = obj._check_down(0, 2)
    assert( coord == (5, 2))
    print("Down 2 Passed")
except:
    print("Down 2 Failed")
    
obj = othello.Othello(3, 5, "B", ">", [". . B . . .",
                                       ". . . W . .", 
                                       ". . . . W .", 
                                       ". . . . . ."])
try:
    coord = obj._check_back_diag_up(3, 5)
    assert( coord == (0, 2))
    print("BdUp 1 Passed")
except:
    print("BdUp 1 Failed")

obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       ". . . .", 
                                       ". . . .", 
                                       "B . . .",
                                       ". W . .",
                                       ". . . ."])

try:
    coord = obj._check_back_diag_up(5, 2)
    assert( coord == (3, 0))
    print("BdUp 2 Passed")
except:
    print("BdUp 2 Failed")

obj = othello.Othello(3, 5, "B", ">", [". . . . . .",
                                       ". W . . . .", 
                                       ". . W . . .", 
                                       ". . . B . ."])
try:
    coord = obj._check_back_diag_down(0, 0)
    assert( coord == (3, 3))
    print("BdDw 1 Passed")
except:
    print("BdDw 1 Failed")
    
obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       ". . W .", 
                                       ". . . B", 
                                       ". . . .",
                                       ". . . .",
                                       ". . . ."])

try:
    coord = obj._check_back_diag_down(0, 1)
    assert( coord == (2, 3))
    print("BdDw 2 Passed")
except:
    print("BdDw 2 Failed")
    
obj = othello.Othello(3, 5, "B", ">", [". . . . B .",
                                       ". . . W . .", 
                                       ". . W . . .", 
                                       ". . . . . ."])
try:
    coord = obj._check_forward_diag_up(3, 1)
    assert( coord == (0, 4))
    print("FdUp 1 Passed")
except:
    print("FdUp 1 Failed")
    
obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       ". . . B", 
                                       ". . W .", 
                                       ". W . .",
                                       ". . . .",
                                       ". . . ."])

try:
    coord = obj._check_forward_diag_up(4, 0)
    assert( coord == (1, 3))
    print("FdUp 2 Passed")
except:
    print("FdUp 2 Failed")
    
obj = othello.Othello(3, 5, "B", ">", [". . . . . .",
                                       ". . . W . .", 
                                       ". . W . . .", 
                                       ". B . . . ."])
try:
    coord = obj._check_forward_diag_down(0, 4)
    assert( coord == (3, 1))
    print("FdDw 1 Passed")
except:
    print("FdDw 1 Failed")
    
obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       ". . . .", 
                                       ". . . .", 
                                       ". . . .",
                                       ". . W .",
                                       ". B . ."])

try:
    coord = obj._check_forward_diag_down(3, 3)
    assert( coord == (5, 1))
    print("FdDw 2 Passed")
except:
    print("FdDw 2 Failed")
    
obj = othello.Othello(5, 3, "B", ">", [". . . .",
                                       ". . . .", 
                                       ". W . .", 
                                       ". . W .",
                                       ". . . B",
                                       ". . . ."])

obj._flip_line(4, 3, 1, 0)
obj.print_board()