#!/usr/bin/env python3
#Accuracy achieved - 72.5%

#Decision decisions
# re package in python was used to remove special characters from the tweet like "-","_",'\r','\n','.','!','*', #
# All the single character words were removed
# Stop words were ignored while computing probabilites
#all words were converted to lowercase as for example words like job and Job  were getting printed in high probability word list
# When test probabilities for words that are not in train, a default probability of 1/(number of words from all tweets combined in training data) was assumed

import re
import itertools
from itertools import chain
import numpy as np
import sys

train_File = sys.argv[1]
test_File = sys.argv[2]
output_File = sys.argv[3]

stop_words = ['will', 'other', 'weren', 'same', 'do', 'myself', 'in', 'out', 'such', 'just', 'should', 'about', 'their', "didn't", 'hers', 'won', 'a', 'has', 've', "don't", 'doesn', "wasn't", 'again', 'itself', 'didn', 'they', 'mightn', "won't", 'me', 'an', 'my', "mustn't", 'y', 'what', 'over', 'had', 'own', 'before', 'that', "you'll", 'shan', 'his', 'then', 'as', 'don', 'from', "she's", 'have', 'under', 'can', "couldn't", 'than', 'of', "doesn't", 'into', 'few', 'your', 'but', 'until', 'when', "isn't", 'the', "you've", 'there', 'more', 'hasn', 'doing', 'isn', 'some', 'how', "weren't", "shouldn't", 'through', 'up', 'all', 'i', 'each', "haven't", 'was', 'himself', 'nor', 'you', 'having', 'ain', 'aren', 'shouldn', "should've", 'll', 'above', "hasn't", 'any', 'mustn', 'if', 'off', 'does', 'ourselves', 'so', 'ma', 'themselves', 'no', 'here', "mightn't", 'most', "shan't", 'am', 'not', 'him', 'did', 'while', 'where', 'her', 'wasn', 'very', 'd', 's', 'herself', 'them', 'its', 'by', 'm', 'ours', 'who', 'both', 'against', 'wouldn', 'during', 'to', 'why', 'now', 'couldn', 'yours', 'because', 'this', 'too', 'being', 'were', 'he', 'been', 'are', 'only', 'whom', 're', 'she', 'o', "wouldn't", 'those', "needn't", 'after', 'which', 'it', "you're", 'yourselves', 'at', 'our', "that'll", "it's", 'with', 'we', 'between', 't', 'haven', 'these', 'further', "hadn't", "aren't", 'on', 'or', 'hadn', 'and', 'down', 'for', "you'd", 'needn', 'once', 'yourself', 'theirs', 'be', 'is', 'below']

tweets_Seperate = {}
training_Cities = []

#Reading input train file and ignoring stop words and single character words
with open(train_File, 'r+') as f:
    for line in f.readlines():
        line = re.sub('[^ a-zA-Z0-9]', '', line)
        line = re.sub(r' +', ' ', line)
        line = line.split(' ')
        line = [x.lower() for x in line]
        for ind_Word in line:
            if ind_Word in stop_words  or len(ind_Word) == 1:
                index_Word = line.index(ind_Word)
                del line[index_Word]
            else:
                continue
        city = line[0]
        training_Cities.append(city)
        line.pop(0)
        tweets_Seperate.setdefault(city,[]).append(line)
city_Counts = {}
#print(tweets_Seperate)
#Creating a dictionary to count the occurences of a city in training file
for city in training_Cities:
    if city in city_Counts.keys():
        city_Counts[city] +=1
    else:
        city_Counts[city] = 1

#Computing the probability of each city based on the number of occurences in training file
city_Counts = {x: city_Counts[x]/len(training_Cities) for x in city_Counts}
city_NameProbabilities  = list(city_Counts.values())


tweets_Combined = {}

#Combining all words that belong to a city in dictionary
for key,value in tweets_Seperate.items():
    l = list(chain(* value))
    tweets_Combined[key] = l
#print(tweets_Combined)
all_City_Words = list(tweets_Combined.values())
all_City_Words = list(itertools.chain.from_iterable(all_City_Words))
all_City_Words = set(all_City_Words)
all_City_Words = list(all_City_Words)
city_Names = list(tweets_Combined.keys())

#Creating dictionaries for each city to hold word:probability in dictioanry
city_One_Prob = {}
city_Two_Prob = {}
city_Three_Prob = {}
city_Four_Prob = {}
city_Five_Prob = {}
city_Six_Prob = {}
city_Seven_Prob = {}
city_Eight_Prob = {}
city_Nine_Prob = {}
city_Ten_Prob = {}
city_Eleven_Prob = {}
city_Twelve_Prob = {}
city_One_Words = [tweets_Combined[city_Names[0]],tweets_Combined[city_Names[1]],tweets_Combined[city_Names[2]],tweets_Combined[city_Names[3]],tweets_Combined[city_Names[4]],tweets_Combined[city_Names[5]],tweets_Combined[city_Names[6]],tweets_Combined[city_Names[7]],tweets_Combined[city_Names[8]],tweets_Combined[city_Names[9]],tweets_Combined[city_Names[10]],tweets_Combined[city_Names[11]]]

