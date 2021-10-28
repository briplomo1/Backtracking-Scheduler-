matrix = [
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
]
# matrix is rows: employees which in this sample is 6 and columns are the shifts. This has 4 shifts per 6 day workweek excluding sundays. A total of 24 shifts.
 # Constants- employees needed for each shift minimum and maximum
MaxEmployeesPerShift = [4,4,3,3]
NumberOfEmployees = len(matrix)

print(f'Number of employees: {NumberOfEmployees}')


employees = [
    {
        'id':1,
        'availability':[
            True, True, False, False,
            True, True, False, False,
            False, False, False, False,
            True, True, False, False,
            True, True, True, True,
            True, True, False, False,
        ],
        'doubles': False,
        'lvn': False,
        'max': 40
    },
    {
        'id':2,
        'availability':[
             False, False,True, True,
             False, False, True, True,
            True, True, True, True,
            False, False, True, True,
            False, False, False, False,
            False, False, True, True, 
        ],
        'doubles': True,
        'lvn': False,
        'max': 36
    },
    {
        'id':3,
        'availability':[
            True, True, False, False,
            True, True, False, False,
            False, False, False, False,
            True, True, False, False,
            True, True, True, True,
            True, True, False, False,
        ],
        'doubles': False,
        'lvn': False,
        'max': 20
    },
    {
        'id':4,
        'availability':[
            True, True, False, False,
            True, True, False, False,
            False, False, False, False,
            True, True, False, False,
            True, True, True, True,
            True, True, False, False,
        ],
        'doubles': True,
        'lvn': False,
        'max': 40
    },
    {
        'id':5,
        'availability':[
            True, False, False, True,
            False, False, False, False,
            False, False, False, True,
            False, False, False, False,
            False, False, False, True,
            True, True, False, False,
        ],
        'doubles': False,
        'lvn': False,
        'max' : 20,
    },
    {
        'id':6,
        'availability':[
            True, False, False, False,
            True, True, False, False,
            True, True, True, True,
            False, False, False, False,
            False, False, False, True,
            True, True, False, False,
        ],
        'doubles': True,
        'lvn': False,
        'max' : 20,
    },

]


def print_matrix():
    for row in range(len(matrix)):
        print(matrix[row])

def solve(m):
    shifts_this_day = 0;
    same_day = True;
    empty_shift = find_open_shift(m);
    # if no available shift solve() returns true because
    if not empty_shift:
        print("returning true because shift is full")
        return True
    else:
        e, s = empty_shift
        val = is_valid(m, e, s)
        if val == 1:
            print("Did not place employee cuz of his avilability. Placing zero and moving on...")
            matrix[e][s] = 0
            print_matrix()
            solve(m)
        elif val == 2:
            matrix[e][s] = 4
            print("placed employee successfully")
            print_matrix()
            if(solve(m)):
                print("Solve returning true")
                return True

            matrix[e][s] = None
            print(f"Undoing shift {e} at {s}")
        
    print("Solve returning false")
    return False
            



def is_valid(m, e, shift): # works with an open shift index and employee index value from matrix
    
    # total sumed values of row cannot exceed max hours of employee

    #Get total curent employee hours
    current_hours = 0;
    for i in range(len(matrix[0])):
        if matrix[e][i]:
            current_hours += matrix[e][i]

    # If current hours is at or over max return false
    if current_hours >= employees[e]['max']:
        print(f"This employee has {current_hours} and has reached his max. Invalid...")
        return 0

    # If employee is not available for that shift return 1
    elif not employees[e]['availability'][shift]:
        print(f"Employee {e} is not available for shift {shift}. Invalid...")
        return 1
    

    # if employee hours sum to 8 already have to check that employee can work doubles.
        # if employee can work doubles then schedule for additional shift.
        # # Set variable of worked double to true. Work double variable resets at each employee.needs attentioon to account for 12 vs 16 hr hifts!!!!!!
    
    # If 4 hours havent passed since employee was last scheduled
    # else return 2
    else:
        print("Returning two")
        return 2


# finds available shift returns flase if shifts full
def find_open_shift(matrix):
    for j in range(len(matrix[0])): # for shift
        # Get all empoyee hours scheduled for that shiftfrom column
        print(f"j is {j}")
        hours_for_shift = 0
        print(hours_for_shift)

        for e in range(len(matrix)):
            print("calculating hours in current shift...employee", e) # for every employee at add any value in shift j
            if matrix[e][j]:
                hours_for_shift += matrix[e][j]
                print(f"Shift {j} hours {hours_for_shift}")

        print(f"Hours for shift {j} are: {hours_for_shift}")
        # check if hours for all shifts are at max
        if hours_for_shift/4 < MaxEmployeesPerShift[j%4]:
            for i in range(len(matrix)):# for employee
                # Check if find available shift. Return index of shift
                if matrix[i][j] == None:
                    print(f"Have found empty shift with available hours. Possible employee i: {i} for shift j: {j}.")
                    return (i, j)
            #need to skip curren shift iteration to chjeck next shift open?
        else:
            print(f"Max employees needed for shift {j} reached: ", hours_for_shift/4, " out of " ,MaxEmployeesPerShift[j%4],"\n\n")

    
    print("Returning true for no reason")        
    return False



print_matrix()
solve(matrix)
print_matrix()
