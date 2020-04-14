# COVID 19 CHALLENGE
# CREATED BY OSWAGO HESBON

import pprint
import sys
#function for estimation
def estimator(data):
  
  reportedCases = int(data['reportedCases']) 
  requestedTime = int(data['timeToElapse'])
  
  impact = { 'currentlyInfected' : int(reportedCases * 10)}
  
  impact = { 'currentlyInfected' : int(reportedCases * 10),
             'infectionsByRequestedTime' : int(impact['currentlyInfected'] * (2 ** int(requestedTime/3)))}
  
  impact = { 'currentlyInfected' : int(reportedCases * 10),
             'infectionsByRequestedTime' : int(impact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * impact['infectionsByRequestedTime'])}
  
  impact = { 'currentlyInfected' : int(reportedCases * 10),
             'infectionsByRequestedTime' : int(impact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * impact['infectionsByRequestedTime']),   
             'hospitalBedsByRequestedTime' : int((0.35 * int(data['totalHospitalBeds']))- 
                                                 impact['severeCasesByRequestedTime'])}
  
  impact = { 'currentlyInfected' : int(reportedCases * 10),
             'infectionsByRequestedTime' : int(impact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * impact['infectionsByRequestedTime']),   
             'hospitalBedsByRequestedTime' : int((0.35 * int(data['totalHospitalBeds']))-
                                                  impact['severeCasesByRequestedTime']) }
             
  
  impact = { 'currentlyInfected' : int(reportedCases * 10),
             'infectionsByRequestedTime' : int(impact['currentlyInfected'] *
                                                (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * impact['infectionsByRequestedTime']),   
             'hospitalBedsByRequestedTime' : int((0.35 * int(data['totalHospitalBeds']))- 
                                                 impact['severeCasesByRequestedTime']),            
             'casesForICUByRequestedTime' : int(0.05 * impact['infectionsByRequestedTime']) }
  
  impact = { 'currentlyInfected' : int(reportedCases * 10),
             'infectionsByRequestedTime' : int(impact['currentlyInfected'] *
                                                (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * impact['infectionsByRequestedTime']),   
             'hospitalBedsByRequestedTime' : int((0.35 * int(data['totalHospitalBeds']))- 
                                                 impact['severeCasesByRequestedTime']),            
             'casesForICUByRequestedTime' : int(0.05 * impact['infectionsByRequestedTime']),  
             'casesForVentilatorsByRequestedTime' : int(0.02 * impact['infectionsByRequestedTime']),
             'dollarsInFlight' : int((impact['infectionsByRequestedTime']) *
                                       (data['region']['avgDailyIncomePopulation']) * 
                                     (data['region']['avgDailyIncomeInUSD']) / requestedTime)
             } 
  
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50)}
  
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50),
             'infectionsByRequestedTime' : int(severeImpact['currentlyInfected'] * (2 ** int(requestedTime/3)))}
  
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50),
             'infectionsByRequestedTime' : int(severeImpact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * severeImpact['infectionsByRequestedTime'])}
  
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50),
             'infectionsByRequestedTime' : int(severeImpact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * severeImpact['infectionsByRequestedTime']) }
  
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50),
             'infectionsByRequestedTime' : int(severeImpact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * severeImpact['infectionsByRequestedTime']),   
             'hospitalBedsByRequestedTime' : int((0.35 * int(data['totalHospitalBeds']))- 
                                                 severeImpact['severeCasesByRequestedTime']) }
  
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50),
             'infectionsByRequestedTime' : int(severeImpact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * severeImpact['infectionsByRequestedTime']),   
             'hospitalBedsByRequestedTime' : int((0.35 * int(data['totalHospitalBeds']))- 
                                                 severeImpact['severeCasesByRequestedTime']) }
  
  severeImpact = { 'currentlyInfected' : int(reportedCases * 50),
             'infectionsByRequestedTime' : int(severeImpact['currentlyInfected'] * (2 ** int(requestedTime/3))),
             'severeCasesByRequestedTime' : int(0.15 * severeImpact['infectionsByRequestedTime']),   
             'hospitalBedsByRequestedTime' : int((0.35 * int(data['totalHospitalBeds']))- 
                                                 severeImpact['severeCasesByRequestedTime']),            
             'casesForICUByRequestedTime' : int(0.05 * severeImpact['infectionsByRequestedTime']),  
             'casesForVentilatorsByRequestedTime' : int(0.02 * severeImpact['infectionsByRequestedTime']),
             'dollarsInFlight' : int((severeImpact['infectionsByRequestedTime']) *
                                       (data['region']['avgDailyIncomePopulation']) * 
                                     (data['region']['avgDailyIncomeInUSD']) / requestedTime)
             } 
  
  output_data = {
    'data' : data,
    'impact': impact,
    'severeImpact' : severeImpact
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
  # print(result)
  pprint.pprint(result)
    
    
if __name__ == "__main__":
  main()