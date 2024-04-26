import librosa
import numpy as np
import random
import soundfile as sf

def load_audio(filename):
    """ Load an audio file """
    audio, sr = librosa.load(filename, sr=None)
    return audio, sr

def pitch_shift(audio, sr, n_steps):
    """ Shift the pitch of the audio within a small range suitable for short clips """
    return librosa.effects.pitch_shift(audio, sr=sr, n_steps=n_steps)

def time_stretch(audio, rate):
    """ Stretch the time of the audio without making it too unnatural for short clips """
    return librosa.effects.time_stretch(audio, rate=rate)

def add_noise(audio, noise_level=0.01):
    """ Add random noise to the audio at a level suitable for short clips """
    noise = np.random.randn(len(audio))
    augmented_audio = audio + noise_level * noise
    return augmented_audio

def apply_augmentation(audio, sr):
    """ Randomly apply one augmentation to avoid over-processing short audio """
    augmentations = [pitch_shift, time_stretch, add_noise]
    aug_func = random.choice(augmentations)
    if aug_func == pitch_shift:
        n_steps = random.choice([-1, 1])  
        audio = aug_func(audio, sr, n_steps)
    elif aug_func == time_stretch:
        rate = random.choice([0.9, 1.1])
        audio = aug_func(audio, rate)
    elif aug_func == add_noise:
        audio = aug_func(audio)
    return audio

def process_dataset(directory):
    """ Process each file in the dataset directory """
    import os
    files = [f for f in os.listdir(directory) if f.endswith('.mp3')]
    # print(len(files))
    for file in files:
        filepath = os.path.join(directory, file)
        try:
            audio, sr = load_audio(filepath)
            augmented_audio = apply_augmentation(audio, sr)
            output_path = os.path.join(directory, 'augmented_' + file)
            sf.write(output_path, augmented_audio, sr)
        except Exception as e:
            print(f"Error processing {file}: {str(e)}")
            
process_dataset('dataset')
