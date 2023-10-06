import librosa
import numpy as np
import random

def encode_audio_to_vector(audio_file_path, n_mfcc=13, n_fft=2048, hop_length=512):
    """
    Encode audio file to vector using librosa library.
    :param audio_file_path: str, path to audio file
    :param n_mfcc: int, number of MFCCs to return
    :param n_fft: int, length of the FFT window
    :param hop_length: int, number of samples between successive frames
    :return: numpy array, encoded audio vector
    """
    # Load audio file
    y, sr = librosa.load(audio_file_path)

    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

    # Normalize MFCCs
    mfccs_normalized = np.mean(mfccs.T, axis=0)

    return mfccs_normalized

def encode_audio_to_vector_batch(audio_file_paths, n_mfcc=13, n_fft=2048, hop_length=512):
    """
    Encode audio file to vector using librosa library.
    :param audio_file_paths: list, paths to audio files
    :param n_mfcc: int, number of MFCCs to return
    :param n_fft: int, length of the FFT window
    :param hop_length: int, number of samples between successive frames
    :return: numpy array, encoded audio vector
    """
    # Load audio file
    y, sr = librosa.load(audio_file_paths[0])

    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

    # Create empty array to store MFCCs
    mfccs_normalized = np.empty((len(audio_file_paths), mfccs.shape[0]))

    # Iterate over audio files
    for i, audio_file_path in enumerate(audio_file_paths):
        # Load audio file
        y, sr = librosa.load(audio_file_path)

        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

        # Normalize MFCCs
        mfccs_normalized[i] = np.mean(mfccs.T, axis=0)

    return mfccs_normalized

def encode_audio_to_vector_batch_parallel(audio_file_paths, n_mfcc=13, n_fft=2048, hop_length=512):
    """
    Encode audio file to vector using librosa library.
    :param audio_file_paths: list, paths to audio files
    :param n_mfcc: int, number of MFCCs to return
    :param n_fft: int, length of the FFT window
    :param hop_length: int, number of samples between successive frames
    :return: numpy array, encoded audio vector
    """
    # Load audio file
    y, sr = librosa.load(audio_file_paths[0])

    # Extract MFCC features
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

    # Create empty array to store MFCCs
    mfccs_normalized = np.empty((len(audio_file_paths), mfccs.shape[0]))

    # Iterate over audio files
    for i, audio_file_path in enumerate(audio_file_paths):
        # Load audio file
        y, sr = librosa.load(audio_file_path)

        # Extract MFCC features
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc, n_fft=n_fft, hop_length=hop_length)

        # Normalize MFCCs
        mfccs_normalized[i] = np.mean(mfccs.T, axis=0)

    return mfccs_normalized


def train_test_split_audio(audio_file_paths, test_ratio=0.2):
    """
    Split audio file paths into training and testing sets.
    :param audio_file_paths: list, paths to audio files
    :param test_ratio: float, ratio of files to use for testing
    :return: tuple, (training_files, testing_files)
    """
    # Shuffle audio file paths
    random.shuffle(audio_file_paths)

    # Split into training and testing sets
    split_index = int(len(audio_file_paths) * (1 - test_ratio))
    training_files = audio_file_paths[:split_index]
    testing_files = audio_file_paths[split_index:]

    # Encode audio files to vectors
    X_train = encode_audio_to_vector_batch_parallel(training_files)
    X_test = encode_audio_to_vector_batch_parallel(testing_files)

    return X_train, X_test
