import argparse
import problem1
import problem2
import problem3



parser = argparse.ArgumentParser()
parser.add_argument("problem", type=int)
args = parser.parse_args()

func_dict = {}
func_dict[1] = problem1.problem_1
func_dict[2] = problem2.problem_2
func_dict[3] = problem3.problem_3

try:
    func_dict[args.problem]()
except KeyError:
    print "Invalid argument. No solution yet."


