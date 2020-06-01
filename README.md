This python scripts filters the results from the Sublist3r and sorts that to a list of responding web sub-domains 

It does the following by :
1. Reading the output file from sublist3r 
2. Make a sorted list without explict information
3. Performs a ping test to each host
4. Adds all the responding hosts to an output file


/***********************************************<br>
**<i><font size = "+2"> Note : This Script only works with python3  </font></i> **<br>
***********************************************/

<font size = "+2"><b>How to run this script : </font></b><br>
python3 subDomainFilter.py [-i/--input] <name_of_the_input_file> [-o/--output] <name_of_the_output_file>


<font size = "+2"><b>Python Command :</font></b>
<br>

<i>short verbose :<i>
![short verbose](images/command-short.jpg)

<br><br>
<i>verbose containing complete arguments :<i>
![verbose containing complete arguments](images/command-longer.jpg)


<br><br>
<i>verbose containing complete arguments and file dir :<i>
![verbose conatining complete arguments and file dir](images/command-longest.jpg)
