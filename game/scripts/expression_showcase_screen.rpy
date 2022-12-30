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
                    for exp in ['Януш', 'Волшебник', 'Румпель', 'Фея']:
                        textbutton exp:
                            action SetScreenVariable(
                                name="sprite_brows",
                                value=exp
                                )

                vbox:
                    label "Физика"
                    for exp in ['Януш', 'Волшебник', 'Румпель', 'Фея']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='sprite_eyes',
                                value=exp
                                )

                vbox:
                    label "Математика"
                    for exp in ['Януш', 'Волшебник', 'Румпель', 'Фея']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='sprite_mouth',
                                value=exp
                                )

                vbox:
                    label "Программирование"

                    for exp in ['Януш', 'Волшебник', 'Румпель', 'Фея']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='',
                                value=exp
                                )

                vbox:
                    label "История"
                    for exp in ['Януш', 'Волшебник', 'Румпель', 'Фея']:
                        textbutton exp:
                            action SetScreenVariable(
                                name='sprite',
                                value=exp
                                )


            # right
            textbutton 'Сохранить' action Return()
