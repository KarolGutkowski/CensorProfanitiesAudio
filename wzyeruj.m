[y,fs] = audioread('audio_input_name.wav');
Spill1 = importdata('output.txt');
for i=1:2:length(Spill1)
    y(Spill1(i)*fs:Spill1(i+1)*fs,:) = 0;
end

audiowrite('audio_output_name.wav',y,fs);

       
