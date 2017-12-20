# used distance library ( https://pypi.python.org/pypi/Distance )

import distance

def fnSplitString( strTransaction ) :

    dictTransSplit = strTransaction.split( "\t" )

    strTrx = str( dictTransSplit[ 2 ] )

    listTrxSplit = strTrx.split( "|" )

    return listTrxSplit

# main

strFile = input( "Specify the file to be processed: " )

strMerchantList = input( "Specify Merchant List File: " )

fltPct = input( "What percentage difference or less are we looking for - enter value less than 1: " )

# oCleanMerchantFile = open( strMerchantList, "r" )

with open( strFile, "r" ) as oFiMerchantFile :

    for fmLine in oFiMerchantFile :

        listTrans = fnSplitString( fmLine )

        # print( listTrans )

        # print( "Vendor: ", listTrans[ 0 ] )

        strOrigMerchantValue = str( listTrans[ 0 ] )

        with open( strMerchantList, "r" ) as oCleanMerchantFile :

            for mlLine in oCleanMerchantFile :

                strRawMerchant = str( mlLine )

                strStripMerchant = strRawMerchant.strip("\r\n")

                d = distance.jaccard( strOrigMerchantValue, strStripMerchant )

                if d <= fltPct :

                    print( "Jaccard distance for " + strOrigMerchantValue + " and " + strStripMerchant + " is: " + str( d ) )

        oCleanMerchantFile.close()

# oFiMerchantFile.close()
