def on_button_pressed_a():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_sound_loud():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    music.start_melody(music.built_in_melody(Melodies.JUMP_UP), MelodyOptions.ONCE)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_three_g():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    music.start_melody(music.built_in_melody(Melodies.DADADADUM),
        MelodyOptions.ONCE)
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

def on_button_pressed_ab():
    basic.show_leds("""
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_leds("""
        . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
    """)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.happy),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_forever():
    pass
basic.forever(on_forever)
