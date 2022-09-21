define e = Character('Эйлин', color="#c8ffc8")
define o = Character('Осёл', color="#808080")


define audio.maintheme = "audio/MainTheme.mp3"
define audio.starttheme = "audio/SSDDSSD.mp3"


init -2:
    image gf_bg = Movie(play="images/main_menu.mpg", size=(2920, 1080))

label main_menu:
    scene gf_bg
    jump main_menu_screen

label start:

    scene scene1
    play music audio.starttheme

    o "Обычным летним вечером Осёл как обычно играл в Доту"
    "Как вдруг он услышал звонок в дискорде... Это был ШРЕК"
