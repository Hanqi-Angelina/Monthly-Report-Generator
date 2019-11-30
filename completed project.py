#input part(revised version of professor's code in labe 8)
import csv 

#the simplified version for professor's code for input

def read_csv():
    ''' () -> (list, list)

    Given a csv file_name, open and read the file.
    Return header and database:
     - The header is the list of the columns' names
     
     - The database is a list of lists that contains all the records.

    REQ: file_name has to be a valid csv file with a header
    '''
    # Open the file given so we can read what's inside
    with open(FILE_NAME) as reader_file:
        # Read the file
        reader = csv.reader(reader_file)
        # Make it a list type, so it's easier for us to manage the data
        data = list(reader)
    # The first row of the data has the header
    # The rest of the data are records and will be stored in the database
    return (data[0], data[1:])  

 
#revised version for the output part
#change from write mode to append mode to be easier to add things



def write_to_csv(data):
    ''' (list) -> NoneType

    Write the data to the csv file.

    REQ: data must be a list of lists with consistent number of columns (in each row)
    '''
    # open a file so we can append it 
    with open(FILE_NAME, 'a', newline="") as writer_file:
        writer = csv.writer(writer_file)
        # write the new data at the end of the original file
        writer.writerows(data)

def cal_average(variable_name):
    ''' (str) -> float 
    calculate the average of data
    
    the sum will be calculated by column
    
    the average will be sum divdided by the number of lines in which the data is in.
    
    REQ: variable_name must be in the list of header 
    '''
    var_sum = 0
    ave_sum = 0 
    for variable_index in range(8):
        if header[variable_index] == variable_name:
            break 
    for index in range(0,length,1):
        #calculate the sum of the varibale 
        var_sum = var_sum + float(my_file[index][variable_index])
    ave_sum = var_sum/(length)
    return(ave_sum)

def cal_max(digit):
    ''' (int) -> float
    
    get the maximum of each column of data and output it 
    
    REQ: the digit should only be intergers from 1 to 7 
    
    '''
    var_max = -1000.0
    for index in range(0,len(my_file),1):
        #calculate the max of the varibale 
        var_max = max(var_max,float(my_file[index][digit]))
    return(var_max)

def cal_min(digit):
    '''(int) -> float
    
    get the minimum of each column of data and output it 
    
    REQ: the digit should only be intergers from 1 to 7 
    
    '''
    var_min = 20000.0
    for index in range(0,len(my_file),1):
        #calculate the min of the varibale 
        var_min = min(var_min,float(my_file[index][digit]))
    return(var_min)
    
def cal_dew_po(tem,RH):
    ''' (float, float) -> float 
    
    calculate the dew point(the formula is from EESA01 course)
    
    >>> cal_dew_po(10.0,23.4)
    -5.3199999999999985
    
    >>> cal_dew_po(14.0,90.0)
    12.0
    
    '''
    dew_po = 0 
    dew_po = tem - ((100 - RH)/5)
    return(dew_po)
    
def cal_vap_pre(dew):
    ''' (float)-> float
    
    calculate the vapour pressure(the formula is from EESA01 course)
    
    >>> cal_vap_pre(12.2)
    14.215910388235216
    
    >>> cal_vap_pre(-5.4)
    4.086927814460807
    
    '''
    vap_pre = 0 
    vap_pre = 6.11 * 10**((7.5*dew)/(237.3+dew))
    return(vap_pre)


def cal_humidex(dew,vap_pre):
    ''' (float,float) -> float
    calculate the humidex(the formula is from the EESA01 course)
    '''
    humi = 0 
    humi = dew + 0.5555*(vap_pre - 10) 
    return(humi)
    


# make prediction according to the data 


# condition 


def know_wet_or_not():
    ''' ()-> str
    return dry iff the average precipitation is strictly less than 0.2 and return wet iff the average precipitation is greater or equal to 0.2.
    '''
    # when the conditon is dry
    if ave_Ra < 0.2:
        return "the area is experiencing a dry month"
    # when the condition is wet
    else:
        return "the area is experiencing a wet month"
    
def heat_waves():
    ''' ()-> str
    know whether or not a heat wave occurs
    return found heatwave iff a 3 consecutive days with temperature 30 or greater occurs otherwise return no heatwaves found. 
    '''
    variable_index = 1 
    heat_waves = ""
    index = 0 
    #loop over the temperature column to examine all the value if it is at least 30 or greater 
    while index < length:
        #check whether there are consecutive hot days:  
        if float(my_file[index][variable_index]) >= 30:
            if float(my_file[index+1][variable_index]) >= 30:
                if float(my_file[index+2][variable_index]) >= 30:
                    # if there exist heat waves, give prediction and precaution
                    heat_waves = "There exist heat waves this month,High persistent temperatures increase the risk of drought and severely impact food production and increases the risk of wildfire.\n Lead to more thunderstorms, which means increased risks of flash flooding, lightning, hail and possibly even tornadoes.\n \n People are much more susceptible to suffer from heat exhaustion and heat stroke. Many outdoor activities become dangerous or impossible. Remember to stay hydrated and drink plenty of water.Also, put some sunscreen shots to prevent sunburns. "
                    return(heat_waves)
            else:index = index + 1 
        index = index +1
    return("There are no heat waves this month")
    
    
        
        
