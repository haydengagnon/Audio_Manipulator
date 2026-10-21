from audio_dsp.effects import (
    fuzz_distortion,
    wavefold_distortion,
    bitcrush_distortion,
    chebyshev_fold_distortion,
    filter,
    vocoder,
)
from audio_dsp.utils import(
    load_audio,
    save_audio,
)
import PySimpleGUI as sg
import os
import soundfile as sf
import playsound as ps
import layouts
import numpy as np
from pydub import AudioSegment


sg.theme("DarkGrey11")

file_select = [
    [
        sg.Text("Audio File"),
        sg.In(size=(25, 1), enable_events=True, key="-FILE-"),
        sg.FileBrowse(file_types=(("Audio Files", "*.wav;*.mp3"),)),
        sg.Button("Play", key="-PLAY-"),
    ],
    [
      sg.Text("Modifier Type"),
      sg.Combo(
            ["Distortion", "Resonance", "Vocoder", "Phaser", "Flanger", "Chorus", "Delay", "Glitch", "Multi-Band Saturation", "Negative Audio", "Sidechain", "Compressor"],
            enable_events=True,
            key="-MODIFIER_TYPE-",
      )  
    ],
    [
        sg.Column(layouts.distortion_layout, key="-DISTORTION_LAYOUT-", visible=False),
        sg.Column(layouts.resonance_layout, key="-RESONANCE_LAYOUT-", visible=False),
        sg.Column(layouts.vocoder_layout, key="-VOCODER_LAYOUT-", visible=False),
    ],
]



layout = [
    [
        sg.Column(file_select),
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
        elif modifier_type =="Vocoder":
            window["-VOCODER_LAYOUT-"].update(visible=True)
        
        if modifier_type != "Distortion":
            window["-DISTORTION_LAYOUT-"].update(visible=False)
        if modifier_type != "Resonance":
            window["-RESONANCE_LAYOUT-"].update(visible=False)
        if modifier_type != "Vocoder":
            window["-VOCODER_LAYOUT-"].update(visible=False)
            
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
                file = None
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
                file = None
    elif event == "-PREVIEW_VOCODER-":
        try:
            sf.write("temp.wav", audio, sr)
            carrier_type = values["-CARRIER_TYPE_VOCODER-"]
            number_of_bands = int(values["-NUM_BANDS_VOCODER-"])
            frequency_range_low = int(values["-FREQUENCY_RANGE_LOW_VOCODER-"])
            frequency_range_high = int(values["-FREQUENCY_RANGE_HIGH_VOCODER-"])
            carrier_frequency = values["-CARRIER_FREQUENCY_VOCODER-"]
            output, sr = vocoder(carrier=None, modulator="temp.wav", carrier_type=carrier_type, carrier_freq=carrier_frequency, n_filters=number_of_bands, freq_range=(frequency_range_low, frequency_range_high))
            sf.write("temp.mp3", output, sr)
            ps.playsound("temp.mp3")
            os.remove("temp.mp3")
            os.remove("temp.wav")
        except:
            try:
                os.remove("temp.mp3")
                os.remove("temp.wav")
            except:
                file = None


window.close()