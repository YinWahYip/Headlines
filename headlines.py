from bs4 import BeautifulSoup
import requests, schedule, time

def run_script():
    def bbc():
        print('*************************************BBC****************************************')


        website = requests.get("https://www.bbc.com").text #website into source html (can print)
        soup = BeautifulSoup(website, 'lxml') #parse all the text from website using lxml the parser

        article = soup.find('ul', class_='media-list') #find a tag called ul with a class of 'media-list'

        title = article.find('h3', class_='media__title').text 
        '''
        sing from the previous variable, article, we can search within article for a tag called
        <h3> and contains a class called 'media__title'. We can convert whatwever we find into a text
        '''

        summary = article.find('p', class_="media__summary").text
        #similar to Article, we're looking for the class 'media__summary' within the tag <p>


        link = soup.find('a', class_='block-link__overlay-link')
        print(link.get('href'))
        # link = article.find('a', class_='block-link__overlay-link').text
        print('1. ', title.strip()) #.strip() is necessary to removing blank space before and after the text.
        print('\t*' + summary.strip())
        print('\t\t www.bbc.com'+link.get('href'))

        print()



        #Remaining articles::

        for i in range(2,6): #including 0-3 elements accessed
            find_title = article.find('li', class_='media-list__item media-list__item--'+str(i)) 
            #concat the class called media-list(...) with str to go through 5 different boxes

            title__ = find_title.find('h3', class_= 'media__title').text 
            print(str(i)+'. ' + title__.strip()) # printing titles
            link = find_title.find('a', class_='media__link')

            print('\t' + link.get('href'))
            # print('\t' + link_.get('href') )
            print('')

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def reuters():
        print('*************************************REUTERS****************************************')

        website = requests.get('https://www.reuters.com/').text
        soup = BeautifulSoup(website, 'lxml') #parse all the text from website using lxml the parser

        title = soup.find('a', class_='text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_4__14ZqK heading__base__2T28j heading_3_bold_static media-story-card__heading__eqhp9').text
        summary = soup.find('p', class_='text__text__1FZLe text__dark-grey__3Ml43 text__regular__2N1Xr text__extra_small__1Mw6v body__base__22dCE body__extra_small_body__3QTYe media-story-card__description__2icjO').text
        date_time = soup.find('time', class_ = 'text__text__1FZLe text__inherit-color__3208F text__regular__2N1Xr text__extra_small__1Mw6v label__label__f9Hew label__small__274ei media-story-card__time__2i9EK').text
        print('1. ' + title)
        print('\t\t', date_time)
        print('\t *' + summary)
        print()
        i=2
        print('***WORLD NEWS ***')
        for world_news in soup.find_all('a', {"class":"text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_6__1qUJ5 heading__base__2T28j heading__heading_6__RtD9P text-story-card__title__3R37x"}):
            tag = world_news
            href = tag['href']
            print(i , '.',  world_news.text)
            print('https://www.reuters.com'+ href)
            print()
            i+=1    
            
        print('\n')

    bbc()
    reuters()
    pass

schedule.every(4).hours.do(run_script)

while True:
    schedule.run_pending()
    time.sleep(1)