def wind_dir():
    ''' ()->str
    know form the data that how the wind direction is dominant in one specific area 
    '''
    N = 0 
    S = 0 
    E = 0 
    W = 0 
    #find the column for wind direction
    for variable_index in range(9):
        if header[variable_index] == "WindDir":
            break 
    #loop over the wind direction column and count the number for each direction
    for index in range(0,len(my_file),1):
        if float(my_file[index][variable_index]) <=45 or float(my_file[index][variable_index]) >315:
            N = N +1
        elif float(my_file[index][variable_index]) >225:
            W = W +1
        elif float(my_file[index][variable_index]) >135:
            S = S +1
        else: 
            E = E+1
    wind_max = max(N,W,E,S)
    dir_max = ""
   
    #if there is only one direction with the highest count,
    #set the dominant wind direction for the direction with the highest count
    if wind_max == N:
        dir_max = "N"
    #set the dominant wind for both if there are two direction with the highest count 
    if wind_max == W:
        dir_max = dir_max+"W"
    if wind_max == E:
        dir_max = dir_max+"E"
    if wind_max == S:
        dir_max = dir_max+"S"
    
    #set the dominant wind direction for "not exist" if two inverse wind direction are with the same highest count     
    if ("N" in dir_max and "S" in dir_max) or ("E" in dir_max and "W" in dir_max):
        dir_max = "not exist"
    return("the dominant wind direction is "+ dir_max)

def mild_or_cold_winter():
    '''()-> str
    know from the data whether the month is mild or cold winter or not
    Return ("mild winter" and the relevant precaution if the the temperature is in the range of -30 to -5)
    Return ("cold winter" and the relevant precaution) iff ave_tem <= -30 ¡ãC
    '''
    variable_index = 1 
    precaution = ""
    if ave_tem <= -5:
        if ave_tem > -30:
            precaution = "Dress Warmly: Dress in bundles and layers, and a wind resistant outer layer. Wear either a hat, mittens or insulated gloves and scarf, neck tube or facemask to keep the face warm. Wear a proper waterproof footwear."
            return("mild winter\n" + precaution)
        else:
            precaution = "Watch for signs of frostbite and hypothermia \n Dress Warmly: Dress in bundles and layers, and a wind resistant outer layer. Wear either a hat, mittens or insulated gloves and scarf, neck tube or facemask to keep the face warm. Wear a proper waterproof footwear. \n Definitions: \n Hypothermia is severe drop in body temperature due to being cold over a prolonged period of time \n Frostbite is a more severe condition, where both the skin and the underlying tissue (fat, muscle, bone) are frozen. \n"
            return(["cold winter\n" + precaution])
    return("It has not been in mild or cold winter yet")
    
def BP():
    ''' ()-> str
    Know from BP what kind of day will people experiencing
    return the associated condition, prediction and precaution 
    If 98 kPA<= Barometric Pressure <= 104 kPA, then the atmospheric condition is in good condition.
    If BP <98, the area is experiencing low pressure
    If BP>104 kPA, the area is experiencing high pressure. 
    '''
    if ave_BP < 98:
        condition = "The area is experiencing low pressure.\n"
        prediction = "This indicate that there isn't enough force, or pressure, to push clouds or storms away.\n"
        precaution ="Low-pressure systems predict a cloudy, rainy, or windy weather. Be cautious for a heavy rainfall possibly rainstorms coming \n"
        return(condition + prediction+precaution)
    elif ave_BP > 104:
        condition = "The area is experiencing high pressure.\n On the body: Higher air pressure feels better on your joints by constricting the tissues and prevent it from expanding. \n"
        prediction ="High-pressure systems are usually associated with clear skies and calm weather\n"
        return(condition + prediction)
    else:
        return("The atmospheric pressure is in good condition")

