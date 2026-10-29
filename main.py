from audio_dsp.effects import (
    fuzz_distortion,
    wavefold_distortion,
    bitcrush_distortion,
    chebyshev_fold_distortion,
    filter,
    vocoder,
    phaser_flanger,
)
import PySimpleGUI as sg
import os
import soundfile as sf
import playsound as ps
import layouts
import numpy as np
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
        
        if modifier_type != "Distortion":
            window["-DISTORTION_LAYOUT-"].update(visible=False)
        if modifier_type != "Resonance":
            window["-RESONANCE_LAYOUT-"].update(visible=False)
        if modifier_type != "Vocoder":
            window["-VOCODER_LAYOUT-"].update(visible=False)
        if modifier_type != "Phaser":
            window["-PHASER_LAYOUT-"].update(visible=False)
            
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
            pass

    elif event == "-PREVIEW_RESONANCE-":
        try:
            filter_type = values["-FILTER_TYPE_RESONANCE-"]
            cutoff_frequency = values["-CUTOFF_FREQUENCY_RESONANCE-"]
            resonance = values["-RESONANCE-"]
            qfactor = values["-QFACTOR_RESONANCE-"]
            if filter_type == "Lowpass":
                resonated_audio = filter(audio, sample_rate=sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="lowpass")
            elif filter_type == "Bandpass":
                resonated_audio = filter(audio, sample_rate=sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="bandpass")
            sf.write("temp.mp3", resonated_audio, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
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
                resonated_audio = filter(audio, sample_rate=sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="lowpass")
            elif filter_type == "Bandpass":
                resonated_audio = filter(audio, sample_rate=sr, cutoff=cutoff_frequency, resonance=resonance, q=qfactor, filter_type="bandpass")
            sf.write("resonated.mp3", resonated_audio, sr)
            shutil.move("resonated.mp3", resonance_save_folder + "/" + resonance_filename + ".mp3")
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
            os.remove("temp.wav")

    elif event == "-PHASER_PREVIEW-":
        try:
            phaser_rate = values["-PHASER_RATE-"]
            phaser_depth = values["-PHASER_DEPTH-"]
            phaser_stages = int(values["-PHASER_STAGES-"])
            phaser_mix = values["-PHASER_MIX-"]
            phaser_wet_mix = values["-PHASER_WET_MIX-"]
            phased = phaser_flanger(audio, sample_rate=sr, phaser_rate=phaser_rate, phaser_depth=phaser_depth, phaser_stages=phaser_stages, phaser_mix=phaser_mix, wet_mix=phaser_wet_mix, flanger_mix=0.0)
            sf.write("temp.mp3", phased, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            try:
                os.remove("temp.mp3")
            except:
                pass
        
    elif event == "-PHASER_SAVE-":
        try:
            phaser_save_folder = values["-PHASER_FOLDER_SELECT-"]
            phaser_file_name = values["-PHASER_FILENAME-"]
            phaser_rate = values["-PHASER_RATE-"]
            phaser_depth = values["-PHASER_DEPTH-"]
            phaser_stages = int(values["-PHASER_STAGES-"])
            phaser_mix = values["-PHASER_MIX-"]
            phased = phaser_flanger(audio, sample_rate=sr, phaser_rate=phaser_rate, phaser_depth=phaser_depth, phaser_stages=phaser_stages, phaser_mix=phaser_mix, wet_mix=0.0, flanger_mix=0.0)
            sf.write("phased.mp3", phased, sr)
            shutil.move("phased.mp3", phaser_save_folder + "/" + phaser_file_name + ".mp3")
        except:
            pass

window.close()