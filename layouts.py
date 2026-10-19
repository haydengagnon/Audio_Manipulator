import PySimpleGUI as sg

distortion_layout = [
    [
        sg.Text("Distortion Type"),
        sg.Combo(
            ["Fuzz", "Wavefold", "Bitcrush", "Chebyshev"],
            default_value="Fuzz",
            key="-DISTORTION_TYPE-",
        ),
    ],
    [
        sg.Text("Gain"),
        sg.Slider(
            range=(0, 20),
            default_value=10,
            resolution=0.1,
            orientation="h",
            size=(20, 15),
            key="-GAIN_DISTORTION-",
        ),
    ],
    [
        sg.Text("Mix"),
        sg.Slider(
            range=(0, 1),
            default_value=0.5,
            resolution=0.01,
            orientation="h",
            size=(20, 15),
            key="-MIX_DISTORTION-",
        ),
    ],
    [
        sg.Button("Preview", key="-PREVIEW_DISTORTION-"),
    ],
]

resonance_layout = [
    [
        sg.Text("Filter Type"),
        sg.Combo(
            ["Lowpass", "Bandpass"],
            default_value="Lowpass",
            key="-FILTER_TYPE_RESONANCE-",
        ),
        
    ],
    [
    sg.Text("Cutoff Frequency"),
        sg.Slider(
            range=(50, 5000),
            default_value=1500,
            resolution=1,
            orientation="h",
            size=(20, 15),
            key="-CUTOFF_FREQUENCY_RESONANCE-",
        ),
    ],
    [
        sg.Text("Resonance"),
        sg.Slider(
            range=(0, 5),
            default_value=0.7,
            resolution=0.1,
            orientation="h",
            size=(20, 15),
            key="-RESONANCE-",
        ),
    ],
    [
        sg.Text("Q Factor"),
        sg.Slider(
            range=(0.1, 10),
            default_value=1.0,
            resolution=0.1,
            orientation="h",
            size=(20, 15),
            key="-QFACTOR_RESONANCE-",
        ),
    ],
    [
        sg.Button("Preview", key="-PREVIEW_RESONANCE-"),
    ],
]

vocoder_layout = [
    [
        sg.Text("Carrier Type"),
        sg.Combo(
            ["Noise", "Sawtooth"],
            default_value="Noise",
            key="-CARRIER_TYPE_VOCODER"
        ),
    ],
    [
        sg.Text("Number of Bands"),
        sg.Slider(
            range=(1, 48),
            default_value=16,
            resolution=1,
            orientation="h",
            size=(20, 15),
            key="-NUM_BANDS_VOCODER-",
        )
    ]
]

phaser_layout = [
    [
        
    ]
]

flanger_layout = [
    [
        
    ]
]

chorus_layout = [
    [
        
    ]
]

delay_layout = [
    [
        
    ]
]

glitch_layout = [
    [
        
    ]
]

multi_band_saturation_layout = [
    [
        
    ]
]

negative_audio_layout = [
    [
        
    ]
]

