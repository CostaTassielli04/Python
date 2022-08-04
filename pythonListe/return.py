def print_hi(name):

    def is_year_leap(year):
        if year % 4 == 0:
            if year % 100 != 0 or year % 400 ==0:
                bisestile=True
            else:
                bisestile= False
        else:
            bisestile=False
        return bisestile

    def days_in_months(year,month):
        condizione=is_year_leap(year)
        if month==4 or month==6 or month==9 or month==11:
            days=30
        elif month==2:
            if condizione==True:
                days=29
            else:
                days=28
        else:
            days=31

        return days

    #test_years = [1900, 2000, 2016, 1987]
    #test_months=[2,2,1,11]
    #test_results = [28,29,31,30]
    #for i in range(len(test_years)):
       # yr = test_years[i]
       # m=test_months[i]
        #print(yr, "->", end="")
       # result = days_in_months(yr,m)
        #if result == test_results[i]:
          #  print("OK")
        #else:
          #  print("Failed")
    #(34%)

    def days_of_years(year,month,day):
        days = 0
        for m in range(1, month):
            md = days_in_month(year, m)
            if md == None:
                return None
            days += md
        md = days_in_month(year, month)
        print("days=", days)
        if day >= 1 and day <= md:
            return days + day
        else:
            return None


    print(days_of_years(2000,12,31))

if __name__=='__main__':
    print_hi('Pycharm')