#Function to create word : probabiltiy for each city
def dic(list_Words,city_Dic_Name):
    for word in list_Words:
        if word in city_Dic_Name.keys():
            city_Dic_Name[word] += 1
        else:
            city_Dic_Name[word] = 1
    del city_Dic_Name['']
    city_Dic_Name = {x: city_Dic_Name[x] / len(city_Dic_Name) for x in city_Dic_Name}
    return city_Dic_Name

city_One_Prob = dic(city_One_Words[0],city_One_Prob)
city_Two_Prob = dic(city_One_Words[1],city_Two_Prob)
city_Three_Prob = dic(city_One_Words[2],city_Three_Prob)
city_Four_Prob = dic(city_One_Words[3],city_Four_Prob)
city_Five_Prob = dic(city_One_Words[4],city_Five_Prob)
city_Six_Prob = dic(city_One_Words[5],city_Six_Prob)
city_Seven_Prob = dic(city_One_Words[6],city_Seven_Prob)
city_Eight_Prob = dic(city_One_Words[7],city_Eight_Prob)
city_Nine_Prob = dic(city_One_Words[8],city_Nine_Prob)
city_Ten_Prob = dic(city_One_Words[9],city_Ten_Prob)
city_Eleven_Prob = dic(city_One_Words[10],city_Eleven_Prob)
city_Twelve_Prob = dic(city_One_Words[11],city_Twelve_Prob)

prob_DicList = [city_One_Prob,city_Two_Prob,city_Three_Prob,city_Four_Prob,city_Five_Prob,city_Six_Prob,city_Seven_Prob,city_Eight_Prob,city_Nine_Prob,city_Ten_Prob,city_Eleven_Prob,city_Twelve_Prob]


#Reading test file and computing the probabilites based on training data
with open(test_File, 'r+') as f:
    output_Final = []
    all_Predictions = []
    for line in f.readlines():
        current_Line = []
        current_Predictions = []
        original_Tweet = line
        original_Tweet = original_Tweet.split()
        del original_Tweet[0]
        original_Tweet = ' '.join(original_Tweet)
        line = re.sub('[^ a-zA-Z0-9]', '', line)
        line = re.sub(r' +', ' ', line)
        line = line.split(' ')
        line = [x.lower() for x in line]
        original_City = line[0]
        for ind_Word in line:
            if ind_Word in stop_words  or len(ind_Word) == 1:
                index_Word = line.index(ind_Word)
                del line[index_Word]
            else:
                continue
        line.pop(0)
        CityProbability = []
        for probdic in prob_DicList:
            city_Index = prob_DicList.index(probdic)
            prob_Values_Onecity = []
            for probword in line:
                if probword in probdic.keys():
                    prob_Val = probdic[probword]
                else:
                    prob_Val = 1/len(all_City_Words)
                prob_Values_Onecity.append(prob_Val)
            prob_Values_Onecity.append(city_NameProbabilities[city_Index])
            prob_Values_Onecity = np.prod(prob_Values_Onecity)
            CityProbability.append(prob_Values_Onecity)
        max_CityProbability = max(CityProbability)
        indx_max_CityProbability =CityProbability.index(max_CityProbability)
        predicted_City = city_Names[indx_max_CityProbability]
        current_Line.append(predicted_City)
        current_Line.append(original_City)
        current_Line.append(original_Tweet)
        output_Final.append(current_Line)
        current_Predictions.append(predicted_City)
        current_Predictions.append(original_City)
        all_Predictions.append(current_Predictions)

#Writing o/p file in the format "predicted city actual city actual tweet"
with open(output_File, 'w') as filehandle:
    for listitem in output_Final:
        listitem = ", ".join( repr(e) for e in listitem )
        filehandle.write('%s\n' % listitem)
correct_Predictions = []
for val in all_Predictions:
    if val[0] == val[1]:
        correct_Predictions.append(1)
    else:
        continue

#Code to print the highest 5 probability words for each city
i = 0
for dictionary in prob_DicList:
    if i<=11:
        sorted_by_value = sorted(dictionary.items(), key=lambda kv: kv[1])
        for sort_Word in sorted_by_value:
            if 'the' in sort_Word or len(sort_Word[0]) ==1:
                index_Sort_Word = sorted_by_value.index(sort_Word)
                del sorted_by_value[index_Sort_Word]
            else:
                continue
        sorted_by_value = sorted_by_value[-5:]
        high_Probabilty_Words = [sorted_by_value[4][0],sorted_by_value[3][0],sorted_by_value[2][0],sorted_by_value[1][0],sorted_by_value[0][0]]
        print("City:",city_Names[i],"|","High Probabilty words:",", ".join(repr(e) for e in high_Probabilty_Words))
        i = i+1
    else:
        break

#print("Accuracy is:",((sum(correct_Predictions) )/len(all_Predictions))*100,"%")



