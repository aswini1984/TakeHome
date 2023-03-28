import requests
import json

# define API key and base url
api_key = "REMOVED"
base_url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"


# define a function to retrieve definition for a given word
def get_definition(wordCheck):
    url = base_url + wordCheck.lower() + "?key=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = json.loads(response.content.decode('utf-8'))
        if type(data) == list:
            for result in data:
                if "meta" in result:
                    # print(f"Definition for {result['meta']['id']}:")
                    if "hwi" in result:
                        # print(result['hwi']['prs'])
                        for sound in result['hwi']['prs']:
                            soundVal = (sound["mw"])
                    if "fl" in result:
                        typeVal = (result['fl'])
                    for definition in result["def"]:
                        for meaning in (definition["sseq"][0][0]):
                            # print(meaning)
                            if "dt" in meaning:
                                val = (meaning['dt'][0][1])
                            else:
                                if "sense" in meaning[1]:
                                    for meanVal in (meaning[1]):
                                        # print(meanVal)
                                        if "dt" in meanVal:
                                            val = (meanVal['dt'][0][1])

                    print("Definition for ", wordCheck)
                    print(soundVal, " (", typeVal, ") :", val.replace("{bc}", "").replace("{sx|use||}", ""))
                    # print(soundVal, " (", typeVal, ") :", val)
                    break
        else:
            print(f"No definition found for {wordCheck}")
    else:
        print(f"Error: {response.status_code}")


# get user input and call the function
word = input("Enter a word: ")
get_definition(word)
