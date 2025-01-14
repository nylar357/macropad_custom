# SPDX-FileCopyrightText: 2021 Phillip Burgess for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Tones

# The syntax for Tones in macros is highly peculiar, in order to maintain
# backward compatibility with the original keycode-only macro files.
# The third item for each macro is a list in brackets, and each value within
# is normally an integer (Keycode), float (delay) or string (typed literally).
# Consumer Control codes were added as list-within-list, and then mouse and
# tone further complicate this by adding dicts-within-list. Each tone-related
# item is the key 'tone' with either an integer frequency value, or 0 to stop
# the tone mid-macro (tone is also stopped when key is released).
# Helpful: https://en.wikipedia.org/wiki/Piano_key_frequencies

# This example ONLY shows tones (and delays), but really they can be mixed
# with other elements (keys, codes, mouse) to provide auditory feedback.

app = {               # REQUIRED dict, must be named 'app'
    'name' : 'Tones', # Application name
    'macros' : [      # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0xFF9800, 'C3', [{'tone':131}]),
        (0xFF9800, 'C4', [{'tone':262}]),
        (0xFF9800, 'C5', [{'tone':523}]),
        # 2nd row ----------
        (0xC3FF93, 'Rising', [{'tone':131}, 0.2, {'tone':262}, 0.2, {'tone':523}]),
        (0xC3FF93, 'Holding', [{'tone':426}, 0.1, {'tone':155}, 0.2, {'tone':426}]),
        (0xC3FF93, 'Falling', [{'tone':523}, 0.2, {'tone':262}, 0.2, {'tone':131}]),
        # 3rd row ----------
        (0x5AB2FF, 'Mate', [{'tone':295}, 0.5, {'tone':600}, 1.0, {'tone':500}]),
        (0x5AB2FF, 'Fly', [{'tone':300}, 0.4, {'tone':356}, 1.4, {'tone':499}]),
        (0x5AB2FF, 'Run', [{'tone':190}, 2.2, {'tone':230}, 1.2, {'tone':100}]),
        # 4th row ----------
        (0xFF76CE, 'Gun', [{'tone':535}, 1.2, {'tone':234}, 0.6, {'tone':345}]),
        (0xFF76CE, 'Lie', [{'tone':325}, 1.0, {'tone':463}, 0.7, {'tone':623}]),
        (0xFF76CE, 'Steal', [{'tone':123}, 2.2, {'tone':421}, 1.2, {'tone':521}]),
        # Encoder button ---
        (0x000000, '', [])
    ]
}
