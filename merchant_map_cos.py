# example: https://stackoverflow.com/questions/15173225/how-to-calculate-cosine-similarity-given-2-sentence-strings-python

import math

from collections import Counter

def fnSplitString( strTransaction ) :

    dictTransSplit = strTransaction.split( "\t" )

    strTrx = str( dictTransSplit[ 2 ] )

    listTrxSplit = strTrx.split( "|" )

    return listTrxSplit;

def fnRemoveSpaces( strMerchant ) :

    strNOSMerchant = strMerchant.replace( " ", "" )

    return strNOSMerchant;

def fnLetterCount( strMerchant ) :

    dictLetters = Counter( ( strMerchant.upper()) )

    return dictLetters;

def fnGetCosine( vec1, vec2 ) :

    intersection = set( vec1.keys() ) & set( vec2.keys() )

    numerator = sum( [ vec1[ x ]**2 for x in intersection ] )

    sum1 = sum( [ vec1[ x ]** 2 for x in vec1.keys() ] )
    sum2 = sum( [ vec2[ x ]** 2 for x in vec2.keys() ] )

    denominator = math.sqrt( sum1 ) * math.sqrt( sum2 )

    if not denominator :

        return 0.0

    else :

        return float( numerator ) / denominator

# main

strFile = input( "Specify the file to be processed: " )

strMerchantList = input( "Specify Merchant List File: " )

# oCleanMerchantFile = open( strMerchantList, "r" )

with open( strFile, "r" ) as oFiMerchantFile :

    for fmLine in oFiMerchantFile :

        listTrans = fnSplitString( fmLine )

        # print( listTrans )

        # print( "Vendor: ", listTrans[ 0 ] )

        strOrigMerchantValue = str( listTrans[ 0 ] )

        strRawMerchant = fnRemoveSpaces( strOrigMerchantValue )

        with open( strMerchantList, "r" ) as oCleanMerchantFile :

            for mlLine in oCleanMerchantFile :

                strTmpMerchant = str( mlLine )

                strStripMerchant = strTmpMerchant.strip("\r\n")

                strCleanMerchant = fnRemoveSpaces( strTmpMerchant )

                print( "Raw Merchant: " + ( strRawMerchant.upper() ) )

                dictRawMerchantChars = fnLetterCount( strRawMerchant )

                print( dictRawMerchantChars )

                print( "Clean Merchant: " + ( strCleanMerchant.upper() ) )

                dictCleanMerchantChars = fnLetterCount( strCleanMerchant )

                print( dictCleanMerchantChars )

                intCos = fnGetCosine( dictRawMerchantChars, dictCleanMerchantChars )

                print( "Cosine: ", str( intCos ) )

        oCleanMerchantFile.close()

# oFiMerchantFile.close()
