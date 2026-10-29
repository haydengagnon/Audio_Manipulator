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
        sg.Button("Save", key="-SAVE_DISTORTION-"),
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
        sg.Button("Save", key="-SAVE_RESONANCE-"),
    ],
]

vocoder_layout = [
    [
        sg.Text("Carrier Type"),
        sg.Combo(
            ["sawtooth", "noise"],
            default_value="sawtooth",
            key="-CARRIER_TYPE_VOCODER-"
        ),
    ],
    [
        sg.Text("Number of Bands"),
        sg.Slider(
            range=(1, 48),
            default_value=48,
            resolution=1,
            orientation="h",
            size=(20, 15),
            key="-NUM_BANDS_VOCODER-",
        )
    ],
    [
        sg.Text("Frequency Range Low"),
        sg.Slider(
            range=(0, 8000),
            default_value=80,
            resolution=1,
            orientation="h",
            size=(20, 15),
            key="-FREQUENCY_RANGE_LOW_VOCODER-",
        ),
    ],
    [
        sg.Text("Frequency Range High"),
        sg.Slider(
            range=(0, 8000),
            default_value=8000,
            resolution=1,
            orientation="h",
            size=(20, 15),
            key="-FREQUENCY_RANGE_HIGH_VOCODER-",
        ),
    ],
    [
        sg.Text("Carrier Frequency"),
        sg.Slider(
            range=(0, 8000),
            default_value=110,
            resolution=1,
            orientation="h",
            size=(20, 15),
            key="-CARRIER_FREQUENCY_VOCODER-",
        ),
    ],
    [
        sg.Button("Preview", key="-VOCODER_PREVIEW-"),
        sg.In(size=(25, 1), enable_events=True, key="-VOCODER_FOLDER_SELECT-"),
        sg.FolderBrowse(button_text="Select Save Folder"),
    ],
    [
        sg.Button("Save", key="-VOCODER_SAVE-"),
        sg.In(size=(15,1), enable_events=True, key="-VOCODER_FILENAME-", placeholder="Filename"),
    ],
    
]

phaser_layout = [
    [
        sg.Text("Phaser Rate"),
        sg.Slider(
            range=(0.0,1.0),
            default_value=0.5,
            resolution=0.1,
            orientation="h",
            size=(20,15),
            key="-PHASER_RATE-",
        ),
    ],
    [
        sg.Text("Phaser Depth"),
        sg.Slider(
            range=(0.0,1.0),
            default_value=0.8,
            resolution=0.1,
            orientation="h",
            size=(20,15),
            key="-PHASER_DEPTH-",
        ),
    ],
    [
        sg.Text("Phaser Stages"),
        sg.Slider(
            range=(1,12),
            default_value=4,
            resolution=1,
            orientation="h",
            size=(20,15),
            key="-PHASER_STAGES-",
        ),
    ],
    [
        sg.Text("Phaser Mix"),
        sg.Slider(
            range=(0.0,1.0),
            default_value=0.7,
            resolution=0.1,
            orientation="h",
            size=(20,15),
            key="-PHASER_MIX-",
        ),
    ],
    [
        sg.Button("Preview", key="-PHASER_PREVIEW-"),
        sg.In(size=(25, 1), enable_events=True, key="-PHASER_FOLDER_SELECT-", placeholder="Select Folder"),
        sg.FolderBrowse(button_text="Select Save Folder"),
    ],
    [
        sg.Button("Save", key="-PHASER_SAVE-"),
        sg.In(size=(15,1), enable_events=True, key="-PHASER_FILENAME-", placeholder="Filename"),
    ],
    
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
        sg.Column(distortion_layout, key="-DISTORTION_LAYOUT-", visible=False),
        sg.Column(resonance_layout, key="-RESONANCE_LAYOUT-", visible=False),
        sg.Column(vocoder_layout, key="-VOCODER_LAYOUT-", visible=False),
        sg.Column(phaser_layout, key="-PHASER_LAYOUT-", visible=False),
    ],
]