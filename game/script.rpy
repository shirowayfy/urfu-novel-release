
define friend_character = Character('Огр', color="#c8ffc8")
define main_character = Character('Сергей', color="#808080")
define main_and_friend_character = Character('Сергей и Огр', color="#808080")
define tips_character = Character('Гига-Пряня', color="#808080")


define audio.maintheme = vars.audio.soundtrack.main_theme
# define audio.starttheme = "audio/SSDDSSD.mp3"
define audio.call_sound = "audio/sounds/call_sound.mp3"
define audio.vibro_sound = "audio/sounds/vibro_sound.mp3"
define audio.donkeysound = "audio/DonkeySound.mp3"
# define audio.pryanyasteps = "audio/PryanyaSteps.mp3"


init -2:
    # image gf_bg = Movie(play="scene.webm", size=(1920, 1080))
    image main_menu: 
        "images/menu/guts.jpg"
        10
        "images/menu/football_1.jpg"
        10
        "images/menu/girl.jpg"
        10
        repeat

    image start_scene = "images/scenes/intro.jpg"
    image scene_with_notification = "images/scenes/intro_with_notification.jpg"


label main_menu:
    scene main_menu
    jump main_menu_screen

label start:
    scene start_scene
    stop music fadeout 1

    "На часах почти полночь. Сквозь приоткрытое окно веет прохладный ветерок. Парень, только переступивший порог взрослой жизни, вяло качается на стуле."

    main_character "Кто я? Зачем я нужен этому миру? Получил среднее образование, что дальше? Работать? Но кому я нужен, ни опыта, ни представления о том, кем хочу быть."
    main_character "Я так и не разобрался, в какую сторону двигаться, какую профессию осваивать. Кажется все, кроме меня, уже добились успеха хоть в чем-то."
    main_character "Гоша получил золотой значок ГТО, теперь метит в мастера спорта. Савелий накопил на свою первую машину, а Саня так вообще устроился в Яндекс, чем же я хуже?"
    main_character "Ну не может же быть, что я единственный, кто не понимает чем заниматься. Почему я не могу измениться, перестать тратить время впустую, начать развиваться?"
    main_character "Вот хотя бы, начать с интересов: люблю играть в игры, смотреть аниме и читать книги. Но у меня нет желания создавать что-либо из этого. Да я и не пробовал…"

    play sound audio.vibro_sound

    "Неожиданный рингтон с телефона прервал монолог Сергея…"

    scene scene_with_notification

    'Вы приняты на специальность "Прикладная информатика"'

    "Сергей с недоверием посмотрел на телефон,протирая глаза. Его в самом деле приняли в [vars.university_name]."

    play sound audio.donkeysound

    scene scene_with_notification

    main_character "УРА!!!"

    main_character "Получилось! Я не думал, что я все-таки пройду. Вот так повезло!"

    main_character "Это что же это, придется съехать от родителей? А как получить общагу? Блин, там же наверняка будут тараканы. А соседи? Феи и огры? Не люблю их. У меня друг огр, но вы не понимаете, это другое. А вещи? Как их перевезти?"

    main_character "Голова болит. Минуту назад я депрессовал, а сейчас думаю о будущем, о новой жизни!"

    stop music

    play music audio.call_sound

    main_character "На аппарате?"

    stop music

    show shrek at center

    friend_character "Ало, ало, меня слышно?"

    main_character "Нет, день добрый."

    friend_character "Здарова мужик, ты это, поступил?"

    main_character "Поступил? Ты тоже подавал в [vars.university_name]?"

    friend_character "Да, ты забыл? Я же говорил об этом. Совсем там в облаках заплутал, даже этого не помнишь."

    main_character "Вот так сюрприз!"

    friend_character "Похоже будем соседями по общаге."

    main_character "Ага, но не надо тащить с собой мешок лука, да и есть его в нашей комнате не стоит."

    friend_character "Ну чего ты… Ладно, договорились!"

    friend_character "Не хочешь прогуляться, хоть глянем куда поступили?"

    main_character "Давай, я и сам хотел предложить!"


    ############ Здесь должна подключаться сцена С ГУКом


    main_and_friend_character "Огоооо, монументально"

    main_character "Не думал, что [vars.university_name] выглядит так круто. Не зря говорили, что Екб красив. У них даже свой Гарвард есть."

    friend_character "Ну да, неплохо, но я сделал бы лучше."

    main_character "Наверняка тут много красивых драконих!"

    friend_character "Э-э-э, притормози, ты даже посвят не прошел, а уже про драконих."

    main_character "Минуту, что такое ИРИТ-РТФ?"

    main_character "Олежа, почему на сайте указан другой адрес, куда ты нас привел?"

    friend_character 'Да ладно тебе, я просто забил “[vars.university_name]” в навигаторе и мы пришли по адресу, который мне показали "Карты тридевятого царства", тут их “Яндекс карты” называют. Хорошее приложение кстати, правда на болоте бывает сбоит.'

    # СЦЕНА С ТЕЛЕФОНОМ, ПОИСКОМ В КАРТАХ

    main_character "Хм-м, ИРИТ-РТФ… Адрес есть, но навигатор не работает, похоже пора покупать новую грушу."

    main_character "Дубина ты стоеросовая! Мы пришли не туда. Это главное здание [vars.university_name], а нам в тот, что рядом, в ИРИТ-РТФ!"

    main_character "Ок, давай спросим местного, может он нам подскажет где эта Мира 32."


    ######### Подключается сцена с гигапряней

    # play sound audio.pryanyasteps fadein 1

    main_character "День добрый, не подскажите, где тут находится ИРИТ-РТФ?"

    tips_character "О! Новенькие в радике, здарова пекусы! Тоже перепутали ГУК и корпус института, со всеми было, не раз проходили. Радик находится там, 200 метров. Идите в сторону черного дыма и не ошибетесь."

    main_character "Спасибо вам, доброго дня!"

    tips_character "И вам пекусы."

    # play sound audio.pryanyasteps
    # stop sound fadeout 1

    ########## Подключается сцена у ИРИТа

    friend_character "Странный одноэтажный небоскреб."

    main_character "Да ладно тебе, не ГУК, но тоже ничего."

    main_character "Давай зайдем внутрь, там вроде что-то интересное происходит."

    friend_character "Пошли."

    ######## Подключается сцена презентации выбора предметов и правил игры
