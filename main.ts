input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showNumber(input.temperature())
})
input.onSound(DetectedSound.Loud, function on_sound_loud() {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    music.startMelody(music.builtInMelody(Melodies.JumpUp), MelodyOptions.Once)
})
input.onGesture(Gesture.ThreeG, function on_gesture_three_g() {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    music.startMelody(music.builtInMelody(Melodies.Dadadadum), MelodyOptions.Once)
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.showLeds(`
        . . # . .
                . # # # .
                # . # . #
                . . # . .
                . . # . .
    `)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showLeds(`
        . . # . .
                . # . # .
                # . . . #
                . # . # .
                . . # . .
    `)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    music.playSoundEffect(music.createSoundEffect(WaveShape.Sine, 5000, 0, 255, 0, 500, SoundExpressionEffect.None, InterpolationCurve.Linear), SoundExpressionPlayMode.UntilDone)
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.happy), SoundExpressionPlayMode.UntilDone)
})
basic.forever(function on_forever() {
    
})
