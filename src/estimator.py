# COVID 19 CHALLENGE
# CREATED BY OSWAGO HESBON

#function for estimation
def estimator(data):
  reportedCases = int(data['reportedCases'])  
  impact_currentlyInfected = reportedCases * 10
  severeImpact_currentlyInfected = reportedCases * 50
  #infection after some duration
  #DAYS
  while True:
    try:      
      days = int(input("Please enter days: "))
    except ValueError:    
      print("Invalid input! If no days, enter digit zero.")      
      continue
    else:
      break
  #WEEKS
  while True:
    try:      
      weeks = int(input("Please enter weeks: "))
    except ValueError:    
      print("Invalid input! If no weeks, enter digit zero.")      
      continue
    else:
      break
  #MONTHS
  while True:
    try:      
      months = int(input("Please enter months: "))
    except ValueError:    
      print("Invalid input! If no months, enter digit zero.")      
      continue
    else:
      break
 
  duration = int(int(days) + (int(weeks) * 7) + (months * 30))
  #impact
  impact_infectionsByRequestedTime = impact_currentlyInfected * (2 ** int(duration/3))
  #severeImpact
  severeImpact_infectionsByRequestedTime = severeImpact_currentlyInfected * (2 ** int(duration/3))
  
  print(f"Impact: {impact_currentlyInfected}\t\t After {duration} days: {impact_infectionsByRequestedTime}")
  print(f"Impact: {severeImpact_currentlyInfected}\t\t After {duration} days: {severeImpact_infectionsByRequestedTime}")
 
  output_data = {
    'data' : data,
    'impact': {impact_infectionsByRequestedTime},
    'severeImpact' : {severeImpact_infectionsByRequestedTime}
  }
  return output_data


input_data= {   
             'region': {       
               'name': "Africa",       
               'avgAge': 19.7,       
               'avgDailyIncomeInUSD': 5,       
               'avgDailyIncomePopulation': 0.71     
               },   
             'periodType': "days",   
             'timeToElapse': 58,   
             'reportedCases': 674,   
             'population': 66622705,   
             'totalHospitalBeds': 1380614 
             }

result = estimator(input_data)
print(result)