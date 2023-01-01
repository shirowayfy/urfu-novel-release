screen expression_showcase_screen():

    frame:
        xalign 0.5
        yalign 0.5
        padding (50, 50, 50, 50)
        ysize 500

        hbox:
            spacing 30

            # left
            viewport:
                scrollbars "vertical"
                xsize 400
                ymaximum config.screen_height
                child_size (None, 4000)

                has vbox

                vbox:
                    label "Английский язык"
                    for exp in ['Чижевски А.С.', 'Вострецова О.А.', 'Мамаева Г.В.', 'Шарычева А.А.']:
                        textbutton exp:
                            action SetScreenVariable(
                                name="sprite_brows",
                                value=exp
                                )

                vbox:
                    label "Физика"
                    for exp in ['Михалёва О.В.', 'Резник В.С.', 'Пушкарева А.С.', 'Плетнёва Е.В.']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='sprite_eyes',
                                value=exp
                                )

                vbox:
                    label "Математика"
                    for exp in ['Шестакова И.А.', 'Рыжкова И.В.', 'Борич А.А', 'Власова В.С.']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='sprite_mouth',
                                value=exp
                                )

                vbox:
                    label "Программирование"

                    for exp in ['Костромцов А.С.', 'Шалашова Т.Б.', 'Антоновская Н.В.', 'Лыкова Н.В.']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='',
                                value=exp
                                )

                vbox:
                    label "История"
                    for exp in ['Зиновьева Г.В.', 'Григоренко М.Г.', 'Воснецов А.В.', 'Смирнов С.Б.']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='sprite',
                                value=exp
                                )


            # right
            textbutton 'Сохранить' action Return()
