# Python_ML_Labor_Analysis

Business Problem: All timekeeping for a multinational manufacturing company was recently centralized. This is the intial analysis to gain insight into labor trends at the company.

Goals:

- Reduction of unecessary overtime
- Can workplace accidents be predicted based on hours worked?
- Can hours worked predict employees leaving the company?

# ML_Labor.py

Data from timekeeping system is stored in T-SQL database. There is too much data to directly pull all employees and analyze (100+ million rows). Employees themselves are also different. Employees in one country will earn overtime differently than those in another country. Employees on the manufacturing floor will be affected by labor shortages different than employees working in the office at the same site. 

This file selectively groups employees by site and department. It then groups hours of the same week for future analysis.
