from audio_dsp.effects import (
    fuzz_distortion,
    wavefold_distortion,
    bitcrush_distortion,
    chebyshev_fold_distortion,
    filter,
    vocoder,
    phaser_flanger,
    delay,
)
from audio_dsp.effects.random_chorus import chorus
from audio_dsp.effects.glitch import glitch
import PySimpleGUI as sg
import os
import soundfile as sf
import playsound as ps
import layouts
import shutil


sg.theme("DarkGrey11")

layout = [
    [
        sg.Column(layouts.file_select),
    ]
]

window = sg.Window("Audio Augmenter", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        try:
            os.remove("temp.wav")
            try:
                os.remove("temp.mp3")
                break
            except:
                break
        except:
            break

    if event == "-FILE-":
        file = values["-FILE-"]
        try:
            audio, sr = sf.read(file)
        except:
            file = None
    elif event == "-PLAY-":
        try:
            ps.playsound(file)
        except:
            file = None
    elif event == "-MODIFIER_TYPE-":
        modifier_type = values["-MODIFIER_TYPE-"]
        if modifier_type == "Distortion":
            window["-DISTORTION_LAYOUT-"].update(visible=True)
        elif modifier_type == "Resonance":
            window["-RESONANCE_LAYOUT-"].update(visible=True)
        elif modifier_type == "Vocoder":
            window["-VOCODER_LAYOUT-"].update(visible=True)
        elif modifier_type == "Phaser":
            window["-PHASER_LAYOUT-"].update(visible=True)
        elif modifier_type == "Flanger":
            window["-FLANGER_LAYOUT-"].update(visible=True)
        elif modifier_type == "Chorus":
            window["-CHORUS_LAYOUT-"].update(visible=True)
        elif modifier_type == "Delay":
            window["-DELAY_LAYOUT-"].update(visible=True)
            window["-DELAY_LAYOUT_DIGITAL-"].update(visible=True)
            window["-DELAY_LAYOUT_ANALOG-"].update(visible=False)
            window["-DELAY_MODE-"].update(value="digital")
        elif modifier_type == "Glitch":
            window["-GLITCH_LAYOUT-"].update(visible=True)
        
        if modifier_type != "Distortion":
            window["-DISTORTION_LAYOUT-"].update(visible=False)
        if modifier_type != "Resonance":
            window["-RESONANCE_LAYOUT-"].update(visible=False)
        if modifier_type != "Vocoder":
            window["-VOCODER_LAYOUT-"].update(visible=False)
        if modifier_type != "Phaser":
            window["-PHASER_LAYOUT-"].update(visible=False)
        if modifier_type != "Flanger":
            window["-FLANGER_LAYOUT-"].update(visible=False)
        if modifier_type != "Chorus":
            window["-CHORUS_LAYOUT-"].update(visible=False)
        if modifier_type != "Delay":
            window["-DELAY_LAYOUT-"].update(visible=False)
            window["-DELAY_LAYOUT_DIGITAL-"].update(visible=False)
            window["-DELAY_LAYOUT_ANALOG-"].update(visible=False)
        if modifier_type != "Glitch":
            window["-GLITCH_LAYOUT-"].update(visible=False)
    
    elif event == "-DELAY_MODE-":
        delay_mode = values["-DELAY_MODE-"]
        if delay_mode == "digital":
            window["-DELAY_LAYOUT_ANALOG-"].update(visible=False)
            window["-DELAY_LAYOUT_DIGITAL-"].update(visible=True)
        elif delay_mode == "analog":
            window["-DELAY_LAYOUT_DIGITAL-"].update(visible=False)
            window["-DELAY_LAYOUT_ANALOG-"].update(visible=True)
        
            
    elif event == "-PREVIEW_DISTORTION-":
        try:
            distortion_type = values["-DISTORTION_TYPE-"]
            gain = values["-GAIN_DISTORTION-"]
            mix = values["-MIX_DISTORTION-"]
            if distortion_type == "Fuzz":
                distorted_audio = fuzz_distortion(audio, gain=gain, threshold=0.2, mix=mix)
            if distortion_type == "Wavefold":
                distorted_audio = wavefold_distortion(audio, gain=gain, mix=mix)
            if distortion_type == "Bitcrush":
                distorted_audio = bitcrush_distortion(audio, bits=6, mix=mix)
            if distortion_type == "Chebyshev":
                distorted_audio = chebyshev_fold_distortion(audio, gain=gain, n=3, mix=mix)
            sf.write("temp.mp3", distorted_audio, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-SAVE_DISTORTION-":
        try:
            distortion_save_folder = values["-DISTORTION_SAVE_FOLDER-"]
            distortion_filename = values["-DISTORTION_FILENAME-"]
            distortion_type = values["-DISTORTION_TYPE-"]
            gain = values["-GAIN_DISTORTION-"]
            mix = values["-MIX_DISTORTION-"]
            if distortion_type == "Fuzz":
                distorted_audio = fuzz_distortion(audio, gain=gain, threshold=0.2, mix=mix)
            if distortion_type == "Wavefold":
                distorted_audio = wavefold_distortion(audio, gain=gain, mix=mix)
            if distortion_type == "Bitcrush":
                distorted_audio = bitcrush_distortion(audio, bits=6, mix=mix)
            if distortion_type == "Chebyshev":
                distorted_audio = chebyshev_fold_distortion(audio, gain=gain, n=3, mix=mix)
            sf.write("distorted.mp3", distorted_audio, sr)
            shutil.move("distorted.mp3", distortion_save_folder + "/" + distortion_filename + ".mp3")
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("distorted.mp3")
            except:
                pass

    elif event == "-PREVIEW_RESONANCE-":
        try:
            filter_type = values["-FILTER_TYPE_RESONANCE-"]
            cutoff_frequency = values["-CUTOFF_FREQUENCY_RESONANCE-"]
            resonance = values["-RESONANCE-"]
            qfactor = values["-QFACTOR_RESONANCE-"]
            if filter_type == "Lowpass":
                resonated_audio = filter(audio, sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="lowpass")
            elif filter_type == "Bandpass":
                resonated_audio = filter(audio, sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="bandpass")
            sf.write("temp.mp3", resonated_audio, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-SAVE_RESONANCE-":
        try:
            resonance_save_folder = values["-RESONANCE_FOLDER_SELECT-"]
            resonance_filename = values["-RESONANCE_FILENAME-"]
            filter_type = values["-FILTER_TYPE_RESONANCE-"]
            cutoff_frequency = values["-CUTOFF_FREQUENCY_RESONANCE-"]
            resonance = values["-RESONANCE-"]
            qfactor = values["-QFACTOR_RESONANCE-"]
            if filter_type == "Lowpass":
                resonated_audio = filter(audio, sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="lowpass")
            elif filter_type == "Bandpass":
                resonated_audio = filter(audio, sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="bandpass")
            sf.write("resonated.mp3", resonated_audio, sr)
            shutil.move("resonated.mp3", resonance_save_folder + "/" + resonance_filename + ".mp3")
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("resonated.mp3")
            except:
                pass

    elif event == "-VOCODER_PREVIEW-":
        try:
            sf.write("temp.wav", audio, sr)
            carrier_type = values["-CARRIER_TYPE_VOCODER-"]
            number_of_bands = int(values["-NUM_BANDS_VOCODER-"])
            frequency_range_low = int(values["-FREQUENCY_RANGE_LOW_VOCODER-"])
            frequency_range_high = int(values["-FREQUENCY_RANGE_HIGH_VOCODER-"])
            carrier_frequency = values["-CARRIER_FREQUENCY_VOCODER-"]
            vocoded, sr = vocoder(carrier=None, modulator="temp.wav", carrier_type=carrier_type, carrier_freq=carrier_frequency, n_filters=number_of_bands, freq_range=(frequency_range_low, frequency_range_high))
            sf.write("temp.mp3", vocoded, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
            os.remove("temp.wav")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.wav")
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-VOCODER_SAVE-":
        try:
            sf.write("temp.wav", audio, sr)
            vocoder_save_folder = values["-VOCODER_FOLDER_SELECT-"]
            vocoder_filename = values["-VOCODER_FILENAME-"]
            carrier_type = values["-CARRIER_TYPE_VOCODER-"]
            number_of_bands = int(values["-NUM_BANDS_VOCODER-"])
            frequency_range_low = int(values["-FREQUENCY_RANGE_LOW_VOCODER-"])
            frequency_range_high = int(values["-FREQUENCY_RANGE_HIGH_VOCODER-"])
            carrier_frequency = values["-CARRIER_FREQUENCY_VOCODER-"]
            vocoded, sr = vocoder(carrier=None, modulator="temp.wav", carrier_type=carrier_type, carrier_freq=carrier_frequency, n_filters=number_of_bands, freq_range=(frequency_range_low, frequency_range_high))
            sf.write("vocoded.mp3", vocoded, sr)
            shutil.move("vocoded.mp3", vocoder_save_folder + "/" + vocoder_filename + ".mp3")
            os.remove("temp.wav")
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("temp.wav")
            except:
                pass
            
    elif event == "-PHASER_PREVIEW-":
        try:
            phaser_rate = values["-PHASER_RATE-"]
            phaser_depth = values["-PHASER_DEPTH-"]
            phaser_stages = int(values["-PHASER_STAGES-"])
            phaser_mix = values["-PHASER_MIX-"]
            phaser_wet_mix = values["-PHASER_WET_MIX-"]
            phased = phaser_flanger(audio, sr, phaser_rate=phaser_rate, phaser_depth=phaser_depth, phaser_stages=phaser_stages, phaser_mix=phaser_mix, wet_mix=phaser_wet_mix, flanger_mix=0.0)
            sf.write("temp.mp3", phased, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass        
    elif event == "-PHASER_SAVE-":
        try:
            phaser_save_folder = values["-PHASER_FOLDER_SELECT-"]
            phaser_filename = values["-PHASER_FILENAME-"]
            phaser_rate = values["-PHASER_RATE-"]
            phaser_depth = values["-PHASER_DEPTH-"]
            phaser_stages = int(values["-PHASER_STAGES-"])
            phaser_mix = values["-PHASER_MIX-"]
            phased = phaser_flanger(audio, sr, phaser_rate=phaser_rate, phaser_depth=phaser_depth, phaser_stages=phaser_stages, phaser_mix=phaser_mix, wet_mix=0.0, flanger_mix=0.0)
            sf.write("phased.mp3", phased, sr)
            shutil.move("phased.mp3", phaser_save_folder + "/" + phaser_filename + ".mp3")
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("phased.mpe3")
            except:
                pass
            
    elif event == "-FLANGER_PREVIEW-":
        try:
            flanger_rate = values["-FLANGER_RATE-"]
            flanger_delay_base = values["-FLANGER_DELAY_BASE-"]
            flanger_delay_depth = values["-FLANGER_DELAY_DEPTH-"]
            flanger_mix = values["-FLANGER_MIX-"]
            flanged = phaser_flanger(audio, sr, flanger_rate=flanger_rate, flanger_delay_base=flanger_delay_base, flanger_delay_depth=flanger_delay_depth, flanger_mix=flanger_mix, phaser_mix=0.0)
            sf.write("temp.mp3", flanged, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-FLANGER_SAVE-":
        try:
            flanger_save_folder = values["-FLANGER_FOLDER_SELECT-"]
            flanger_filename = values["-FLANGER_FILENAME-"]
            flanger_rate = values["-FLANGER_RATE-"]
            flanger_delay_base = values["-FLANGER_DELAY_BASE-"]
            flanger_delay_depth = values["-FLANGER_DELAY_DEPTH-"]
            flanger_mix = values["-FLANGER_MIX-"]
            flanged = phaser_flanger(audio, sr, flanger_rate=flanger_rate, flanger_delay_base=flanger_delay_base, flanger_delay_depth=flanger_delay_depth, flanger_mix=flanger_mix, phaser_mix=0.0)
            sf.write("flanged.mp3", flanged, sr)
            shutil.move("flanged.mp3", flanger_save_folder + "/" + flanger_filename + ".mp3")
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("flanged.mp3")
            except:
                pass
            
    elif event == "-CHORUS_PREVIEW-":
        try:
            chorus_modulation_amount = values["-CHORUS_MODULATION_AMOUNT-"]
            chorus_speed = values["-CHORUS_SPEED-"]
            chorus_numberof_clones = int(values["-CHORUS_NUMBEROF_CLONES-"])
            chorus_delay = values["-CHORUS_DELAY-"]
            chorus_mix = values["-CHORUS_MIX-"]
            chorused = chorus(audio, sr, mix=chorus_mix, amount=chorus_modulation_amount, speed=chorus_speed, n_clones=chorus_numberof_clones, delay=chorus_delay)
            sf.write("temp.mp3", chorused, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-CHORUS_SAVE-":
        try:
            chorus_folder_select = values["-CHORUS_FOLDER_SELECT-"]
            chorus_filename = values["-CHORUS_FILENAME-"]
            chorus_modulation_amount = values["-CHORUS_MODULATION_AMOUNT-"]
            chorus_speed = values["-CHORUS_SPEED-"]
            chorus_numberof_clones = int(values["-CHORUS_NUMBEROF_CLONES-"])
            chorus_delay = values["-CHORUS_DELAY-"]
            chorus_mix = values["-CHORUS_MIX-"]
            chorused = chorus(audio, sr, mix=chorus_mix, amount=chorus_modulation_amount, speed=chorus_speed, n_clones=chorus_numberof_clones, delay=chorus_delay)
            sf.write("chorused.mp3", chorused, sr)
            shutil.move("chorused.mp3", chorus_folder_select + "/" + chorus_filename + ".mp3")
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("chorused.mp3")
            except:
                pass
    
    elif event == "-DELAY_PREVIEW_DIGITAL-":
        try:
            mode = values["-DELAY_MODE-"]
            delay_time = values["-DELAY_TIME-"]
            feedback = values["-DELAY_FEEDBACK-"]
            mix = values["-DELAY_MIX_DIGITAL-"]
            delayed = delay(audio, sr, delay_time=delay_time, feedback=feedback, mix=mix, mode=mode)
            sf.write("temp.mp3", delayed, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-DELAY_SAVE_DIGITAL-":
        try:
            folder_select = values["-DELAY_DIGITAL_FOLDER_SELECT-"]
            filename = values["-DELAY_DIGITAL_FILENAME-"]
            mode = values["-DELAY_MODE-"]
            delay_time = values["-DELAY_TIME-"]
            feedback = values["-DELAY_FEEDBACK-"]
            mix = values["-DELAY_MIX_DIGITAL-"]
            delayed = delay(audio, sr, delay_time=delay_time, feedback=feedback, mix=mix, mode=mode)
            sf.write("digital_delay.mp3", delayed, sr)
            shutil.move("digital_delay.mp3", folder_select + "/" + filename + ".mp3")
            sg.popup("File successfully saved to " + folder_select)
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("digital_delay.mp3")
            except:
                pass
    elif event == "-DELAY_PREVIEW_ANALOG-":
        try:
            mode = values["-DELAY_MODE-"]
            delay_time = values["-DELAY_TIME-"]
            feedback = values["-DELAY_FEEDBACK-"]
            lp_cutoff = values["-DELAY_LOWPASS_CUTOFF-"]
            flutter_depth = values["-DELAY_FLUTTER_DEPTH-"]
            pitch_drift_depth = values["-DELAY_PITCH_DRIFT_DEPTH-"]
            drive = values["-DELAY_DRIVE-"]
            mix = values["-DELAY_MIX_ANALOG-"]
            delayed = delay(audio, sr, delay_time=delay_time, feedback=feedback, mix=mix, mode=mode, lp_cutoff=lp_cutoff, flutter_depth=flutter_depth, pitch_drift_depth=pitch_drift_depth)
            sf.write("temp.mp3", delayed, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-DELAY_SAVE_ANALOG-":
        try:
            folder_select = values["-DELAY_ANALOG_FOLDER_SELECT-"]
            filename = values["-DELAY_ANALOG_FILENAME-"]
            mode = values["-DELAY_MODE-"]
            delay_time = values["-DELAY_TIME-"]
            feedback = values["-DELAY_FEEDBACK-"]
            lp_cutoff = values["-DELAY_LOWPASS_CUTOFF-"]
            flutter_depth = values["-DELAY_FLUTTER_DEPTH-"]
            pitch_drift_depth = values["-DELAY_PITCH_DRIFT_DEPTH-"]
            drive = values["-DELAY_DRIVE-"]
            mix = values["-DELAY_MIX_ANALOG-"]
            delayed = delay(audio, sr, delay_time=delay_time, feedback=feedback, mix=mix, mode=mode, lp_cutoff=lp_cutoff, flutter_depth=flutter_depth, pitch_drift_depth=pitch_drift_depth)
            sf.write("delayed.mp3", delayed, sr)
            shutil.move("delayed.mp3", folder_select + "/" + filename + ".mp3")
            sg.popup("File successfully saved to " + folder_select)
        except:
            sg.popup("Error saving file.")
            try:
                os.remove("delayed.mp3")
            except:
                pass
        
    elif event == "-GLITCH_PREVIEW-":
        try:
            n_segments = int(values["-GLITCH_NUMBER_OF_SEGMENTS-"])
            intensity = values["-GLITCH_INTENSITY-"]
            loop_length = values["-GLITCH_LOOP_LENGTH-"]
            glitched = glitch(audio, sr, n_segments=n_segments, intensity=intensity, loop_length=loop_length)
            sf.write("temp.mp3", glitched, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            sg.popup("Error previewing sound.")
            try:
                os.remove("temp.mp3")
            except:
                pass
    elif event == "-GLITCH_SAVE-":
        try:
            folder_select = values["-GLITCH_FOLDER_SELECT-"]
            filename = values["-GLITCH_FILENAME-"]
            n_segments = int(values["-GLITCH_NUMBER_OF_SEGMENTS-"])
            intensity = values["-GLITCH_INTENSITY-"]
            loop_length = values["-GLITCH_LOOP_LENGTH-"]
            glitched = glitch(audio, sr, n_segments=n_segments, intensity=intensity, loop_length=loop_length)
            sf.write("glitched.mp3", glitched, sr)
            shutil.move("glitched.mp3", folder_select + "/" + filename + ".mp3")
            sg.popup("File successfully saved to " + folder_select)
        except:
            sg.popup("Error saving sound.")
            try:
                os.remove("glitched.mp3")
            except:
                pass

window.close()