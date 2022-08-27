# display the city options
# make the user select two cities
# calculate and print the distance

from math import sqrt
import cities


cities_lat_coordinates = {
    "London" : 51.509865,
    "Buenos Aires" : -34.58333333,
    "Baku" : 40.38333333,
    "Sofia" : 42.68333333,
    "Ottawa" : 45.41666667,
    "Havana" : 23.11666667,
    "Helsinki" : 60.16666667,
    "Paris" : 48.86666667,
    "Berlin" : 52.51666667,
    "Athens" : 37.98333333,
    "Moscow" : 55.75,
    "D.C." : 38.883333,
    "İstanbul" : 41.015137
}
cities_long_coordinates = {
    "london" : -0.118092,
    "Buenos Aires" : -58.666667,
    "Baku" : 49.866667,
    "Sofia" : 23.316667,
    "Ottawa" : -75.7,
    "Havana" : -82.35,
    "Helsinki" : 24.933333,
    "Paris" : 2.333333,
    "Berlin" : 13.4,
    "Athens" : 23.733333,
    "Moscow" : 37.6,
    "D.C." : -77,
    "İstanbul" : 28.979530 }

select1 = input ("select the first city")
select2 = input ("select the second city")

def distance_calc(select1,select2):
    
    first_lat = cities_lat_coordinates[select1] 
    second_lat = cities_lat_coordinates[select2]
    
    first_long = cities_long_coordinates[select1]
    second_long = cities_long_coordinates[select2]   

    distance = round (sqrt((first_lat - second_lat)**2) + ((first_long - second_long)**2),3)
    
    print (distance)
    
distance_calc(select1,select2)