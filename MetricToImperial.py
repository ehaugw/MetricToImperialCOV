
# # Converts a string containing metric value to imperial
def metricValueToImperial(metricString):
    imperialString = ""
    roundingDecimals = 2
    punctuations = ".,!?)"
    
    # Conversion rates from metric units to their corresponding imperial units
    unitConversionRates = {
        "g": [0.00220462, "lbs"],
        "m": [3.28084, "'"]
    }

    SIPrefixes = {
        "G": 1e09,
        "M": 1e06,
        "k": 1e03,
        "h": 1e01,
        "": 1,
        "d": 1e-01,
        "c": 1e-02,
        "m": 1e-03,
        "n": 1e-09
    }

    # Input without unit is returned unchanged
    if metricString[-1].isnumeric():
        return metricString    
    
    # Extracts any punctuation at the end of input
    punctuation = ""
    if metricString[-1] in punctuations:
        punctuation = metricString[-1]
        metricString = metricString[:-1]
    
    # Extracts metric unit from input
    metricUnit = metricString[-1]
    if not metricUnit in unitConversionRates:
        print("Unknown unit! Check spelling of: '" + metricString +  "', or update unitConversionRates.")
        return metricString
    
    # Extracts SI-prefix from input
    metricPrefix = ""
    if (metricString[-2].isalpha()) and (not metricString[-2] in SIPrefixes):
        print("Unknown prefix! Check spelling of: '" + metricString +  "', or update SIPrefixes.")
        return metricString
    elif metricString[-2] in SIPrefixes:
        metricPrefix = metricString[-2]

    # Extracts numeric value from input
    metricValue = float(metricString.strip(metricUnit+metricPrefix))

    # Converts to imperial and scales value according to prefix
    imperialValue = metricValue*SIPrefixes[metricPrefix]*unitConversionRates[metricUnit][0]      

    # Special formatting for feet and inches
    if metricUnit == "m":
        inches = int((imperialValue%1)*12)
        imperialString = str(int(imperialValue)) + unitConversionRates[metricUnit][1] + str(inches) + "''"
    else:
        imperialString = str(round(imperialValue, roundingDecimals)) + unitConversionRates[metricUnit][1]
    
    return imperialString+punctuation



# # Replaces all ocurrencies of metric values in a sentence with imperial
def metricSentenceToImperial(metricSentence):
    imperialWords = []

    # Split sentence into individual words
    metricWords = metricSentence.split()

    for word in metricWords:
        if word[0].isnumeric():
            # Each occurence of a numeric value is converted to imperial
            word = metricValueToImperial(word)
        imperialWords.append(word)
    
    # Reassemble into a complete sentence
    imperialSentence = " ".join(imperialWords)
    return imperialSentence



# # Unit test for metricValueToImperial()
# testString = "200cm"
# testString = "63.93kg"
# testString = "150mg"
# testString = "3.2km"
# print(metricValueToImperial(testString))



# # Verification test
verificationSentence = "The baby was 591mm tall and weighed 4kg at birth. The mother was 1.71m and 71.22kg before birth and 67.22kg after birth."
print(metricSentenceToImperial(verificationSentence))



# # Test for sentence with only words
# noNumbersTest = "The quick brown fox jumps over the lazy dog."
# print(metricSentenceToImperial(noNumbersTest))

# # Test for numbers without metric units
# nonMetricUnitsTest = "I am 22 years old, and I have lived in 3 different houses."
# print(metricSentenceToImperial(nonMetricUnitsTest))

# # Test for decimal numbers
# decimalNumbersTest = "The largest recorded blue whale was 29.9m long."
# print(metricSentenceToImperial(decimalNumbersTest))

