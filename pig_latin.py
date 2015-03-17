# http://www.dreamincode.net/forums/topic/78802-martyr2s-mega-project-ideas-list/

'''
The following rules is:

For words that begin with consonant sounds,
the initial consonant or consonant cluster is moved to the end of the word,
and "ay" (some people just add "a") is added, as in the following examples:

"pig" → "igpay"
"banana" → "ananabay"
"trash" → "rashtay"
"happy" → "appyhay"
"duck" → "uckday"
"glove" → "oveglay" # not sure how this one would work in general

For words that begin with vowel sounds or silent letter,
one just adds "way" (or "wa") to the end. Examples are:

"egg" → "eggway"
"inbox" → "inboxway"
"eight" → "eightway"

'''

def pig_latin(str):

    #vowel first
    if ('a' == str[0]
        or 'e' == str[0]
        or 'i' == str[0]
        or 'o' == str[0]
        or 'u' == str[0]):

        str = str + 'way'
        print(str)

    #consonant first    
    else:
        
        str = str[1:] + str[0] + 'ay'
        print(str)

#vowel first
pig_latin('pig')
pig_latin('banana')
pig_latin('trash')
pig_latin('happy')
pig_latin('duck')

#consonant first
pig_latin('egg')
pig_latin('inbox')
pig_latin('eight')



