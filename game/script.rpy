define friend_character = Character('Огр', color="#c8ffc8", image="ogre")
define main_character = Character('Сергей', color="#808080", image="donkey")
define main_and_friend_character = Character('Сергей и Огр', color="#808080")
define doril = Character('Дорил', image="doril")
define humpty = Character('Шалтай', image="humpty")
define fiona = Character('Огриха-Староста', image="fiona")
define cat = Character('Костя', image="cat")
define wizard = Character('Физик-Волшебник', image="wizard")
define fairy = Character('Фея-Англичанка', image="fairy")
define rumpel = Character('Румпель-миддл-в-контуре', image="rumpel")
define tips_character = Character('Гига-Пряня', color="#808080", image="cookie")
define tamara = Character('Тамара', image="doril")

define answers = 0

define bad_ending = 0
define good_ending = 0
define bro_ending = 0
define kot = 0
define shrek = 0

define audio.maintheme = vars.audio.soundtrack.main_theme
# define audio.starttheme = "audio/SSDDSSD.mp3"
define audio.call_sound = "audio/sounds/call_sound.mp3"
define audio.vibro_sound = "audio/sounds/vibro_sound.mp3"
define audio.donkeysound = "audio/DonkeySound.mp3"
define audio.discord_leave = "audio/sounds/disconnect.mp3"
define audio.discord_join = "audio/sounds/user_join.mp3"
define audio.unmute = "audio/sounds/unmute.mp3"
# define audio.pryanyasteps = "audio/PryanyaSteps.mp3"


init -2:
    # image gf_bg = Movie(play="scene.webm", size=(1920, 1080))
    image main_menu:
        "images/menu/sketch_s_travoy.jpg"
        #10
        #"images/menu/football_1.jpg"
        #10
        #"images/menu/girl.jpg"
        #10
        #repeat

    define scenes_path = "images/scenes"

    image start_scene = scenes_path + "/start.png"
    image scene_with_notification = scenes_path + "/notify.png"
    image guk = scenes_path + "/guk.jpg"
    image rtf = scenes_path + "/rtf.png"
    image eng = scenes_path + "/eng.png"
    image phys = scenes_path + "/phys.png"
    image proga = scenes_path + "/proga.png"
    image brothers = scenes_path + "/brothers.png"
    image bad = scenes_path + "/bad.png"
    image good = scenes_path + "/good.png"
    image call_pic = scenes_path + "/call.png"

screen error_panel:
    modal True
    frame:
        padding(50,50,50,50)
        xalign 0.5
        yalign 0.5
        xsize 1000
        ysize 500

        vbox:
            text _("Извините, но при выборе предметов произошла ошибка системы(x00078), поэтому она автоматически распределила для вас преподавателей в случайном порядке")
            null height 20
            textbutton _("Закрыть") action Hide("error_panel")

label main_menu:
    scene main_menu
    jump main_menu_screen

