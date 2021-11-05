import time

schedule = [
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
]
 # Constants- employees needed for each shift minimum and maximum
 ##############################  Problems with multiple employees needed ###########################
MaxEmployeesPerShift = [1,3,1,1]
NumberOfEmployees = len(schedule)
conflict = []

print(f'Number of employees: {NumberOfEmployees}')


employees = [
    {
        'id':1,
        'availability':[
            True, True, False, True,
            False, False, False, False,
            False, True, False, False,
            False, False, False, False,
            False, True, True, False,
            True, True, False, True,
        ],
        'doubles': False,
        'lvn': False,
        'max': 40
    },
    {
        'id':2,
        'availability':[
            False, True, False, False,
            False, False, True, True,
            False, True, False, False, 
            False, False, True, True,
            False, False, True, True,
            False, False, True, False, 
        ],
        'doubles': True,
        'lvn': False,
        'max': 36
    },
    {
        'id':3,
        'availability':[
            True, False, True, False,
            True, True, False, False,
            False, False, True, False,
            True, True, False, False,
            True, True, True, False,
            True, True, False, False,
        ],
        'doubles': False,
        'lvn': False,
        'max': 20
    },
    {
        'id':4,
        'availability':[
            True, False, True, True,
            True, True, True, True,
            False, False, False, False,
            True, True, True, True,
            True, True, True, False,
            True, True, True, False,
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
            True, False, False, True,
            False, False, False, False,
            False, False, False, False,
            True, True, False, False,
        ],
        'doubles': False,
        'lvn': False,
        'max' : 20,
    },
    {
        'id':6,
        'availability':[
            True, True, False, False,
            True, True, False, False,
            True, True, True, True,
            False, False, False, False,
            False, False, False, False,
            True, True, False, False,
        ],
        'doubles': True,
        'lvn': False,
        'max' : 8,
    },

]


############################   HELPER FUNCTIONS #############################################

def print_matrix():
    print("\n\n")
    print("\t\t\t\t |  Monday  |  Tuesday  | Wednesday | Thursday  |  Friday   | Saturday  |")
    for row in range(len(schedule)):
        print("\t\t\t\t",schedule[row])
    print("\n\n")

def reformat_matrix(schedule):
    for row in range(len(schedule)):
        for col in range(len(schedule[0])):
            if schedule[row][col] is None:
                schedule[row][col] = 0
    print_matrix()

def log_conflict(y):
    global conflict
    conflict.append(y)

def resolve_conflict():
    global conflict
    if len(conflict) >0:
        conflict.clear()

def is_column_not_full(col):
    total_in_col = get_col_hours(col)
    if total_in_col/4 < MaxEmployeesPerShift[col%4]:
        return True
    return False

def get_row_hours(m, e):
    hours = 0
    for i in range(len(m[0])):
        if m[e][i]:
            hours += m[e][i]
    return hours

def get_col_hours(j):
    hours = 0
    for e in range(len(schedule)):
        if schedule[e][j] is not None:
            hours += schedule[e][j]
    return hours

def reset_zeros(m, col):
    for e in range(len(m)):
        if m[e][col] == 0:
            print(f"Replacing 0 with None at {e}, {col}")
            m[e][col] = None
reformat_matrix(schedule)
############################################## MAIN FUNCTIONS ###########################################

def is_valid(m, e, shift): # works with an open shift index and employee index value from schedule
    #Get total curent employee hours
    current_hours = get_row_hours(m, e);
    # If current hours is at or over max hours for employee return false
    print(f"Checking ({e}, {shift})")
    if current_hours >= employees[e]['max']:
        print(f"This employee has {current_hours} and has reached his max. Invalid...")
        return False
    # If employee is not available for that shift return False
    elif not employees[e]['availability'][shift]:
        print(f"Employee {e} is not available for shift {shift}. Invalid...")
        return False
    # If employee is already scheduled that shift return Flase
    elif m[e][shift] > 0:
        print(f"Employee {e} is already scheduled for this shift...")
        return 2
    
    
    # if employee hours sum to 8 already have to check that employee can work doubles.
        # if employee can work doubles then schedule for additional shift.
        # Set variable of worked double to true. Work double variable resets at each employee.
        # Needs attentioon to account for 12 vs 16 hr hifts!!!!!!
        # May split day into 3 shifts one 8 am and two 4hr pm shifts
    # If 4 hours havent passed since employee was last scheduled
    # else return 2
    else:
        return True

