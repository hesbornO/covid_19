# COVID 19 CHALLENGE
# CREATED BY OSWAGO HESBON
import argparse
import string

import sys
#function for estimation
def estimator(data):
  
  reportedCases = int(data['reportedCases'])  
  impact_currentlyInfected = reportedCases * 10
  severeImpact_currentlyInfected = reportedCases * 50
 
  requestedTime = int(data['timeToElapse'])
  #impact
  impact_infectionsByRequestedTime = int(impact_currentlyInfected * (2 ** int(requestedTime/3)))
  #severeImpact
  severeImpact_infectionsByRequestedTime = int(severeImpact_currentlyInfected * (2 ** int(requestedTime/3)))
  
  print(f"Impact: {impact_currentlyInfected}\t\t After {requestedTime} days: {impact_infectionsByRequestedTime}")
  print(f"Impact: {severeImpact_currentlyInfected}\t\t After {requestedTime} days: {severeImpact_infectionsByRequestedTime}")

  severeCasesByRequestedTime = int(0.15 * severeImpact_infectionsByRequestedTime)
  
  hospitalBedsByRequestedTime = int((0.35 * int(data['totalHospitalBeds'])) -  severeCasesByRequestedTime)
  
  casesForICUByRequestedTime = int(0.05 * severeImpact_infectionsByRequestedTime)
  
  casesForVentilatorsByRequestedTime = int(0.02 * severeImpact_infectionsByRequestedTime)
  
  dollarsInFlight = int((impact_infectionsByRequestedTime * 0.65 * 1.5) / requestedTime)
  
  output_data = {
    'data' : data,
    'impact': impact_infectionsByRequestedTime,
    'severeImpact' : severeImpact_infectionsByRequestedTime,
    'severeCasesByRequestedTime' : severeCasesByRequestedTime,
    'hospitalBedsByRequestedTime' : hospitalBedsByRequestedTime
  }
  return output_data

def main():

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
    
    
if __name__ == "__main__":
  main()