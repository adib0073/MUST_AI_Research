import wikipedia
import sys
import io
import requests


def get_summary(search_term="Null"):
        
        '''
        #_summary = wikipedia.summary(search_term)
        _summary="Hi"
        paragraph=_summary.splitlines()
        data=paragraph[0]
        '''
        session = requests.Session()
        session.trust_env = False
        url='https://en.wikipedia.org/w/api.php?action=opensearch&search='+search_term+'&limit=1&namespace=0&format=json'
        _summary=session.get(url,headers={'Connection':'close'})
        data=_summary.json()[2][0]
        print(data)
        file = io.open("summary.txt", "w",encoding="utf-8") 
        file.write(data);
        file.close() 
'''   
if __name__ == "__main__":
    get_summary(sys.argv[1]) 
 
'''