# finds available shift returns false if all shifts are full or returns column index
def find_open_shift(schedule):
    for j in range(len(schedule[0])):
        # Get all empoyee hours currently scheduled for that column
        # hours_for_shift = get_col_hours(schedule, j)
        # print(f"Checking  col {j}...")

        # check if hours for shifts are at max. If not, return column.
        #if hours_for_shift/4 < MaxEmployeesPerShift[j%4]:
        if is_column_not_full(j):
            print(f"returning col {j}")
            return 1,j

        # elif schedule[len(schedule[j])][j] == 0:
            
        # elif j == len(schedule[0])-1:
        #     print(f"last col: return slot at end of col {j}")
        #     return (j)


                # elif schedule[i][j] == 0:
                #     # print(f"Replacing 0 with None at {i}, {j} in loop")
                #     schedule[i][j] = None
                # if schedule[i][j] == 0:
                #     #print(f"Empty shift at {i} {j}.\n")
                #     return (i, j)
                
                # IMPORTANT: if schedule has been previously seen and skipped because 
                # iteration of employee was unavailable it will be marked as 0.
                # any 0 will be turned to None to be considered as open shift for next employee iterated
        # elif hours_for_shift/4 == MaxEmployeesPerShift[j%4]:
          #  print(f"Max employees needed for shift {j} reached: ", hours_for_shift/4, " out of " , MaxEmployeesPerShift[j%4])
        # reset slots that were passed over due to unavailability to None

        #reset_zeros(schedule, j)

    return False

def solve_schedule(m):
    global conflict
    print("Finding open shift...")
    avail_col = find_open_shift(m)
    if not avail_col:
        print("\t\t---------------------  All shifts filled! Scheduling complete!!!  ----------------------\n\n")
        print("\t  :::::::::::::::::::::::::::  Outputting Completed Schedule Now  ::::::::::::::::::::::::::::")
        reformat_matrix(schedule)
        print("\t\t\t\t\t\t------------------  ENDING PROGRAM  ------------------\n\n")
        return True
    else:
        _, c = avail_col

    for e in range(len(m)):
        
        print(f"checking if {e}, {c} is valid...")       
        val = is_valid(m,e,c)
        if val == 2:
            print("Employee scheduled already...")
        elif not val:
            m[e][c] = 0
        elif val:
            print(f"Placing {e} at {c}......\n")
            resolve_conflict()
            m[e][c] =4
            print_matrix()
            
            if solve_schedule(m):
                print("Recurse returned true...")
                return True
                
            print(f"Removing {e} from {c}.......\n")
            m[e][c] = 0
            print_matrix()

    if is_column_not_full(c):
        log_conflict(c)
        print(f"Column {c} not filled! Backtracking...")
        if c != 0:
            return False
        else:
            print("Could not resolve conflict...")

    print(f"\n\nERROR!!! -------------  Could not find availability for column {conflict[0]}!!!   -------------------\n\n   ::::::::::::::: Ouputting incomplete schedule due to schedule conflict::::::::::::::::::::::")
    reformat_matrix(schedule)
   
    print("  --------------- Scheduler must manually make changes to schedule OR change employee availability  -------------------------\n\n")
    print("                       .....ENDING PROGRAM.....\n\n")
    print("\nReturning false just cuz...\n")
    return False




reformat_matrix(schedule)
solve_schedule(schedule)
# print_matrix()
###################################################################################
