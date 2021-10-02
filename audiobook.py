import os

import pyttsx3

engine = pyttsx3.init()

audiobook_name = input('> Enter Audio Book Name: ')

print()

content = input('> Content: ')

print()

desktop_content = os.listdir('C:/Users/Ayodeji/Desktop')

if 'AudioBook' in desktop_content:

    male_female_voice = input('> Do you want a male or female voice(m/f): ')

    if male_female_voice == 'm':

        engine.setProperty('rate', 125)

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[0].id)

        os.chdir('C:/Users/Ayodeji/Desktop')

        save_file = f'C:/Users/Ayodeji/Desktop/AudioBook/{audiobook_name}.mp3'

        engine.save_to_file(content, save_file)

        engine.runAndWait()

        engine.stop()

    elif male_female_voice == 'f':

        engine.setProperty('rate', 125)

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[1].id)

        os.chdir('C:/Users/Ayodeji/Desktop')

        save_file = f'C:/Users/Ayodeji/Desktop/AudioBook/{audiobook_name}.mp3'

        engine.save_to_file(content, save_file)

        engine.runAndWait()

        engine.stop()

elif 'AudioBook' not in desktop_content:

    os.chdir('C:/Users/Ayodeji/Desktop')

    os.mkdir('AudioBook')

    male_female_voice = input('> Do you want a male or female voice(m/f): ')

    if male_female_voice == 'm':

        engine.setProperty('rate', 125)

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[0].id)

        os.chdir('C:/Users/Ayodeji/Desktop')

        save_file = f'C:/Users/Ayodeji/Desktop/AudioBook/{audiobook_name}.mp3'

        engine.save_to_file(content, save_file)

        engine.runAndWait()

        engine.stop()

    elif male_female_voice == 'f':

        engine.setProperty('rate', 125)

        voices = engine.getProperty('voices')

        engine.setProperty('voice', voices[1].id)

        os.chdir('C:/Users/Ayodeji/Desktop')

        save_file = f'C:/Users/Ayodeji/Desktop/AudioBook/{audiobook_name}.mp3'

        engine.save_to_file(content, save_file)

        engine.runAndWait()

        engine.stop()

