from course_csp import *
from propagators import *
from orderings import *


testcase = [
    [[5],["M8,M9,M10","Tu13,Tu14,Tu15"],["Tu9,Tu10","Th11,Th12","F9,F10"],["F14,F15,F16"],["M10","Tu13","W11","W14"],["Th12,Th13,Th14","F8,F9,F10"],["Tu11","Tu13","W11","F8"]]
]

def print_course_soln(var_array):
    for var in var_array:
        print(var.get_assigned_value())

if __name__ == "__main__":
    

    for b in testcase:
        print("Solving courses")
        csp, var_array = model_course_as_var(b)
        #csp, var_array = model_timeslot_as_var(b)
        solver = BT(csp)
        print("=======================================================")
        print("FC")
        solver.bt_search(prop_FC)
        # print("GAC")
        # solver.bt_search(prop_GAC)
        print("Solution")
        print_course_soln(var_array)

