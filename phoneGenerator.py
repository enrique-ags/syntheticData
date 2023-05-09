#data phone generator
import random
import pytest
def generatePhoneNumbers(Country,State,Limit):#function to generate phone numbers
    directory=[]
    countryCode=''
    stateCode=''
    fullPhone=''
    
    for i in range(0,Limit):
        
        for x in range(0,8):
            n = random.randint(0,9)
            directory.append(n)
            string = ''.join([str(item) for item in directory])
            countryCode=getCountry(Country)
            stateCode = getState(State)
            fullPhone = str(countryCode) + str(stateCode) + string
        print(fullPhone)
        directory.clear()
def generatePhoneNumbersandExportToSQLDump(Country,State,Limit,tableName,DB):#function to generate phone numbers
    sqlString='Insert into ' + tableName + '(id,phoneNumber) values ('
    directory=[]
    countryCode=''
    stateCode=''
    fullPhone=''
    
    for i in range(0,Limit):
        
        for x in range(0,8):
            n = random.randint(0,9)
            directory.append(n)
            string = ''.join([str(item) for item in directory])
            countryCode=getCountry(Country)
            stateCode = getState(State)
            fullPhone = str(countryCode) + str(stateCode) + string 
        print(sqlString  + str(x)+ ',' + fullPhone + ')')
        directory.clear()

def getCountry(code): #python dictionary  for country
    countryCode={'MX':52,'USA':1,'CA':1,'DE':49}
    return countryCode[code]

def getState(StateCod): #python dictionary for state
    StateCode={'Aguascalientes':449,'Chihuahua':614,'Guadalajara':333,'Salt Lake City':385}
    return StateCode[StateCod]
