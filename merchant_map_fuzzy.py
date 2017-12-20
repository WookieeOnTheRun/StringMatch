import distance

from fuzzywuzzy import fuzz

from fuzzywuzzy import process

def fnSplitTrxString( strTransaction ) :

    dictTransSplit = strTransaction.split( "\t" )

    strTrx = str( dictTransSplit[ 2 ] )

    listTrxSplit = strTrx.split( "|" )

    return str( listTrxSplit[ 0 ] );

def fnCleanString ( strStringToClean ) :

    # purpose of function: take a string, strip out spaces and set all
    #   characters in string to lower case
    #   Example: "Starbucks of London"
    #   After Function: "starbucksoflondon"

    strNoSpaces = strStringToClean.replace( " ", "" )

    strChangeCase = strNoSpaces.lower()

    return strChangeCase;

def GroupBy2andReturn ( strFirstString ) :

    # purpose of function: take a Merchant strings and create a
    #   list of a group of 2 characters from the string
    #   example: strFirstString = "starbucksoflondon"
    #   list would contain: [ "sta", "tar", "arb", "rbu", "buc", "uck", "cks", "kso", "sof",
    #                       "ofl", "flo", "lon", "ond", ndo", "don" ]
    # list would be returned

    intStrLen = len( strFirstString )

    # print( str( intStrLen ) )

    intStart = 0
    intEnd = 2

    listListOf2s = []

    while( intEnd <= intStrLen ) :

        strTmp = ""

        strTmp = strFirstString[ intStart:intEnd ]

        listListOf2s.append( strTmp )

        intStart += 1
        intEnd += 1

    return listListOf2s;

#############
# main body #
#############

# str1 = input( "Please type a Merchant Name: " )
# str2 = input( "Please type a Merchant Name to Compare: ")

strTrxFile = input( "Please specify file to be cleaned: " )
strCleanSrc = input( "Please specify matching source: " )

with open( strTrxFile, "r" ) as oTrxFile :

    for trx in oTrxFile :

        str1 = fnSplitTrxString( trx )

        strCleanStr1 = fnCleanString( str1 )

        print( "Preparing to clean: ", strCleanStr1 )

        with open( strCleanSrc, "r" ) as oCleanSrc :

            for cs in oCleanSrc :

                str2 = str( cs )

                strCleanStr2 = fnCleanString( str2 )

                # print( "Checking for match against: ", strCleanStr2 )

                # calculate Jaccard distance
                d = distance.jaccard( strCleanStr1, strCleanStr2 )

                # let's begin to filter obvious non-matches - jaccard distance >= .6

                if d < 0.7 :

                    print( "Jaccard Distance: " + str( d ) )

                    if d <= 0.5 :

                        # calculate fuzzy and partial fuzzy ratio(s)
                        intFz = fuzz.ratio( strCleanStr1, strCleanStr2 )
                        intPfz = fuzz.partial_ratio( strCleanStr1, strCleanStr2 )

                        # tokenize strings and calculate ratios
                        intSortRatio = fuzz.token_sort_ratio( strCleanStr1, strCleanStr2 )
                        intSetRatio = fuzz.token_set_ratio( strCleanStr1, strCleanStr2 )

                        print( "Fuzzy Ratio: ", str( intFz ) )
                        print( "Partial Fuzzy Ratio: ", str( intPfz ) )

                        print( "Sort Ratio: ", str( intSortRatio ) )
                        print( "Set Ratio: ", str( intSetRatio ) )

                        listFirstMerchantBreakdown = GroupBy2andReturn( strCleanStr1 )
                        listSecondMerchantBreakdown = GroupBy2andReturn( strCleanStr2 )

                        for dbl in listFirstMerchantBreakdown :

                            strDbl = str( dbl )

                            # print( str( dbl ), "exists at least once" ) if dbl in listSecondMerchantBreakdown else print( str( dbl ), "does not exist" )

                            # for dbl2 in listSecondMerchantBreakdown :

                            if listSecondMerchantBreakdown.count( strDbl ) >= 1 :

                                print( strDbl, " appears ", str( listSecondMerchantBreakdown.count( strDbl ) ), " time(s)." )

                    else :

                        print( strCleanStr1, " and ", strCleanStr2, " is a possible match - please review." )

                # else :

                    # print( "Jaccard distance between ", strCleanStr1, " and ", strCleanStr2, " is greater than 60%" )

        oCleanSrc.close();

# print( listFirstMerchantBreakdown )
# print( listSecondMerchantBreakdown )


