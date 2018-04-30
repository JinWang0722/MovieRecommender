# MovieRecommender
=================HOW TO RUN PYTHON CODE=====================

Type: python CodeName -f InputFileName -s MinSupport -c MinConfidence -r OutputFileName
For example, if you wanna test my code on vote.arff, and set the minimum support and minimnum confidence both 0.5, and generate a output file named "1.txt"
Type: python jin1.py -f vote.arff -s 0.5 -c 0.5 -r 1.txt, and press ENTER

NOTE: when test some other dataset, please make sure that the format of the input file must be exactly same as following. Extra blank line may cause some error when read the data.

The format should be:
@relation.....
BLANK LINE
@attribute.....
BLANK LINE
@data
n,y,n,y,......... 
==========================================================



=================File Description=========================
There are 9 files for association rules part.
jin1.py---------Use Yan's output file (utilize CF to fill the missing values) as input, genrate                      association rules.
jin2.py---------Same as jin1.py, but output file is just support, confidence, and lift. Use this                     output file to plot the scatter graph in matlab.
jin3.py---------Use raw data (ratings.csv) as input file, generate association rules.
jin4.py---------Same as jin3.py, but output file is just support, confidence, and lift. Use this                     output file to plot the scatter graph in matlab.

RatingTrans.java & RatingTrans2.java -----Preprocessing for the raw data.

trans.m & trans2.m------------------------Preprocessing for Yan's output file. Yan did his CF part by using matlab, and finally his program would output a file (a .mat file). Therefore, I need to use matlab to do the preprocess. 

README----------Description. 

Since the data file after preprocessing 
================================================================


