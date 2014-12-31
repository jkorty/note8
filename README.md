audio-transcription
===================
1. Get input signal
2. 

Implementation of Fujishima's Chroma Vectors\n
    1.1. Process
      1.1.1. Get input signal
      1.1.2. Do spectral analysis
      1.1.3. Use Forier Transform to convert the signal to into a spectrogram
            (Forier transform is a type of time-frequency analysis)
            1.1.3.1 Time-Frequency Analysis
      1.1.4. Peak detection (only local max used)
      1.1.5. Do reference frequency computation procedure. Estimate the deviation with respect to 440 Hz.
      1.1.6. Do Pitch class mapping with respect to the estimated reference frequency. This is a procedure for determining the pitch class value from frequency values. A weighting scheme with cosine function is used. It considers the presence of harmonic frequencies (harmonic summation procedure), taking account a total of 8 harmonics for each frequency. In order to map the value on a one-third of a semitone, the size of the pitch class distribution vectors has to be equal to 36.
      1.1.7. Normalize the feature frame by frame dividing through the maximum value to eliminate dependency on global loudness. 
      
2. HMM

3. Convolutional Neural Networks
