'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 20, 2023.
'''

import math

def norm(vec):
    '''Return the norm of a vector stored as a dictionary, as 
    described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    ''' dot product words in common and divide by norm of input vectors '''
    # find dictionary elements that are in common
    commonList = []
    for key in vec1.keys():
        if key in vec2:
            commonList.append(key)
    print(commonList)
    prod = 0
    for i in commonList: # take dot product
        prod += vec1[i]*vec2[i]

    return prod / (norm(vec1)*norm(vec2))

def build_semantic_descriptors(sentences):
    # get list of keywords
    keywords = generate_unique_words(sentences)
    outputDict = {}
    # for every keyword in sentences[i], count the occurance of each word
    for s in range(len(sentences)): # iterate across sentences
        for word in keywords:
            # count occurances of word in current sentence
            if word in sentences[s]: # check if word is in current sentence
                tmpDict = {}
                # check if word has an existing hashmap entry
                if word in outputDict:
                    tmpDict = outputDict[word]
                # update tmpDict
                for bit in sentences[s]:
                    if bit in tmpDict and word != bit:
                        # if bit != word then add thingy
                        tmpDict[bit] += 1
                    else:
                        if word != bit:
                            tmpDict[bit] = 1
                # once your at the end of the word, update tmpDict in outputDict
                outputDict[word] = tmpDict

    # for debugging, remove any 0 elements from the dictionary

    return outputDict

def build_semantic_descriptors_from_files(filenames):
    pass

def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    pass


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    pass

''' My helper functions '''
def generate_unique_words(sentences):
    # hopefully avoid O(n) sweep by not checking if elem in list
    # instead add to a dictionary
    uniqueWords = {}
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            uniqueWords.update({sentences[i][j]: 0})

    uniqueWordsList = list(uniqueWords.keys())
    
    return uniqueWordsList

def psa_generate_unique_words(sentences):
    # count the occurances of each word in every sentence
    # psa it to get word count for every sentence you need
    # put everything thing into massive list... uh I don't want to debug this. 
    pass

if __name__=="__main__":
    vec1 = {"a": 1, "b": 2, "c": 3}
    vec2 = {"b": 4, "c": 5, "d": 6}
    sentences =  [["i", "am", "a", "sick", "man"], ["i", "am", "a", "spiteful", "man"], ["i", "am", "an", "unattractive", "man"], ["i", "believe", "my", "liver", "is", "diseased"], ["however", "i", "know", "nothing", "at", "all", "about", "my", "disease", "and", "do", "not", "know", "for", "certain", "what", "ails", "me"]]

    #build_semantic_descriptors(sentences)
    tmp = build_semantic_descriptors(sentences)

    for key, value in tmp.items():
        print(key, "\t", value)
        print("\n")
