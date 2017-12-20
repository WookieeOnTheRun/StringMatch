import distance

def fnSplitString( strTransaction ) :

    dictTransSplit = strTransaction.split( "\t" )

    # print( "Pre strTrx: ", dictTransSplit )

    strTrx = str( dictTransSplit[ 2 ] )

    listTrxSplit = strTrx.split( "|" )

    return listTrxSplit


def fnCompareMerchant( strCleanMerchantVal, strDirtyMerchantVal, IsTesting ) :

    print( "Merchant to Check:", strDirtyMerchantVal )

    if IsTesting :

        dictLetters = { "S":2, "T":1, "A":1, "R":1, "B":1, "U":1, "C":1, "K":1 }

        for Letter in dictLetters :

            print( "Checking letter: ", str( Letter ).upper() )

            intLetterCount = strDirtyMerchantVal.count( str( Letter ).upper() )

            if intLetterCount == dictLetters[ str( Letter ).upper() ] :

                # print( "Merchant from File:", strDirtyMerchantVal )

                print( str( Letter ), "is a match." )

            elif intLetterCount >= dictLetters[ str( Letter ).upper() ] :

                # print( "Merchant from File:", strDirtyMerchantVal )

                print( str( Letter ), "is a possible match." )

    else :

        # print( "Prod code not ready yet to compare ", strCleanMerchantVal, " and ", strDirtyMerchantVal )

        intDiff = distance.hamming( strDirtyMerchantVal, strCleanMerchantVal )

        # fnCalculateDiff( strDirtyMerchantVal, intDiff, n )

        print( strDirtyMerchantVal, " and ", strCleanMerchantVal, " have a hamming distance of: ", str( intDiff ) )


# main

strFile = input( "Specify the file to be processed: " )

strMerchantList = input( "Specify Merchant List File: " )

boolTesting = input( "Are we testing? 1 for Yes, 0 for No: ")

with open( strFile, "r" ) as oFiMerchantFile :

    for fmLine in oFiMerchantFile :

        listTrans = fnSplitString( ( fmLine.strip( "\r\n" ) ) )

        # print( listTrans )

        # print( "Vendor: ", listTrans[ 0 ] )

        strOrigMerchantValue = str( listTrans[ 0 ] )

        # strip out any whitespaces to create compressed string
        strDirtyMerchant = strOrigMerchantValue.replace( " ", "" )

            # print( "Stripped Vendor: ", strCompMerchantValue )

        with open( strMerchantList, "r" ) as oCleanMerchantFile :

            for mlLine in oCleanMerchantFile :

                strRawMerchant = str( mlLine )

                strStripMerchant = strRawMerchant.strip("\r\n")

                strCleanMerchant = ( strStripMerchant.replace( " ", "" ).upper() )

                # commenting out hamming distance due to requirement that strings be same length

                if len( strDirtyMerchant ) == len( strCleanMerchant ) :

                    fnCompareMerchant( strCleanMerchant, strDirtyMerchant, boolTesting )

                # calculate jaccard distance for comparison

                d = distance.jaccard( strOrigMerchantValue, strStripMerchant )

                print( "Jaccard distance for ", strOrigMerchantValue, " and ", strStripMerchant, "is: ", str( d ) )

        oCleanMerchantFile.close()


# oFiMerchantFile.close()
