import numpy as np
#import matplotlib.pyplot as plt
#from IPython.display import Audio as play
from librosa import load,magphase,decompose,util,stft,istft,time_to_frames,feature
#import pandas as pd
import pickle

class vocalyze:
    def __init__(self,path,duration=60,rate=22050):
        self.__path = path
        self.__signal,self.__sr = load(path,duration=duration,sr=rate)
        self.__filtered = 0

    def get_signal(self):
        return self.__signal,self.__sr

    def vocal_melody(self):
        pass

    def vocal_regions(self):
        classified = self.__predict_voice_regions()
        vocal_regions = self.__combine_with_signal(classified)
        
        return vocal_regions

    def __predict_voice_regions(self):
        preprocessed = self.__preprocess()
        vrcmodel = pickle.load(open('vocal-region-classifier','rb'))
        prediction = vrcmodel.predict(preprocessed)
        return prediction

    def __combine_with_signal(self,prediction):
        predsong = []
        for x in range(len(prediction)):
            predsong.append(self.__signal[220*x:220*(x+1)]*(prediction[x]))
        predsignal=np.array(predsong).flatten()
        
        return predsignal
        
    def __preprocess(self):
        preprocessed = []
        filtered = self.__filter_voice(self.__signal,self.__sr)
        milliseconds = int((len(self.__signal)/self.__sr) * 100)
        for c in range(milliseconds):
            array = filtered[220*c:220*(c+1)]
            transform = np.abs(np.fft.fft(array)[:int(len(array)/2)])
            rms =  feature.rms(array,frame_length=220,hop_length=110).flatten()
            mfcc = feature.mfcc(array,n_fft=220,sr=44000,n_mfcc=20).flatten()
            concat = np.concatenate((rms,mfcc,transform))
            # concat = transform
            preprocessed.append(concat)
        preprocessed = np.array(preprocessed)
        normalised = self.__normalise(preprocessed)
        
        return normalised


    def __filter_voice(self,array,rate=22050):
        S_full, phase = magphase(stft(array))
        S_filter = decompose.nn_filter(S_full,
                                        aggregate=np.median,
                                        metric='cosine',
                                        width=int(time_to_frames(2, sr=rate)))
        S_filter = np.minimum(S_full, S_filter)

        margin_v = 25
        power = 2
        mask_v = util.softmask(S_full - S_filter,
                                    margin_v * S_filter,
                                    power=power)
        S_foreground = mask_v * S_full
        y_foreground = istft(S_foreground * phase)
    
        return y_foreground

    def __normalise(self,x):
        data = pickle.load(open('trainingdata','rb'))
        Max = np.max(data)
        Min = np.min(data)

        #normalisation
        X = x - Min
        X = x / (Max-Min)
        
        # End of normalisation
        return X
    






