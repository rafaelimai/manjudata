# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 22:29:00 2020
 
# Released under MIT License

Copyright (c) 2020 Rafael.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

"""

Term Structure Generator

- Assists on the generation of a simple term structure, considering all days for the sake of simplicity.
- A term structure can be specified by a number of days to be considered and rates for the vertexes
- Outputs include the curve as a CSV file, considering 1 as the first point, and a neat graph.

"""

def main():
    print("Term structure generator")
    name = input("Please enter a name:")
    daycount = input("Please enter the total amount of days:")
    
    

