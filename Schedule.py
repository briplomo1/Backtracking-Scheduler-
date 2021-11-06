import time
import sys

sys.setrecursionlimit(2000)

schedule = [
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None],
    [None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]
]
 # Constants- employees needed for each shift minimum and maximum
# 4 shifts per day. Employees needed per shift
MaxEmployeesPerShift = [2,2,2,1]
NumberOfEmployees = len(schedule)

employees = [
    {
        'id':1,
        'availability':[
            True, True, False, True,
            False, False, False, False,
            False, True, False, False,
            False, False, False, False,
            False, True, True, False,
            True, True, False, False,
        ],
        'doubles': False,
        'lvn': False,
        'max': 40
    },
    {
        'id':2,
        'availability':[
            False, False, False, False,
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
            True, True, True, False,
            True, True, False, False,
            False, True, True, False,
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
            True, True, False, True,
            False, False, False, False,
            True, False, False, True,
            True, False, False, False,
            False, False, False, False,
            True, True, False, False,
        ],
        'doubles': False,
        'lvn': False,
        'max' : 40,
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
        'max' : 40,
    },

]


############################   HELPER FUNCTIONS #############################################

def print_matrix():
    print("\n")
    print("\t\t\t\t |  Monday  |  Tuesday  | Wednesday | Thursday  |  Friday   | Saturday  |")
    for row in range(len(schedule)):
        print("\t\t\t\t",schedule[row])
    print("\n")

def reformat_matrix(schedule):
    for row in range(len(schedule)):
        for col in range(len(schedule[0])):
            if schedule[row][col] is None:
                schedule[row][col] = 0
    print_matrix()

def is_column_not_full(col, m):
    total_in_col = get_col_hours(col, m)
    if total_in_col/4 < MaxEmployeesPerShift[col%4]:
        return True
    return False

def get_row_hours(m, e):
    hours = 0
    for i in range(len(m[0])):
        if m[e][i]:
            hours += m[e][i]
    return hours

def get_col_hours(j, schedule):
    hours = 0
    for e in range(len(schedule)):
        if schedule[e][j] is not None:
            hours += schedule[e][j]
    return hours

def has_availability(col):
    #print(f"Checking availability for col {col}")
    for emp in employees:
        if emp['availability'][col]:
            return True
    #print(f"Col {col} has no availability")
    return False
############################################## MAIN FUNCTIONS ###########################################

def is_valid(m, e, shift): # works with an open shift index and employee index value from schedule
    #Get total curent employee hours
    current_hours = get_row_hours(m, e);
    # If current hours is at or over max hours for employee return false
    #print(f"Checking ({e}, {shift})")
    if current_hours >= employees[e]['max']:
        #print(f"This employee has {current_hours} and has reached his max. Invalid...")
        return False
    # If employee is not available for that shift return False
    elif not employees[e]['availability'][shift]:
        #print(f"Employee {e} is not available for shift {shift}. Invalid...")
        return False
    # If employee is already scheduled that shift return Flase
    elif m[e][shift] > 0:
        #print(f"Employee {e} is already scheduled for this shift...")
        return 2

    else:
        return True

# finds available shift returns false if all shifts are full or returns column index
def find_open_shift(m):
    for j in range(len(m[0])):
        # check if hours for shifts are at max. If not, return column.
        if is_column_not_full(j, m):
            #print(f"returning col {j}")
            return 1,j



    return False

def solve_schedule(m):

    #print("Finding open shift...")
    avail_col = find_open_shift(m)
    if not avail_col:
        print("\t\t---------------------  All shifts filled! Scheduling complete!!!  ----------------------\n\n")
        print("\t  :::::::::::::::::::::::::::  Outputting Completed Schedule Now  ::::::::::::::::::::::::::::")
        reformat_matrix(schedule)
        print("\t\t\t\t\t\t------------------  ENDING PROGRAM  ------------------\n\n")
        return True
    else:
        _, c = avail_col

    if not has_availability(c):
        print(f"\n\nERROR!!! -----------------  Could not find availability for column {c} !!!   -------------------\n\n   ::::::::::::::::::::: Ouputting incomplete schedule due to schedule conflict::::::::::::::::::::::")
        reformat_matrix(m)
   
        print("  --------------- Scheduler must manually make changes to schedule OR change employee availability  -------------------------\n\n")
        print("                       .....ENDING PROGRAM.....\n\n")
        print("\nReturning false just cuz...\n")
        return True

    for e in range(len(m)):
        
        #print(f"checking if {e}, {c} is valid...")       
        val = is_valid(m,e,c)
        if val == 2:
            #print("Employee scheduled already...")
            pass
        elif not val:
            m[e][c] = 0
        elif val:
            # print(f"Placing {e} at {c}......\n")
    
            m[e][c] =4
            print_matrix()
            
            if solve_schedule(m):
                #print("Recurse returned true...")
                return True
                
            #print(f"Removing {e} from {c}.......\n")
            m[e][c] = 0
            print_matrix()

    # if column is not full
    if is_column_not_full(c,m):
        #print(f"Column {c} not filled! Backtracking...")
        # if it has not backtracked all the way to the first column it returns zero and backtracks
        if c != 0:
            return False
        else:
            #print("Could not resolve conflict...")
            pass
    return False


reformat_matrix(schedule)
startT = time.time()
solve_schedule(schedule)

print(time.time()-startT)

###################################################################################################################
