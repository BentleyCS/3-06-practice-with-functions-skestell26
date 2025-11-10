#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(n1,n2,n3):
    semiPerimeter = (n1+n2+n3)/2
    return semiPerimeter


def multiplyDifferences(dif, n1,n2,n3):
    #dif=semiPerimeter(n1,n2,n3)
    dif = dif*(dif-n1)*(dif-n2)*(dif-n3)
    return(dif)



#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    s = semiPerimeter(a,b,c)
    area=multiplyDifferences(s, a,b,c)
    area = root(area)
    return area


#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(number):
    return number*2

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(a,b):
    ModifiedArgumentOne= a*(-1)
    argumentTwo= b
    return ModifiedArgumentOne + argumentTwo, ModifiedArgumentOne - argumentTwo

#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    multResults=(a*c)*4
    return (b**2)-multResults


#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    m=mainCalc(a,b,c)
    s= root(m)
    x1,x2 = plusMinus(b,s)
    d= denominator(a)
    return x1/d, x2/d