label start:
    $ _dismiss_pause = False
    $ _dismiss_video = False
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

    scene call_pic

    main_character "На аппарате?"

    stop music

    show ogre normal at right

    friend_character "Ало, ало, меня слышно?"

    hide ogre normal

    show donkey happy at left

    main_character "Нет, день добрый."

    hide donkey happy

    show ogre normal at right

    friend_character "Здарова мужик, ты это, поступил?"

    hide ogre normal

    show donkey happy at left

    main_character "Поступил? Ты тоже подавал в [vars.university_name]?"

    hide donkey happy

    show ogre normal at right

    friend_character "Да, ты забыл? Я же говорил об этом. Совсем там в облаках заплутал, даже этого не помнишь."

    hide ogre normal

    show donkey happy at left

    main_character "Вот так сюрприз!"

    hide donkey happy

    show ogre normal at right

    friend_character "Похоже будем соседями по общаге."

    hide ogre normal

    show donkey happy at left

    main_character "Ага, но не надо тащить с собой мешок лука, да и есть его в нашей комнате не стоит."

    hide donkey happy

    show ogre normal at right

    friend_character "Ну чего ты… Ладно, договорились!"

    friend_character "Не хочешь прогуляться, хоть глянем куда поступили?"

    hide ogre normal

    show donkey energized at left

    main_character "Давай, я и сам хотел предложить!"

    hide donkey energized

    ############ Здесь должна подключаться сцена С ГУКом

    scene guk

    show donkey outdoor at left
    show ogre outdoor at right

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

    hide donkey outdoor
    hide ogre outdoor

    ######### Подключается сцена с гигапряней


    show guk_s_pryaney

    # play sound audio.pryanyasteps fadein 1

    main_character "День добрый, не подскажите, где тут находится ИРИТ-РТФ?"

    tips_character "О! Новенькие в радике, здарова пекусы! Тоже перепутали ГУК и корпус института, со всеми было, не раз проходили. Радик находится там, 200 метров. Идите в сторону черного дыма и не ошибетесь."

    main_character "Спасибо вам, доброго дня!"

    tips_character "И вам пекусы."

    # play sound audio.pryanyasteps
    # stop sound fadeout 1

    ########## Подключается сцена у ИРИТа

    show rtf

    show donkey outdoor at left
    show ogre outdoor at right

    friend_character "Странный одноэтажный небоскреб."

    main_character "Да ладно тебе, не ГУК, но тоже ничего."

    main_character "Давай зайдем внутрь, там вроде что-то интересное происходит."

    friend_character "Пошли."

    ######## Подключается сцена презентации выбора предметов и правил игры

    scene rtf

    show doril neytral1
    tamara "Куда идем? Студенческий покажите!"

    hide doril
    show ogre outdoor at left

    friend_character "Здравствуйте, так нету, еще не выдали."

    friend_character "Пришли просто институт глянуть."

    show doril zzlaya
    hide ogre

    tamara "Разглядывать дома у себя будете, а без студенческого не пущу!"
    tamara "Приходите первого сентября, после выбора предметов, там и получите пропуски."
    show iot with Fade(1.0, 1.0, 1.0)

    fairy "Дорогие студенты 5 направления, ваше обучение будет построено по принципу ИОТ."
    fairy "ИОТ позволяет самостоятельно конструировать собственный уникальный маршрут обучения в университете."
    fairy "Система ИОТ ориентирована на индивидуализацию студента в учебном пространстве как по уровню сложности,"
    fairy "так и по выбору дисциплин, что позволяет ему углубленно изучить выбранную траекторию и стать конкурентоспособнее на рынке труда."
    fairy "Каждый семестр, на основе выбора студента (форма обучения, уровень сложности) формируются учебные команды."
    fairy "Здесь студент-айтишник может встретиться со студентами радиотехнических и инженерных направлений."
    fairy "За 4 года в общеуниверситетском пространстве каждый обучающийся становится участником минимум 20 смешанных учебных команд"
    fairy "Разве не чудесно?"
    fairy "Выбор расписания и учителей состоится на платформе модеус через полчаса после трансляции."
    fairy "Также хочу напомнить, что в будущем, вы будете делится на волны, которые будут выбирать свое расписание поочередно"
    fairy "Зависеть это будет от вашей успеваемости."
    fairy "Таким образом, отличники будут выбирать самые интересные предметы в самое удачное время, остальным же придется выбирать из остатков."
    fairy "Ну да ладно, что там о втором семестре."
    fairy "Сейчас вам всем предстоит выбрать предметы в одной волне."
    fairy "Учитывая, сколько в этом году первокурсников, желаю вам удачных голодных игр!"

    call screen expression_showcase_screen()

    show screen error_panel

    main_character "Чтож, я по крайней мере пытался"

    scene rtf with Fade(1.0, 1.0, 1.0)

    show donkey outdoor at left
    show ogre outdoor at right

    main_character "О, здарова, Олегофренд, чего опаздываешь? Я тебя тут уже как полчаса жду."

    friend_character "Ты только представь, дракон приземлился прямо на дилижанс и все движение встало, хорошо хоть трамваи ездили, но из-за какого-то кросса наций пришлось стоять по 3 минуты на каждом повороте. Дорога заняла целый час."

    friend_character "И все же стоило селится в общаге, так хоть не пришлось бы тратить столько времени на дорогу. Возможно даже познакомился бы с красивой огрихой.."

    friend_character "Ладно, какие у нас планы на сегодня, что у тебя по парам на сегодня?"

    main_character "Всего ничего, разве что физика первой парой. А у тебя?"

    friend_character "У меня Огрология, как биология, но для огров, я поступил на целевое, поэтому приходится ходить на этот предмет,"

    friend_character "ООО (Огрологическое Офтальмологическое Общество), папа устроил по местной квоте. Представь себе, существует целый предмет, изучающий биологию огров."

    friend_character "Вот ты знал, что у нас есть “карман Генри”, прямо как у котов. Не знаю зачем оно. Ученые до сих пор не выяснили зачем он котам, а ограм то и подавно. Не понимаю, зачем мне эта информация."

    friend_character "Ты только представь, дракон приземлился прямо на дилижанс и все движение встало, хорошо хоть трамваи ездили, но из-за какого-то кросса наций пришлось стоять по 3 минуты на каждом повороте. Дорога заняла целый час."

    friend_character "Что думаешь, не хотел бы пропустить физику и куда-нибудь сходить?"

    menu:
        "Пойти с Олегом":
            jump skip_classes

        "Пойти на физику":
            jump go_study

    return

    label skip_classes:

        main_character "Да, давай, не очень то и хотелось идти на физику."

        friend_character "Вот увидишь, ты не пожалеешь!"

        $ bro_ending += 1

        jump second_day

        # пересказ дня слайдами

    label go_study:

        main_character "Это конечно хорошо, но пропускать первый день в институте опрометчиво, я все же схожу."

        friend_character "Олух, это все фигня, вот увидишь, как будет скучно на твоей физике. Жди фото с  “Отравленного яблока”"

        # звук хлопанья дверью

        scene phys

        # звуки вентиляции

        show wizard normal

        wizard "Кхе-кхе, здравствуйте студенты, как ваши дела? Все в порядке? Никто не пострадал?"

        wizard "У кого-то тут есть изолента, мне кажется она мне точно понадобится, кажется в поиске своей драконьей ковырялки я сломал свои очки."

        main_character "Мда, мужик явно с прибабахом, надо было идти с огром."

        # Таймскип, разбор темы

        show wizard thoughtful

        wizard "Есть кто-то из смельчаков решить пару примеров на плюсик у доски?"

        menu:
            "Не выходить к доске":
                jump nothing_to_do
            "Осмелиться и всё же хотя бы попробовать":
                jump try_to_solve

        return

        label nothing_to_do:

            main_character "Ну нафиг, все равно ничего не знаю, пожалуй не стоит позориться у доски."

            $ bad_ending += 1

            wizard "Неужели никто не хочет, что ж, тогда всем до следующего занятия начертить график механического движения прыгающей лягушки и описать ее движение!"

            jump second_day

        label try_to_solve:

            main_character "Что ж, давайте попробую"
            $ good_ending += 1

            menu:
                wizard "Назовите формулу для Второго Закона Ньютона."
                "F = m * a":
                    $ answers += 1
                "I = U / R":
                    pass
                "F1 = -F2":
                    pass

            menu:
                wizard "Теперь скажите, чему равно ускорение свободного падения"
                "10м/c^2":
                    pass
                "9,81м/с^2":
                    $ answers += 1

            menu:
                wizard "Хорошо, тогда назовите мне формулу момента силы."
                "E = mv^2 / 2":
                    pass
                "M = F * l":
                    $ answers += 1
                "M = F / a":
                    pass

            if answers >= 2:

                wizard "А вы неплохо разбираетесь в механике, молодой человек. 5 очков Грифф.. Ой! Извините, что-то занесло, вспомнил молодость."

                wizard "Садитесь, в вашу ведомость уже записан плюсик!"

            else:

                wizard "Молодой человек, учиться и учиться, но за смелость поощряю!"

                wizard "Садитесь, поставил плюсик в вашей ведомости, в следующий раз такое не пройдет, готовьтесь."

            $ answers = 0
            jump second_day

    label second_day:

        hide wizard with dissolve
        scene eng with Fade(1.0, 1.0, 1.0)

        main_character "Да что ж это такое, два дня подряд к первой паре, не учеба, а издевательство какое-то!"

        main_character "Спасибо хоть английский, не самый сложный предмет. Можно расслабится. Это тебе не физика с *дедушкой-волшебником*, падающим с потолка"

        show fiona normal

        fiona "Здравствуйте, к сожалению из-за рекордного количества студентов в этом году преподаватели не успели определить ваш текущий уровень английского, сегодня мы закроем этот просчет."

        hide fiona
        show fairy happy

        menu:
            fairy "Переведите это предложение: Hello, World"
            "Привет, Мир":
                $ answers += 1
            "Пока Мир":
                pass
        menu:
            fairy "А теперь нужно сделать перевод этого предложения: How Are You?"
            "Как ты?":
                $ answers += 1
            "Не подскажите, который час?":
                pass
        menu:
            fairy "OK, then translate what am i saying right now."
            "Хорошо, теперь скажите то, что я сказала вам 5 минут назад":
                pass
            "Ладно, а теперь переведите, что я говорю прямо сейчас":
                $ answers += 1

        if answers >= 2:
            "Ваш уровень - B2"
            $ kot += 1
            main_character "Вот что значит МБОУ СОШ Н99 имени Шрека с углубленным изучением англ. языка. Не зря учился 8 лет."

        else:
            "Ваш уровень - A1"
            $ shrek += 1
            main_character "Мда, но зато можно расслабится. Но все-же стоит подтянуть навыки перевода"

        jump third_day

    label third_day:

        scene proga with Fade(1.0, 1.0, 1.0)

        main_character "До сих пор не верится, что пара по проге проходит в дискорде."

        main_character "Расскажу друзьям, так все будут в шоке, думал будет как в школе, обычный класс с полумертвыми компьютерами, а разработка будет в какой-нибудь древней IDE."

        main_character "А здесь что-то современное, впервые такое вижу. Интересно, кто будет у меня преподавать."

        main_character "В этом году как-то все пошло наперекосяк и всех автоматически раскидало по преподавателям, надеюсь мне повезло и попался Сэр Пендрагон."

        main_character "Судя по табличке он отлично объясняет теорию, иногда даже позволяет сдавать практику позже крайнего срока."

        rumpel "здрав-ствуйй-тее, м-ня слшно? Ч-то с интрнетом."

        rumpel "секундочку"

        main_character "что это блин было."

        main_character "ладно, пары похоже не будет, можно и в доту скатать."

        scene bg_black with eyeclose
        scene proga with eyeopen

        "** спустя 2 катки в доту **"

        "**звук захода в дискорд**"

        rumpel "Здравствуйте, извините за задержку, кошка перегрызла оптоволокно"

        rumpel "Сегодня мы с вами познакомимся с азами *А-А-А-ПЧХИ*"

        rumpel "Простите, простудился. Так на чем это я остановился."

        rumpel "Ах да, сегодня мы с вами начнем изучать основы языка c#. Это прекрасный язык, который будет вам очень полезен в дальнейшей учебе, что ж, давайте начнем"

        # 25 кадр с челом с юлерна

        rumpel "Вот так можно проинициализировать базовые типы. Может быть кто-то сможет написать пару базовых вещей, исходя из того, что мы разобрали на текущей лекции?"

        menu:
            "Продолжить играть в доту":
                jump play_dota
            "Написать программу и представить её преподавателю":
                jump make_a_programm

        label play_dota:

            main_character "Черт, тут такая потная катка, да ну пофиг на эти баллы, титанчик сам себя не апнет, а мне ещё в вп играть"
            $ bad_ending += 1

            jump fourth_day

        label make_a_programm:
            play sound audio.unmute

            main_character "Да, я бы мог попробовать"
            $ good_ending += 1
            play sound audio.discord_leave

            main_character "Задача непростая, но я вроде справился, я надеюсь."

            play sound audio.discord_join
            # звук вылета из дискорда

            rumpel "Да господи, опять эта драная кошка, простите пожалуйста, ох уж эти соседские кошки в Тбилиси."
            rumpel "Только переехал, никак не могу совладать с ними. За все сегодняшние неполадки вы получаете плюсик в ведомость, а теперь - свободны."

            jump fourth_day
            # *звук за кадром, приглушенный, он забыл выключить микрофон*(дописать, что же там было) - пометка

    label fourth_day:

        scene eng with Fade(1.0, 1.0, 1.0)

        if kot == 1:

            show donkey happy white at left

            main_character "Кто в здравом уме мог поставить пару в 17 часов в субботу?!"

            hide donkey
            show cat happy at right

            cat "И не говори, что не день, то испытание."

            hide cat
            show donkey happy white at left

            main_character "О, Костя, привет, какими судьбами, тоже поступил в УРФУ?"

            hide donkey
            show cat happy at right

            cat "Так это ты, Серега, сначала и не приметил, слишком уж ты серый какой-то."

            cat "Да вот, перевелся сюда из ДГУ, условия получше, да и к дому поближе."

            cat "А ты сам каким образом тут оказался?"

            hide cat
            show donkey happy white at left

            main_character "Да вот, нажал не на ту кнопку во время катки в доту, так и занесло."

            main_character "Сам же знаешь, и не такое может быть во время тяжелых жизненных ситуаций."

            hide donkey
            show cat happy at right

            cat "ХА-Ха-ха, всегда ты умел сморозить чепуху!"

            hide cat
            show donkey happy white at left

            main_character "Ты случайно не знаешь, что это за группа по англу?"

            main_character "Я до сих пор не разобрался как написал тест, и куда я попал, может ты подскажешь?"

            hide donkey
            show cat happy at right

            cat "Друг мой, это группа с уровнем B2, исходя из этого могу поздравить тебя, ты попал в тот самый процент счастливчиков, что выбрали уровень, выше A0."

            cat "Не каждый на первом курсе хочет идти туда, ведь есть уровень попроще, да и особо напрягаться хотят."

            hide cat
            show donkey happy white at left

            main_character "Спасибо за объяснение"

        elif shrek == 1:

            show ogre normal at right

            friend_character "Серхио, что ты ноешь, расслабься ! :)"

            hide ogre
            show donkey happy white at left

            main_character "Ого, Олег!?"

            main_character "А ты что тут делаешь?"

            hide donkey
            show ogre normal at right

            friend_character "Что тут делаю? То же, что и ты, сижу… на паре по английскому."

            hide ogre
            show donkey happy white at left

            main_character "Это я понял, но как ты тут оказался, разве ты сдал на B2? Не думал, что ты настолько хорош в английском."

            hide donkey
            show ogre normal at right

            friend_character "Пф-ф, ты прав, я не настолько хорош в нем, а вот ты себя явно переоценил."

            friend_character "Мы в группе с уровнем A1, друг мой, лучше готовится надо было, если хотел в B2."

            hide ogre
            show donkey happy white at left

            main_character "0 _ 0"

            main_character "М-да, не ожидал, ну и ладно, менять уже нечего, можно расслабиться."

            hide donkey
            show ogre normal at right

            friend_character "Полностью согласен дружище, сиди и расслабляйся, ведь на A1 напряга нет."

        hide donkey
        hide ogre
        show humpty normal

        humpty "Здравствуйте-здравствуйте, доброго вечера всем, приветствую вас на занятии по английскому языку."

        humpty "Прежде чем начать, мне бы хотелось произнести небольшую речь, напутствие вам, первокурсникам, чтобы как-можно больше людей провели этот год с пользой."

        scene bg_black with eyeclose
        scene eng with eyeopen

        show humpty normal

        humpty "Также не стоит забывать о безопасности в походах. Очень важно брать с собой в поход пару отпугивателей медведей, в экстремальной ситуации это может спасти вам жизнь."

        if shrek == 1:
            hide humpty
            show donkey happy white at left
            show ogre normal at right
            main_and_friend_character "Господи, да когда это уже закончится."

        hide donkey
        hide ogre
        show humpty normal

        humpty "Я уже говорил, что река Нил в Египте замерзала всего дважды."

        humpty "В IX И XI ВЕКАХ"

        humpty "Что за удивительный факт! Неужели вас это не поражает?"

        scene bg_black with eyeclose
        scene eng with eyeopen

        humpty "Что-то я разговорился, всем спасибо за внимание, до следующей пары подготовьте конспект этой лекции."

        if shrek == 1:
            hide humpty
            show ogre normal at right
            friend_character "Когда я говорил, что можно расслабиться, я и предположить не мог, что мы вообще не будем заниматься английским."

            hide ogre
            show donkey happy white at left

            main_character "И что это будет настолько нудно!"

            main_character "Он почти 40 минут говорил про все и, одновременно, ничего, про какие-то походы, правила поведения в транспорте и красоты южных морей."

            hide donkey
            show ogre normal at right

            friend_character "Я и сам не до конца понял этой речи, после истории про череп ламантина глаза закрылись."

            friend_character "А проснулся я уже на моменте, когда он говорил про самую необычную новогоднюю ёлку в зимнем лесу."

            hide ogre
            show donkey happy white at left

            main_character "Провели время с пользой, ничего не сказать."

        else:
            hide humpty
            show cat happy at right

            cat "Не ожидал, что английский будет выглядеть подобным образом. Это больше походит на какое-то бжд с примесью дедовских историй!"
            hide cat

            show donkey happy white at left

            main_character "И что это будет настолько нудно!"

            main_character "Он почти 40 минут говорил про все и, одновременно, ничего, про какие-то походы, правила поведения в транспорте и красоты южных морей."

            main_character "Провели время с пользой, ничего не сказать."

        if bro_ending == good_ending:
            jump bro_end
        elif good_ending == 2:
            jump good_end
        elif bad_ending == bro_ending:
            jump bad_end
        elif bad_ending == 2:
            jump bad_end
        elif bad_ending == good_ending and shrek == 1:
            jump bro_end
        elif bad_ending == good_ending and kot == 1:
            jump bad_end

    label bro_end:
        scene brothers with Fade(1.0, 1.0, 1.0)
        "Остаток года Олег и Сергей были неразлучны, но из-за постоянных тусовок с другом, Сергей не смог закрыть долги во втором семестре и вместе с ним отправился в свободное плавание."
        main_character "Пейзаж навеивает воспоминания."
        main_character "Ты так не думаешь, Олег?"
        friend_character "Да, действительно, год был непростой, но нам с тобой определенно было весело."
        main_character "С этим не поспоришь."
        main_character "Что думаешь, есть мысли на дальнейшее будущее?"
        friend_character "Знаешь Серега, моя голова пуста. Не в том плане, как обычно. Я не знаю."
        main_character "Хорошо сказано. Я тоже не знаю."
        friend_character "Мы вместе, а это главное, не пропадем."
        friend_character "Главное двигаться вперед и не унывать."
        main_character "Согласен братан!"
        "Спустя 3 года, Олег и Сергей открыли перспективный стартап по разработке коммерческого софта для аэрокосмической отрасли."
        "На пути к этому их ждало много неудач, но это многому их научило и все это время они были неразлучны, вдвоем выстоя все невзгоды."
        hide bro_end
        $ renpy.movie_cutscene('videos/titres.ogv')
        return

    label good_end:
        scene good
        "Весь год Сергей пахал не покладая копыт, многие студенты и преподаватели оценили его старания и в конце - концов он был выдвинут на звание “Студента года”"
        main_character "И подумать не мог, что этот год обернется подобным образом."
        main_character "Думаю, что и сам себе не поверил бы, встретив себя настоящего в прошлом."
        main_character "Определенно, год был непростой, но он принес много новых знакомств, навыков, знаний."
        main_character "В конце концов, главное, что я сам про себя могу сказать, что я достоин."
        main_character "Жаль, что Олег не увидит номинацию."
        main_character "Будет еще обиднее, что в случае моей победы, я не смогу услышать его типичную подколку над собой."
        main_character "Хоть это меня и раздражало, но это было своего рода душевным."
        main_character "Интересно что с ним, где он?"
        main_character "Жаль, что из-за моего желания учиться наши пути разошлись."
        show cat happy at left
        cat "Серега, опять витаешь в облаках, иди на сцену, твоя очередь!"
        "За свои заслуги, Сергей получил звание “Студент года”, к сожалению его лучший друг не увидел этого, но видимо этому не суждено было случится."
        "Каждый пошел своей дорогой. В будущем Сергей устроился в “Индюкс” и построил блестящую карьеру. Про Олега же ничего больше не было слышно."
        "Неизвестно, что с ним произошло в дальнейшем.. (Прим. автора:Намёк на сиквел?)"
        hide good
        $ renpy.movie_cutscene('videos/titres.ogv')
        return

    label bad_end:
        scene bad
        main_character "Пуш мид дебил!"
        main_character "Господи да что вы творите!"
        main_character "Почему у войда нет бфа на 10 минуте, вы издеваетесь?"
        main_character "Да гори оно огнем, почему в каждой катке мне попадаются такие тиммейты!"
        "Из-за неуспеваемости в учебе, Сергея отчислили из [vars.university_name], впоследствии он пару лет жил с родителями, проводя праздный образ жизни."
        "Последующие пару лет, пока его сверстники строили карьеру и получали докторскую степень, Сергей апал ммр в надеже на то, что ему удастся стать киберкотлетой. К сожалению судьба была жестока."
        "Поняв, что затея не удалась, Сергей устроился менеджером среднего звена, где его жизнь протекала неспешно и размеренно, в однообразной рутине, поглотившей его навсегда…."
        hide bad
        $ renpy.movie_cutscene('videos/titres.ogv')
        return
