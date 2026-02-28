def leap_year(year):
    '''
    Docstring for leap_year
    
    :param year: takes integer for year and returns if year was leap year
    '''
    if year % 4 == 0:
        if  year % 100 == 0 and not year % 400 == 0:
            return False;
        else:
            return True;
    else:
         return False;