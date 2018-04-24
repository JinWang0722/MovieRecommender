# MovieRecommender
=================HOW TO RUN MY CODE=====================

Type: python CodeName -f InputFileName -s MinSupport -c MinConfidence -r OutputFileName
For example, if you wanna test my code on vote.arff, and set the minimum support and minimnum confidence both 0.5, and generate a output file named "1.txt"
Type: python jin1.py -f vote.arff -s 0.5 -c 0.5 -r 1.txt, and press ENTER

NOTE: the default input filename is "vote.arff", the default minimum support and confidence are both 0.5, the default output file name is "output_jin.txt"

NOTE: when test some other dataset, please make sure that the format of the arff file must be exactly same as the vote.arff. Extra blank line may cause some error when read the data.

The format should be:
@relation.....
BLANK LINE
@attribute.....
BLANK LINE
@data
n,y,n,y,......... 
==========================================================



=================File Description=========================
There are 10 files and 2 folders for this assignment.

Screenshot------All original file of screenshots in report are kept in this folder. Since there is a resolution problem, the screenshots in the report may not be 		very clear.

txtOutput-------All generated output files are kept here. 01.txt~ 03.txt are the results of Test_1.arff ~ Test_3.arff
		plot01.txt ~ plot10.txt are results of FigureB in report.
	        
jin1.py---------Python code for programming part. Will print the result and output an txt file.

jin2.py---------Python code for programming part. Will only print the runtime and rule number. It will output a same txt file as jin1.py. 
                jin2.py comments most of the print instructions to achieve a better performance.

plot.xlsx-------The original file for generating the plot figure.

Wang_Kurupalli.pdf------The report for this assignment with contribution form.

Test_1.arff-----The test case 1 in report. small data set.

Tsst_2.arff-----The test case 2 in report. medimum data set.

Test_3.arff-----The test case 3 in report. large data set.

Test_for_plot.arff-----The test case for plot part in report.

vote.arff-------A provided dataset. 

README----------Description. 

================================================================


