import sys

filename = "vote.arff"; 
out_file = "output_jin.txt"; # this is the name of outputing txt file by default
minSupport = 0.1;
minConfidence  = 1.0;

#obj = None;
record = list();#all transactions
itemSet = set();#instances labels0
freqItems = list();#support count
ruleItems = list();#association rules

def main():
    arguments_option = None;
    parser = OptionParser();
    parser.add_option("-f", "--file", dest = "filename", help = "Write file name after '-f'", default = "vote.arff");
    parser.add_option("-s", "--min support", dest = "minSupport",help = "Write a minimum support after '-s'",default = 0.5);
    parser.add_option("-c", "--min confidence", dest = "minConfidence",help = "Write a minimum confidence after '-c'", default = 0.5);
    parser.add_option("-r", "--output file", dest = "out_file", help = "Write file name after '-r'", default = "output.txt");
    (arguments_option, args) = parser.parse_args();
    inFile = None;
    if arguments_option.filename is not None:      
        minSupport  = arguments_option.minSupport;
        outFile = open(arguments_option.out_file,"w");
        minConfidence = arguments_option.minConfidence; 
        filename   = arguments_option.filename;
        # print "_________________________________________________________________";
        # print "DataMining_HW2_Apriori:";
        # print "*********************************";
        # print "Read data from \'" + filename + "\'";
        print "The minimum support is " + minSupport;
        print "The minimum confidence is " + minConfidence;
        # print "=================================";

        outFile.write("_________________________________________________________________\r\n");
        outFile.write("DataMining_HW2_Apriori:\r\n");
        outFile.write("*********************************\r\n");
        outFile.write("Read data from \'" + filename + "\' \r\n");
        outFile.write("The minimum support is " + minSupport+"\r\n");
        outFile.write("The minimum confidence is " + minConfidence+"\r\n");
        outFile.write("=================================\r\n");       
        objSet, recordSet = readData(filename);
        apriori(objSet, recordSet, minSupport, minConfidence, outFile);
    else:
        #print "No found file, exit."
        sys.exit();
from optparse import OptionParser

#load data
def readData(name):
    readFile = open(name, "rU");
    itemSet  = set();
    itemSet2  = set();
    record   = list();
   
    obj = [];
    attIndex=0;
    acounter = 0;
    
    # while(1):
    #     t= readFile.readline()
    #     t= t.strip().rstrip();
    #     if(t!=None and len(t)!=0):
    #         temp = t.split(" ");
            
    #         sy = str(attIndex)+("=y");
    #         # sn = str(attIndex)+("=n");
    #         attIndex = attIndex+1;  
    #         objy.append(sy);
    #         # objn.append(sn);
    #         obj.append(temp[1]);
    #     else:
    #          break;    

    # for o in objy:
    #     itemSet.add(frozenset([o]));
    # for o in obj:
    #     itemSet2.add(frozenset([o]));
    t= readFile.readline(); 
    
    while(1):
        t= readFile.readline();
        t= t.strip().rstrip();
        idv= set();
        if(t!=None and len(t)!=0):
            temp = t.split(",");
            for s in temp:               
                idv.add(s);
                obj.append(s);
                transactionl = frozenset(idv);
            record.append(transactionl);                   
        else:
             break;
    for o in obj:
        itemSet.add(frozenset([o]));
        itemSet.add(frozenset([o]));          
    return itemSet, record;

from collections import defaultdict
from itertools import chain, combinations
from decimal import *
from itertools import chain	

def getLK(items, trans, minSupport, freqSet):
    tempSet    = defaultdict(int);
    itemSet    = set();
    	
    for item in items:
        for tran in trans:
            if item.issubset(tran):
                tempSet[item] = tempSet[item]+1;
                freqSet[item] = freqSet[item]+1;
                

    for item, count in tempSet.items():
        total=len(trans);
        curSupportCount = float(count);
        curSupport = curSupportCount / total;
		
        if (Decimal(curSupport) >= Decimal(minSupport) and curSupport >=0):
            itemSet.add(item);
			
    return itemSet;
	
def getSupport(freqSet, tranList, item):
    x = float(freqSet[item]);
    y = len(tranList);
    support = -1;
    if (y != 0):
        support = float(x / y);
    return support;

#return the support count
def getSupportNum(item,tranList):   
    count = 0;
    for s in tranList:
        if(set(item).issubset(s)):
            count = count +1;
    return count;    
	