def pre_dew_point():
    ''' ()->str
    determine what the person would the most in a month
    If Dewpoint = Air Temperature, then the air saturated with water vapour
    If Dewpoint < Air Temperature, then this indicates that the air is unsaturated with vapour, which means more water could evaporate. 
    People feels comfortable as the body can cool down as water evaporates to the form dew.
    If Dewpoint > Air temperature, then the air already saturated with vapour which results to people feeling hot or sticky.
    '''
    body_feeling = ""
    if dew_po == ave_tem:
        condition = "Condition:the air saturated with water vapour"
        return(condition)
    
    elif dew_po < ave_tem:
        condition = "Condition: This indicates that the air is unsaturated with vapour, which means more water could evaporate"
        return(condition+"\nBody feeling: People feels comfortable as the body can cool down as water evaporates to the form dew.")
        
    else:
        condition = "Condition: The air already saturated with vapour "
        body_feeling = "\nBody feeling: This results to people feeling hot or sticky, because the air slows down the evaporation of sweat from the body and inhibit heat regulation in the body"
        return(condition+body_feeling)


def wind_speed():
    ''' ()-> str
    provide precautionary statements that could occur wihthin the month
    If Wind Speed > 74 km/h, this indicates that the area is experiencing a high wind warning
    Precautions: Ensure that all objects outside are secured. Refrain from driving during this time because these winds will make driving very difficult, especially for larger vehicles. Winds this strong may cause damage to power lines and small buildings and trees to fall down.
    '''
    if ave_WS > 74: 
        condition="High wind warning"
        precaution = "\n Precaution: Ensure that all objects outside are secured. Refrain from any unnecessary driving during this time since these winds will make driving very difficult, especially for high profile vehicles. Winds this strong may damage trees, power lines and small structures"
        return(condition + precaution)
    else:
        return("The wind speed is within the normal range")


def solar_ir():
    ''' ()-> str
    correlation between the input energy from the sun to the monthly temperature
    When Solar Irradiance > 1361 W/m2, the energy received from the sun is above the average. This can indicate higher temperatures for a month.
    When the energy received from the sun is below the average. This can indicate a colder temperature for the month.  
    '''
    Solar_Ir = ave_Sl*(length)
    condition = "average temperature in a year"
    if Solar_Ir > 1361:
        condition = "The energy received from the sun is above the average. This can indicate higher temperature days for the month"
    elif Solar_Ir < 1361:
        condition = "The energy received from the sun is below the average. This can indicate a colder temperature days for the month"
    return(condition)


#operation part 

FILE_NAME = "July_2019.csv"
my_file = read_csv()[1]
header = read_csv()[0]
print(my_file)
length = len(my_file)
ave_tem = cal_average("AirTC")  
ave_RH = cal_average("RH") 
ave_BP = cal_average("BP_kPa")
ave_Ra = cal_average("Rain_mm")
ave_WS = cal_average("WS_kph")
ave_WindDir = cal_average("WindDir")
ave_Sl = cal_average("SlrW")
dew_po = cal_dew_po(ave_tem,ave_RH)
vap_pre = cal_vap_pre(dew_po)
humidex = cal_humidex(dew_po,vap_pre)
maximum = ["maximum"]
minimum = ["minimum"]

# add all the calculated staff to the csv
# loop through all the rows contain data to get the maximum and minimum of each column 
for digit in range(1,8,1):
    maximum.append(cal_max(digit))
    minimum.append(cal_min(digit))
# write all the calculated data to the csv 
write_to_csv([["Average",str(ave_tem),str(ave_RH),str(ave_BP), str(ave_Ra),str(ave_WS),str(ave_WindDir),str(ave_Sl)]])
write_to_csv([["dew point",str(dew_po)]])
write_to_csv([["vapour pressure", str(vap_pre)]])
write_to_csv([["humidex", str(humidex)]])
write_to_csv([maximum])
write_to_csv([minimum])


#output to a txt file

from typing import TextIO

tem = "the average temperature is " +str(round(ave_tem,2)) + " C"+"\n"+"\n" 
RH = "the average Relative Humidity is " +str(round(ave_RH,2))+" %"+"\n"+"\n"
BaP = "the average Barometric Pressure is " +str(round(ave_BP,2))+" kPa"+"\n"+"\n"
WS = "the average wind speed is " +str(round(ave_WS,2))+" kph"+"\n"+"\n"
Sl = "the average solar irradiance is " +str(round(ave_Sl,2))+" W/m^2"+"\n"+"\n"
Ra = "the average rainfall is " +str(round(ave_Ra,2))+" mm"+"\n"+"\n"


f = open("generatedreport.txt","w")
# turn all the output of condition into a string 
a = "Brief Monthly Weather Report\n" +"\n"+"\n"+ tem + RH + BaP+ WS + Sl + Ra + know_wet_or_not() +"\n" +"\n" + wind_dir() +"\n" + "\n" + mild_or_cold_winter() + "\n" + "\n" + BP() + "\n" + "\n"  + pre_dew_point() + "\n" + "\n" + wind_speed() + "\n" + "\n" + solar_ir() +"\n"+"\n"+ heat_waves()

f.write(a)

f.close()
