#Look for #IMPLEMENT tags in this file.

'''
Construct and return Kenken CSP model.
'''

from cspbase import *
import itertools

def kenken_csp_model(course_list):

    course_num = course_list[0][0]
    # list of timeslots e.g.["M10","Tu10","W16"]
    no_go = course_list[course_num + 1]
    # generate vars
    vars = []
    for i in range(1, course_num+1):
        domain_list = course_list[i]
        invalid_domain = []
        for item in domain_list:
            for nogo_time in no_go:
                if nogo_time in item:
                    invalid_domain.append(item)
        for item in invalid_domain:
            domain_list.remove(item)

        vars.append(Variable('V{}'.format(i), domain_list))
        #vars.append(Variable('V{}'.format(i), course_list[i]))

    cons = []

    # add all diff constraint for each course
    for i in range(0, len(vars)):
        sat_tuples = []
        for j in range(i+1, len(vars)):
            sat_tuples = check_vars(vars[i].domain(), vars[j].domain())

            con = Constraint("C(CS{},CS{})".format(i + 1, j + 1), [vars[i], vars[j]])
            con.add_satisfying_tuples(sat_tuples)
            cons.append(con)


    # #add constraints for nogo times
    # for i in range(0, len(vars)):
    #     sat_tuples = []
    #     sat_list = []
    #     for nogo_time in no_go:
    #         for session in vars[i].domain():
    #             if nogo_time not in session and session not in sat_tuples:
    #                 sat_tuples.append(session)
    #             if nogo_time in session and session in sat_tuples:
    #                 sat_tuples.remove(session)
    #     #sat_t = tuple(sat_list)
    #     #sat_tuples.append(sat_t)
    #     # for item in sat_list:
    #     #     sat_tuples.append(tuple(item))
    #     con = Constraint("C(V{},nogo)".format(i + 1), [vars[i]])
    #     con.add_satisfying_tuples(sat_tuples)
    #     cons.append(con)

    #make csp
    course_csp = CSP("course_csp")

    # add all vars
    for var in vars:
        course_csp.add_var(var)

    # add all constraints
    for each_con in cons:
        course_csp.add_constraint(each_con)

    print ("finish")
    return course_csp, vars


def check_vars(d0, d1):
    sat_tuples = []

    for t in itertools.product(d0, d1):
        if (t[1] not in t[0]) and (t[0] not in t[1]):
            sat_tuples.append(t)

    return sat_tuples




