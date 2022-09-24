
define author = Character('Автор', color="#c8ffc8")
define serega = Character('Сергей', color="#808080")


define audio.maintheme = "audio/MainTheme.mp3"
define audio.starttheme = "audio/SSDDSSD.mp3"

print "privet"


init -2:
    image gf_bg = Movie(play="images/main_menu.mpg", size=(2920, 1080))

label main_menu:
    scene gf_bg
    jump main_menu_screen

label start:

    scene scene1
    stop music fadeout 1

    author "Сергей закончил школу. Прошли очередные 11 лет его жизни.Углубляясь в прошедшее, его настигает меланхолия."
    serega "Получил среднее образование, но, зачем оно мне, что я узнал за это время? Много ли я вспомню из школьной программы за последние года?"
    serega "Я так и не понял, что мне интересно, кем я хочу быть. Кажется все, кроме меня уже добились успеха хоть в чем-то."
    serega "Васька получил золотой значок ГТО, Иван накопил на свою первую машину, а Гриша так вообще устроился фронтендом сразу после школы, куда мне до них"
