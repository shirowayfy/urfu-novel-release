﻿
define friend_character = Character('Огр', color="#c8ffc8")
define main_character = Character('Сергей', color="#808080")
define main_and_friend_character = Character('Сергей и Огр', color="#808080")
define tips_character = Character('Гига-Пряня', color="#808080")


# define audio.maintheme = vars.audio.soundtrack.main_theme
# define audio.starttheme = "audio/SSDDSSD.mp3"
define audio.call_sound = "audio/sounds/call_sound.mp3"
define audio.vibro_sound = "audio/sounds/vibro_sound.mp3"
define audio.not_berserk_theme = "audio/soundtracks/not_berserk_theme.mp3"
# define audio.donkeysound = "audio/DonkeySound.mp3"
# define audio.pryanyasteps = "audio/PryanyaSteps.mp3"


init -2:
    # image gf_bg = Movie(play="images/scene.webm", size=(1920, 1080))
    image main_menu = "gui/main_menu.png"
    image start_scene = "images/scenes/intro.jpg"
    image scene_with_notification = "images/scenes/intro_with_notification.jpg"

label main_menu:
    scene main_menu
    jump main_menu_screen

label start:

    scene start_scene
    stop music fadeout 1

    play music audio.not_berserk_theme

    "Сергей закончил школу. Прошли 11 лет его жизни.Углубляясь в прошлое, его настигает меланхолия."

    main_character "Получил среднее образование, но, зачем оно мне, что я узнал за это время? Много ли я вспомню из школьной программы за последние года?"
    main_character "Я так и не понял, что мне интересно, кем я хочу быть. Кажется все, кроме меня уже добились успеха хоть в чем-то."
    main_character "Васька получил золотой значок ГТО, Иван накопил на свою первую машину, а Гриша так вообще устроился фронтендом сразу после школы, чем я хуже?"
    main_character "Неужели, абсолютно все уже знают как обустроить свою жизнь. У всех есть планы на будущее, невероятные амбиции к саморазвитию и самосовершенствованию."
    main_character "Я люблю играть в игры, смотреть аниме, читать книги и смотреть сериалы с фильмами. Но это не поможет мне найти работу."

    "Сергей пребывал в полной растерянности, его мучали терзания, абсолютный хаос и пустота после потери своей повседневности - школьных будней."

    main_character "Черт! Не понимаю. Как понять, кем я хочу быть? Чем я хочу заниматься? Что мне вообще может быть интересно?"

   
    play sound audio.vibro_sound
    stop music fadeout 4

    scene scene_with_notification
    # play sound audio.donkeysound

    # 'Вы приняты на специальность "Прикладная информатика"'


    "Сергей с недоверием посмотрел на телефон и 5 раз все перкпроверил. Его в самом деле приняли в УРФУ, единственный вуз, куда он подал документы."


    main_character "Офигеть! Я не думал, что я все-таки пройду. Вот это повезло!"

    "Осла переполняли эмоции, он был взбудоражен и потрясен этим событием."

    main_character "Это что же это, придется съехать от родителей? А как получить общагу? Блин, там же наверняка будут тараканы. А кто будут соседями, надеюсь не феи и огры. Не люблю их. А как же мои вещи, как их перевезти."

    
    play music audio.call_sound

    main_character "Голова болит. Минуту назад я размышлял о бытие, а сейчас уже думаю как перевезти вещи в общагу!"
   
    stop music

    main_character "На аппарате?"

    show shrek at center

    friend_character "Ало, ало, слышно меня?"

    main_character "Да, да, привет."

    friend_character "Здарова мужик, тебе тоже пришло письмо от госуслуг?"

    main_character "Всмысле тоже? Ты тоже подавал заявление на поступление в УРФУ?"

    friend_character "Да, ты что забыл, я же упоминал это на выпускном. Совсем там в облаках залетался, раз даже этого не помнишь."

    main_character "Вот так сюрприз!"

    friend_character "Ну чтож, будем соседями по общаге"

    main_character "Ладно, только не бери с собой мешок лука и не ешь его в нашей комнате!"

    friend_character "Ахахпхах, хорошо, договорились!"

    main_character "Не хочешь прогулятся до туда, хоть глянем куда поступили?"

    friend_character "Давай, только что сам хотел предложить!"


    ############ Здесь должна подключаться сцена С ГУКом


    main_and_friend_character "Огоооо, монументально"

    main_character "Не думал, что УРФУ выглядит так. Напоминает какой-нибудь Гарвард или Оксфорд."

    friend_character "Согласен, красиво."

    main_character "Наверняка тут много красивых драконих."

    friend_character "Э-э-э, притормози, ещё даже посвят не прошёл, а ты уже про драконих."

    main_character "Минуту, что такое ИРИТ-РТФ?"

    main_character "Огр, почему на сайте указан другой адрес, куда ты нас привел?"

    friend_character 'Всмысле, я просто забил "Урфу" в навигаторе и мв пришли по адресу, который мне показали "Карты тридевятого царства". Хорошее приложение кстати, правда на болоте плохо ориентируется.'

    main_character "*Гуглит информацию об Ирит-РТФ*"

    main_character "Дубина ты сталеросовая! Мы пришли не туда. Это главное здание  УРФУ, а мы учимся в институте по близости, в ИРИТ-РТФ."

    main_character "Ладно, давай спросим местного, мб он нам подскажет куда нам идти."


    ######### Подключается сцена с гигапряней

    # play sound audio.pryanyasteps fadein 1

    main_character "Здравствуйте, не подскажите, где тут находится ИРИТ-РТФ?"

    tips_character "О! Новенькие в радике, здарова пекусы! Тоже перепутали ГУК и корпус института, со всеми было, не раз проходили. Радик находится вон в том направлении в 200 метрах. Идите в сторону дымного тумана и не ошибетесь."

    main_character "Спасибо вам, доброго дня! :)"

    tips_character "И вам пекусы."

    # play sound audio.pryanyasteps
    # stop sound fadeout 1

    ########## Подключается сцена у ИРИТа

    friend_character "Неон в тумане, красиво."

    main_character "Да, и не поспоришь. Не так монументально как у ГУКа, но тоже ничего."

    main_character "Давай зайдем внутрь, там вроде что-то интересноу происходит."

    friend_character "Пошли."

    ######## Подключается сцена презентации выбора предметов и правил игры
