#Look for #IMPLEMENT tags in this file.

'''
Construct and return Kenken CSP model.
'''

from cspbase import *
import itertools

def kenken_csp_model(course_list):

    course_num = course_list[0][0]
    # generate vars
    vars = []
    for i in range(1, course_num+1):
        vars.append(Variable('V{}'.format(i), course_list[i]))
    #list of timeslots e.g.["M10","Tu10","W16"]
    no_go = course_list[course_num+1]


    num_of_courses = course_list[0][0]

    cons = []

    # add all diff constraint for each course
    for i in range(0, len(vars)):
        sat_tuples = []
        for j in range(i, len(vars)):
            sat_tuples = check_vars(vars[i].domain(), vars[j].domain())

        con = Constraint("C(CS{},CS{})".format(i + 1, j + 1), [vars[i], vars[j]])
        con.add_satisfying_tuples(sat_tuples)
        cons.append(con)

    # add constraints for nogo times
    # for var in vars:
    #     sat_tuples = []
    #     for nogo_time in no_go:
    #         if no_go not in var.domain():
    #             sat_tuples.append()

    course_csp = CSP("course_csp")

    # add all vars
    for row in vars:
        for v in row:
            course_csp.add_var(v)

    # add all constraints
    for each_con in cons:
        course_csp.add_constraint(each_con)

    return course_csp, vars





def check_vars(d0, d1):
    sat_tuples = []


    for t in itertools.product(d0, d1):
        if t[0] != t[1]:
            sat_tuples.append(t)

    return sat_tuples




