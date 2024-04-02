import pyttsx3
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import openai
#from config import apikey
import datetime
import pywhatkit
import random
import numpy as np
from win10toast import ToastNotifier
import imaplib
import pyjokes
import email
import pygame
import random
import requests
from email.header import decode_header
from simplegmail import Gmail
from simplegmail.query import construct_query

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from googlesearch import search
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
from youtubesearchpython import VideosSearch

current_time = datetime.datetime.now()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def snake():
    # importing libraries
    import pygame
    import time
    import random

    snake_speed = 15

    # Window size
    window_x = 720
    window_y = 480

    # defining colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    red = pygame.Color(255, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)

    # Initialising pygame
    pygame.init()

    # Initialise game window
    pygame.display.set_caption('GeeksforGeeks Snakes')
    game_window = pygame.display.set_mode((window_x, window_y))

    # FPS (frames per second) controller
    fps = pygame.time.Clock()

    # defining snake default position
    snake_position = [100, 50]

    # defining first 4 blocks of snake body
    snake_body = [[100, 50],
                  [90, 50],
                  [80, 50],
                  [70, 50]
                  ]
    # fruit position
    fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                      random.randrange(1, (window_y // 10)) * 10]

    fruit_spawn = True

    # setting default snake direction towards
    # right
    direction = 'RIGHT'
    change_to = direction

    # initial score
    score = 0

    # displaying Score function
    def show_score(choice, color, font, size):

        # creating font object score_font
        score_font = pygame.font.SysFont(font, size)

        # create the display surface object
        # score_surface
        score_surface = score_font.render('Score : ' + str(score), True, color)

        # create a rectangular object for the text
        # surface object
        score_rect = score_surface.get_rect()

        # displaying text
        game_window.blit(score_surface, score_rect)

    # game over function
    def game_over():

        # creating font object my_font
        my_font = pygame.font.SysFont('times new roman', 50)

        # creating a text surface on which text
        # will be drawn
        game_over_surface = my_font.render(
            'Your Score is : ' + str(score), True, red)

        # create a rectangular object for the text
        # surface object
        game_over_rect = game_over_surface.get_rect()

        # setting position of the text
        game_over_rect.midtop = (window_x / 2, window_y / 4)

        # blit will draw the text on screen
        game_window.blit(game_over_surface, game_over_rect)
        pygame.display.flip()

        # after 2 seconds we will quit the program
        time.sleep(2)

        # deactivating pygame library
        pygame.quit()

        # quit the program


    # Main Function
    while True:

        # handling key events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'

        # If two keys pressed simultaneously
        # we don't want snake to move into two
        # directions simultaneously
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        # Moving the snake
        if direction == 'UP':
            snake_position[1] -= 10
        if direction == 'DOWN':
            snake_position[1] += 10
        if direction == 'LEFT':
            snake_position[0] -= 10
        if direction == 'RIGHT':
            snake_position[0] += 10

        # Snake body growing mechanism
        # if fruits and snakes collide then scores
        # will be incremented by 10
        snake_body.insert(0, list(snake_position))
        if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
            score += 10
            fruit_spawn = False
        else:
            snake_body.pop()

        if not fruit_spawn:
            fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                              random.randrange(1, (window_y // 10)) * 10]

        fruit_spawn = True
        game_window.fill(black)

        for pos in snake_body:
            pygame.draw.rect(game_window, green,
                             pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(game_window, white, pygame.Rect(
            fruit_position[0], fruit_position[1], 10, 10))

        # Game Over conditions
        if snake_position[0] < 0 or snake_position[0] > window_x - 10:
            game_over()
        if snake_position[1] < 0 or snake_position[1] > window_y - 10:
            game_over()

        # Touching the snake body
        for block in snake_body[1:]:
            if snake_position[0] == block[0] and snake_position[1] == block[1]:
                game_over()

        # displaying score continuously
        show_score(1, white, 'times new roman', 20)

        # Refresh game screen
        pygame.display.update()

        # Frame Per Second /Refresh Rate
        fps.tick(snake_speed)


def send_email():
    import smtplib
    from email.mime.text import MIMEText

    # Set up your Gmail credentials
    sender_email = 'famousiitian999@gmail.com'
    sender_password = 'nqer teqw zyrt zabe'

    speak("Please write the recipient's email address.")
    recipient_email = input("Enter Email Address: ")

    speak("Please speak the subject of the email.")
    subject = takevoice()

    speak("Please speak the body of the email.")
    body = takevoice()


    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

    speak('Email sent successfully!')





def search_youtube(query, max_results=5):
    videos_search = VideosSearch(query, limit=max_results)
    results = videos_search.result()['result']
    return results

def get_most_viewed_url(query):
    search_results = search_youtube(query)
    if search_results:
        # Sort search results by view count in descending order
        sorted_results = sorted(search_results, key=lambda x: int(x['viewCount']['text'].replace(' views', '').replace(',', '')), reverse=True)
        # Get URL of the most viewed video
        most_viewed_url = sorted_results[0]['link']
        return most_viewed_url
    else:
        return None



def google_search(query):
    search_results = list(search(query,advanced=True))
    url=search_results[0].url
    webbrowser.open(url)



def mind_reading():
    speak("Welcome to the Mind Reading game!")
    speak("Think of a number between 1 and 20 and keep it a secret.")
    speak("speak ok when you're ready to begin...")
    q = input("Write Ok")

    if "ok" in q.lower():
        speak("Now Add 1 to your number.")
        speak("Write ok when you're ready to begin...")
        l2 = input("Write Ok")

        if "ok" in l2.lower():
            speak("ok Now Double the new number.")
            speak("Write ok when you're ready to begin...")
            l3 = input("Write Ok")

            if "ok" in l3.lower():
                speak("ok Now Add 4 more to the doubled number.")
                speak("Write ok when you're ready to begin...")
                l4 = input("Write Ok")

                if "ok" in l4.lower():
                    speak("ok Now  Divide the result by 2")
                    speak("Write ok when you're ready to begin...")
                    l5 = input("Write Ok")

                    if "ok" in l5.lower():
                        speak("ok Now Subtract the original number from the result.")
                        speak("Write ok when you're ready to begin...")
                        l6 = input("Write Ok")

                        if "ok" in l6.lower():
                            speak("Wait I will now predict your final number...")
                            speak("ok I think Your final number is 3")



def read_email_notifications():


    # use your email id here
    username = "famousiitian999@gmail.com"

    # use your App Password you
    # generated above here.
    password = "nqer teqw zyrt zabe"

    # create a imap object
    imap = imaplib.IMAP4_SSL("imap.gmail.com")

    # login
    result = imap.login(username, password)

    # Use "[Gmail]/Sent Mails" for fetching
    # mails from Sent Mails.
    imap.select('"[Gmail]/All Mail"',
                readonly=True)

    response, messages = imap.search(None,
                                     'UnSeen')
    messages = messages[0].split()

    # take it from last
    latest = int(messages[-1])

    # take it from start
    oldest = int(messages[0])

    for i in range(latest, latest - 20, -1):
        # fetch
        res, msg = imap.fetch(str(i), "(RFC822)")

        for response in msg:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                # print required information
                speak(msg["Date"])
                speak(msg["From"])
                speak(msg["Subject"])



        for part in msg.walk():
            if part.get_content_type() == "text / plain":
                # get text or plain data
                body = part.get_payload(decode=True)
                print(f'Body: {body.decode("UTF-8")}', )


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Hello, Good morning")
    elif 12 <= hour < 18:
        speak("Hello, Good afternoon")
    else:
        speak("Hello, Good evening")
    speak("I am your AI assistant. How can I help you today?")


def takevoice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        r.energy_threshold = 100
        try:
            print("Listening...")
            r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            audio = r.listen(source, timeout=5)  # Listen for up to 5 seconds
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            if "jarvis" in query.lower():
                print(f"User said: {query}")
                return query
            else:
                speak("Wake word not detected.")
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except TimeoutError:
            print("Timeout occurred. Please try again.")
        except Exception as e:
            print(f"Some error occurred: {e}")

def send_whatapp_message(number , message):
    pywhatkit.sendwhatmsg_instantly(number, message, 10)
    speak("Message send sucessfully")






if __name__ == '__main__':
    wishme()

    while True:
        query = takevoice()
        if query is not None:  # Check if query is not None
            if "youtube" in query.lower():
                pywhatkit.playonyt(query)

            elif "Email Notifications" in query.lower():
                read_email_notifications()

            elif "whatsapp" in query.lower():

                speak("Please tell the number .")
                number = input("Enter a number")
                speak("Please tell the message.")
                message = None
                while message == None:
                    message = takevoice()

                send_whatapp_message(number, message)


            elif 'play' in query.lower():
                song = query.replace('play', '')
                speak('playing ' + song)
                pywhatkit.playonyt(song)
            elif "game" in query.lower():
                speak("Hey you can play many games with me ")
                speak("Here is list of game Snake , mindgame")
                speak("Choose which game you want to play")
                s = None
                while s == None:
                    s = takevoice()
                if "snake" in s.lower():
                    snake()
                elif "mindgame" in s.lower():
                    mind_reading()

            elif " send email" in query.lower():
                send_email()

            elif "wikipedia" in query.lower():
                speak("Ok! Please wait...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                speak("Here is a summary.")
                speak(results)

            elif 'open google' in query.lower():
                webbrowser.open("https://www.google.com")
            elif 'open gpt' in query.lower():
                webbrowser.open("https://openai.com/blog/chatgpt")

            elif 'open spotify' in query.lower():
                spotify = 'C:\\Users\\rohit\\AppData\\Local\\Microsoft\\WindowsApps\\Spotify.exe'
                os.startfile(spotify)

            elif 'open email' in query.lower():
                webbrowser.open('https://mail.google.com/mail/u/0/?pli=1#inbox/FMfcgzGtwVxhnBRBzZJVHDChPFFnCtDt')

            elif 'notebook' in query.lower():
                notebook = '"C:\\Users\\rohit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook (anaconda3) (1).lnk"'
                os.startfile(notebook)

            elif 'pycharm' in query.lower():
                pycharm = '"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2022.1.lnk"'
                os.startfile(pycharm)
            elif 'code' in query.lower():
                code = "C:\\Users\\rohit\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
                os.startfile(code)

            elif 'edge' in query.lower():
                edge = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Edge.lnk"
                os.startfile(edge)

            elif 'word' in query.lower():
                word = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
                os.startfile(word)

            elif 'PowerPoint' in query.lower():
                pp = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
                os.startfile(pp)

            elif 'Notepad' in query.lower():
                np = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Notepad++.lnk"
                os.startfile(np)

            elif 'joke' in query.lower():
                speak(pyjokes.get_joke())

            elif 'amazon' in query.lower():
                webbrowser.open(
                    "https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwjzzMed_L2AAxWRbA8CHaCUDrMYABAAGgJ0Yg&ae=2&ohost=www.google.com&cid=CAESa-D24DxxRlP5ILUj8u2RxzyT8xJjn6DkTq178uGaG7fXA-dMaMo7ghdCWpMbL4Jre3YFPIo4oxZQ3JoazGdHqS1SIicgC0204-wFHKRXeNMFyhzYiWfxqzbft7qoAzKDAW2d8T3yiHu5oixx&sig=AOD64_2gQwl3Hlc3VI2RHmGZvAuaYDkyiw&q&adurl&ved=2ahUKEwiiisCd_L2AAxWvp1YBHV5vBU4Q0Qx6BAgGEAE")

            elif 'exit' in query or 'stop' in query.lower():
                speak("Goodbye Rohit, have a nice day.")
                break

            else:
                google_search(query)





















