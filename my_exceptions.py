

class NoAvailabilityException(Exception):

    def __init__(self, error):
        self.error = error
    
    def __str__(self):
        return f"\n\nERROR!!! -----------------  Could not find enough availability for column {self.error}!!! -------------------\n\n ---------------- Scheduler must manually make changes to schedule OR change employee availability  ------------------\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t.....ENDING PROGRAM.....\n\n"

    