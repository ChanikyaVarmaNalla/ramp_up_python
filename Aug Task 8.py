from datetime import date, timedelta
import pandas as pd

class AttendanceAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.today = date.today().strftime('%b %d')
        self.data = self.load_data()
        self.no_attendance = {}

    def load_data(self):
        df = pd.read_excel(self.file_path)
        return df.set_index('Emp ID').fillna('').to_dict(orient='index')

    def count_attendance_today(self):
        WFH_today = 0
        WFO_today = 0
        for emp_id, attend in self.data.items():
            if self.today in attend:
                if attend[self.today] == 'WFH':
                    WFH_today += 1
                elif attend[self.today] == 'WFO':
                    WFO_today += 1
        return WFH_today, WFO_today

    def count_attendance_previous(self):
        previous_dates = [(date.today() - timedelta(days=i)).strftime('%b %d') for i in range(1, 6)]
        WFH_previous = 0
        WFO_previous = 0
        for emp_id, attend in self.data.items():
            for day in previous_dates:
                if day in attend:
                    if attend[day] == 'WFH':
                        WFH_previous += 1
                    elif attend[day] == 'WFO':
                        WFO_previous += 1
        return WFH_previous, WFO_previous

    def find_no_attendance(self):
        for emp_id, attend in self.data.items():
            no_attendance_days = []
            if self.today not in attend:
                no_attendance_days.append(self.today)
            for day in attend:
                if attend[day] == '':
                    no_attendance_days.append(day)
            if no_attendance_days:
                self.no_attendance[emp_id] = no_attendance_days

    def analyze(self):
        WFH_today, WFO_today = self.count_attendance_today()
        WFH_previous, WFO_previous = self.count_attendance_previous()
        self.find_no_attendance()

        print(f"WFH Count for {self.today}: {WFH_today}")
        print(f"WFO Count for {self.today}: {WFO_today}")
        print(f"WFH Count for the previous 5 days: {WFH_previous}")
        print(f"WFO Count for the previous 5 days: {WFO_previous}")

        if self.no_attendance:
            print("Employee(s) who haven't filled attendance for today and previous 5 days:")
            for emp_id, days in self.no_attendance.items():
                print(f"Employee ID: {emp_id}, Days with No Attendance: {', '.join(days)}")

# Usage
if __name__ == "__main__":
    analyzer = AttendanceAnalyzer('attendance.xlsx')
    analyzer.analyze()
