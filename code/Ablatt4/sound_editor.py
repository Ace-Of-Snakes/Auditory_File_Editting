import numpy as np
import soundfile as sf
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt
import time
import platform

def downsampler(audio, samplerate, target_fs, save_audio = False):
    downsamp_factor = int(samplerate/target_fs)
    audio = audio[::downsamp_factor]
    if save_audio:
        return sf.write(f"code/Ablatt4/audios/sample{int(target_fs//1000)}.wav", audio, target_fs, subtype='PCM_24')
    else:
        return audio

def butter_filter(audio,samplerate, target_fs):
    # fs> 2*fmax
    b,a = butter(10, (target_fs/2)-1, btype='lowpass', output='ba', fs=float(samplerate))
    audio = lfilter(b,a,audio)
    audio = downsampler(audio, samplerate, target_fs,False)
    return sf.write(f"code/Ablatt4/audios/sample_butter{int(target_fs//1000)}.wav", audio, target_fs, subtype='PCM_24')

def reduce_bitdepth (signal:np.ndarray, target_bitdepth:int) -> np . ndarray:

    shift = signal.itemsize * 8 - target_bitdepth
    signal = signal >> shift
    signal = signal << shift
    return signal
    
    """
    Diese Funktion nimmt ein numpy - Array mit Elementen eines Integertyps
    entgegen und reduziert die Wortbreite ( engl . bitdepth ) auf einen
    gewünschten Wert. Das Ausgabesignal soll aber den selben Datentyp
    verwenden wie das Eingabesignal und überflüssige Bitstellen mit
    Nullen auffüllen .
    : param signal : ein numpy - Array , welches Elemente eines Integertyps enthält
    : param target_bitdepth : die Anzahl von Bits , die für  jedes Array - Element
    2
    verwendet werden soll
    : returns : ein numpy - Array mit dem selben Datentyp wie die Eingabe
    aber reduzierter Anzahl genutzter Bits
    """
def calc_snr(signal:np.ndarray, noise:np.ndarray) -> float:
    signal = signal.astype(np.float64)
    noise = noise.astype(np.float64)
    signal = np.sum(signal**2)
    noise = np.sum(noise**2)
    return 10*np.log10(signal/noise)
    """
    Diese Funktion berechnet den Signal - zu - Rauschabstand ( SNR ) eines
    Signals gegenüber einem Rauschsignal . Die Funktion nimmt zwei
    numpy - Arrays entgegen und gibt den SNR als float - Wert zurück .
    : param signal : ein numpy - Array , welches Elemente eines Integertyps enthält
    : param noise : ein numpy - Array , welches Elemente eines Integertyps enthält
    : returns : der SNR als float - Wert
    Berechnen des SNR mit Watt - Werten daher 10*log10(Psignal/Pnoise)
    """
def plot_spectrogram(audio, samplerate):
    plt.specgram(audio, Fs=samplerate)
    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.show()

def plot_samples(signal, noise, samplerate):
    quantization_error = np.subtract(audio, audio_reduced)
    '''
    Unsere zwei arrays haben die selbe Länge, daher können wir die beiden arrays einfach 
    subtrahieren und damit den quantization error berechnen.
    Um die aber sinnvoll zu visualiesieren, müssen wir den Bereich der angezeigten Werte reduzieren.
    Dazu dienen xmax und xmin. 
    Unsere arrays haben grad eine Länge von 2729936 Samples.
    '''
    time = 1/samplerate*np.arange(signal.size)
    second = samplerate
    xmin = time[58*second]
    xmax = time[60*second]
    print(calc_snr(signal, noise))

    fig, ax = plt.subplots(3)
    fig.suptitle(f"Original vs. reduced bitdepth to {intsize} bit")
    ax[0].plot(time,signal)
    ax[0].set_xlim(xmin,xmax)
    ax[0].set_title("Original")
    
    ax[1].plot(time,noise)
    ax[1].set_xlim(xmin,xmax)
    ax[1].set_title("Reduced")

    ax[2].plot(time,quantization_error)
    ax[2].set_title("Quantization error")
    ax[2].set_xlim(xmin,xmax)

    if platform.system() == 'Windows':    
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
    elif platform.system() == 'Linux':
        mng = plt.get_current_fig_manager()
        mng.resize(*mng.window.maxsize())
    elif platform.system() == 'Darwin':
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
    else:
        print("Unknown OS")

    plt.show(block=False)
    plt.pause(15)
    plt.close()


if __name__ == "__main__":
    # load in sound file
    # audio, samplerate = sf.read("code/Ablatt4/sample48.wav")
    # audio_length_in_sec = audio.shape[0]/48000
    # Function calls for task 1.1
    # audio_to_bit(audio, samplerate, 8000)
    # audio_to_bit(audio, samplerate, 16000)
    # audio_to_bit(audio, samplerate, 24000)

    # Function calls for task 1.2
    # butter_filter(audio, samplerate,8000)
    # butter_filter(audio, samplerate,16000)
    # butter_filter(audio, samplerate,24000)
    
    # Function calls for task 1.3
    audio, samplerate = sf.read("code/Ablatt4/audios/ear_raper_sample.wav", dtype='int16')
    intsize = 12
    audio_reduced = reduce_bitdepth(audio, intsize)
    plot_samples(audio,audio_reduced,samplerate)
    # plot_spectrogram(audio,samplerate)
    # sf.write(f"code/Ablatt4/audios/sample_int_{intsize}.wav", audio_reduced, samplerate, subtype='PCM_24')
    exit()