def getUnion(itemSet, l):
    resultSet = set();
    for i in itemSet:
        for j in itemSet:
            if (len(i.union(j)) == l and len(i.union(j))>=0):
                resultSet.add(i.union(j));
    return resultSet;
	
def apriori(attName, recordList, support, minConfidence, outFile):
    #count time from here
    t_start     = time.time();
    tranList    = recordList;
    itemSet     = attName;
    z=0;
    canSet      = dict();
    freqSet     = defaultdict(int);	
    firstSet    = getLK(itemSet, tranList, support, freqSet);
    curSet      = firstSet;  
    k = 2;
    while (len(curSet) !=0):
        canSet[k - 1] = curSet;
        curSet = getUnion(curSet, k);
        curSet = getLK(curSet, tranList, support, freqSet);
        k += 1;
		
    #frequent item set
    freqItems = list();	
	
    #print "Support items: ";
    #print "***************************************************************************************";
    outFile.write("Support items: \r\n");
    outFile.write("***************************************************************************************\r\n");
    
    for index, items in canSet.items():
        for item in items:
            sup = getSupport(freqSet, tranList, item);
            freqItems.extend([(tuple(item), sup)]);

    buckets = []
    for i in xrange(0,100):
        buckets.append(0);
    x=0;
    for item, support in freqItems:
        buckets[len(item)]=buckets[len(item)]+1;
        if(len(item)>x):
            x=len(item);
        #print str(item) + "; support=" + str(support);
        outFile.write(str(item) + "; support=" + str(support)+"\r\n");
    #print "***************************************************************************************";
    outFile.write("***************************************************************************************\r\n");
    #print "Generated sets of large itemsets:"
    outFile.write("Generated sets of large itemsets:\r\n");
    y=1;
    while(y<=x):
        #print "Size of set of large itemset L(",y,"): ",buckets[y];
        outFile.write("Size of set of large itemset L("+str(y)+"): "+str(buckets[y])+"\r\n");
        y=y+1;
    #print "***************************************************************************************";
    resultSet = set();
    outFile.write("***************************************************************************************\r\n");
    #associate rules
    #print "Associate rules: ";
    ruleItems = list();	
    #print "***************************************************************************************";
    outFile.write("Associate rules: \r\n");
    outFile.write("***************************************************************************************\r\n");
    assFrequence = 0;
    for index, items in canSet.items()[0:]:
        for item in items:
		    #generate all possible rules
            resultSet = chain(*[combinations(item, r + 1) for r, a in enumerate(item)]); 
            if(resultSet is not None):
                subset = map(frozenset, [x for x in resultSet]);
            for e in subset:
                rightSet = None;
                if(len(item.difference(e))>0):				
                    rightSet = item.difference(e);
                    allSupport = getSupport(freqSet, tranList, item);
                    leftSupport = getSupport(freqSet, tranList, e);
                    confidence = allSupport/leftSupport;
                    if Decimal(confidence) >= Decimal(minConfidence):
                        ruleItems.append(((tuple(e), tuple(rightSet)), confidence));
               
    for rule, confidence in ruleItems:
        assFrequence += 1;
        #print "rule_",assFrequence,": [",rule[0]," ",getSupportNum(rule[0], tranList)," -> ",rule[1]," ",getSupportNum(rule[1], tranList),"]; confidence=" + str(confidence); 
        #outFile.write("rule_"+str(assFrequence)+": ["+str(rule[0])+" "+str(getSupportNum(rule[0], tranList))+" -> "+str(rule[1])+" "+str(getSupportNum(rule[1], tranList))+"]; confidence=" + str(confidence)+"\r\n");
        s=float(float(getSupportNum(rule[1], tranList))/float(len(tranList)));
        outFile.write(str(s)+", "+str(confidence)+", "+str(float(confidence)/float(s))+"\r\n");
    #print "***************************************************************************************";
    outFile.write("***************************************************************************************\r\n");
    print "The number of association rules is: " + str(assFrequence);
    #time end here    
    outFile.write("The number of association rules is: " + str(assFrequence)+"\r\n");
    t_end=time.time();
    t = t_end - t_start;
    print t, "seconds are used.";
    outFile.write(str(t)+ "seconds are used.\r\n");
    #print "_________________________________________________________________";
    outFile.write("_________________________________________________________________\r\n");
    pass;
import time



if __name__ == "__main__":
    main();
    
