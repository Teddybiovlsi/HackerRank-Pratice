# HackerRank 30 Days of Code - Day 26: Nested Logic
# Problem link: https://www.hackerrank.com/challenges/30-nested-logic/problem
#
# Objective:
# Calculate the fine for returning a library book late, based on the rules:
# 1. No fine if returned on or before the due date
# 2. If returned late within the same month and year: 15 Hackos × days late
# 3. If returned late within the same year but different month: 500 Hackos × months late
# 4. If returned in a different year: fixed fine of 10000 Hackos
#
# Approach:
# - Parse the returned and due dates
# - Use tuple comparison to check if returned on time
# - Apply the correct fine logic based on year/month/day difference

# Enter your code here. Read input from STDIN. Print output to STDOUT
# first is return date
day1, month1, year1 = input().strip().split()
# second is due date
day2, month2, year2 = input().strip().split()

# Convert input to integers
cvt_day1, cvt_mn1, cvt_yr1 = int(day1), int(month1), int(year1)
cvt_day2, cvt_mn2, cvt_yr2 = int(day2), int(month2), int(year2)

# Case 1: Returned on or before due date
if (cvt_yr1, cvt_mn1, cvt_day1) <= (cvt_yr2, cvt_mn2, cvt_day2):
    print(0)

# Case 2: Same year
elif cvt_yr1 == cvt_yr2:
    # Same month
    if cvt_mn1 == cvt_mn2:
        print((cvt_day1 - cvt_day2) * 15)
    # Different month
    else:
        print((cvt_mn1 - cvt_mn2) * 500)

# Case 3: Returned in different year
else:
    print(10000)