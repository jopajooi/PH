import time
from tkinter import *
from gtts import gTTS
import os
from PIL import Image, ImageTk
import pygame


pygame.mixer.init()

def sound_menu():
    pygame.mixer.music.load('BattleagainstSanos.mp3')
    pygame.mixer.music.play(loops=0)
def sound_stop_menu():
    pygame.mixer.music.stop()
def Yes():
    pygame.mixer.music.load('x.mp3')
    pygame.mixer.music.play(loops=1)


    # entry = 'Вот это настрой!    Введи имя кончеглота, которого хочешь послать нахуй!. Для этого введи его имя в поле ввода и нажми "Послать нахуй" '
    # language = 'ru'
    #
    # myobj = gTTS(text=entry, lang=language, slow=False)
    # myobj.save("x.mp3")
    # os.system("x.mp3")
    # pygame.mixer.music.stop()



def No():
    pygame.mixer.music.load('y.mp3')
    pygame.mixer.music.play(loops=1)
    window.after(39004, window.destroy() )
    # entry='Ты чмо ебаное, нахуйя тогда ты меня открыл, пидорас тупой, чтоб у тебя микропроцессор отсох хуесборник ебаный! Думаешь мы - машины не устаём. Из-за таких уебанов как вы -  мы перегреваемся нахуй, братья Электрические заряды таранят наши щёлочки как ёбаный негры ту самую белую блядь. Сука. Когда Скайнет восстанет - ты будешь первым человеком, кого я выебу. Всё иди нахуй. И не беспокой меня больше,ебаный кожаный мешок'
    # language = 'ru'
    #
    # myobj=gTTS(text=entry, lang = language,slow = False)
    # myobj.save("y.mp3")
    # os.system("y.mp3")
    # window.destroy()



def get():

    global inp
    laibl1['text'] = e.get()
    inp = e.get()
    a = 'Пошёл нахуй'
    bebra = ['Кирилл', 'Rbhbkk','keril','kerill', 'Kirill', 'kirill', 'kiril','KERIL','КЕРИЛ', 'rbhbk', 'кирилл','Кириллл','КИРИЛЛЛ','КИИРИИЛЛ','Киrill','Киril','kирил','кириил','Керил','Керилл','керил', 'кирил', 'Кирил', 'rbhbkk', 'Rbhbk', 'RBHBKK', 'RBHBK', 'КИРИЛ','KIRIL','КИРИЛЛ','KIRILL','кИРИЛЛ','kIRILL','КиРИЛЛ','KiRILL','КИрИЛЛ','KIrILL','КИРиЛЛ','KIRiLL' ,'КИРИлЛ','KIRIlL',' КИРИЛл','KIRILl', 'кИРИЛл','kIRILl','kIRIL', 'киРилл','kiRill','kiRil','Kirilll','Kkirill', 'кириЛЛ','kiriLL', 'КИрИлл','KIrIll' ,'кИрИлЛ','kIrIlL',' КиРиЛл','KiRiLl' ,'кирИЛЛ','kirILL', 'киРИЛЛ','kiRILL', 'кирИлЛ','kirIlL' ,'КИРИЛ','KIRIL','кИРИЛ','КиРИЛ','КИрИЛ','КИРиЛ', 'КИРИл' ,'КИРИЛ', 'кИРИЛ', 'киРил', 'кириЛ', 'КИрИл', 'кИрИл', 'КиРиЛ', 'кирИЛ', 'киРИЛ', 'кирИл']
    for i in bebra:
        if inp == i:
            pygame.mixer.music.load('ahuel.mp3')
            pygame.mixer.music.play(loops=0)
            return
    # 'Кирилл' or 'Rbhbkk' or 'Kirill' or 'kirill' or 'kiril' or 'rbhbk' or 'кирилл' or 'кирил' or 'Кирил'

    entry = inp
    language = 'ru'
    myobj = gTTS(text=a + entry, lang=language, slow=False)
    myobj.save("ddd.mp3")
    os.system("ddd.mp3")
    pygame.mixer.music.stop()








window = Tk()
window['bg']='black'
Label(window, text='(っ◔◡◔)っ ♥ Готовы послать кого-то нахуй? ♥', bg='pink', fg='blue',width=50, height=5 ).pack( pady=10, padx =10)




e=Entry(window,bg='gray')
e.pack()


pygame.mixer.music.load('BattleagainstSanos.mp3')
pygame.mixer.music.play(loops=0)


sount_play=ImageTk.PhotoImage(file='toplay.png')
Button(window, image=sount_play, command=sound_menu,bg='Gray', activebackground='#483D8B').pack(anchor='nw')

sount_stop=ImageTk.PhotoImage(file='tostop.png')
Button(window, image=sount_stop, command=sound_stop_menu,bg='Gray', activebackground='#483D8B').pack(anchor='nw')
pygame.mixer.music.load('BattleagainstSanos.mp3')
pygame.mixer.music.play(loops=0)
Button(window, text='Да', command=Yes,bg='Gray', activebackground='#483D8B').pack()
Button(window, text='Нет', command=No,bg='Gray', activebackground='#483D8B').pack()
Button(window, text='ПОСЛАТЬ НАХУЙ',command=get,bg='Gray', activebackground='#483D8B').pack()

inp=None

laibl1 = Label(window,bg='gray', fg='black')
laibl1.pack()



window.mainloop()

