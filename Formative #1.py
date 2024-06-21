def savings(gross_pay,tax_rate,expenses):
    take_home_pay = int(gross_pay - tax_rate * gross_pay - expenses)
    return take_home_pay

def material_waste(total_material,material_units,num_jobs,job_consumption):
    wasted_material = str(total_material - job_consumption * num_jobs) + str(material_units)
    return wasted_material 

def interest(principal,rate,periods):
    simple_interest = round(principal * rate * periods)
    principal += simple_interest
    return principal // 1