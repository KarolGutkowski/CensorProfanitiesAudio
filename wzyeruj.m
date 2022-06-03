[y,fs] = audioread('k.wav');
Spill1 = importdata('output.txt');
for i=1:2:length(Spill1)
    y(Spill1(i)*fs:Spill1(i+1)*fs,:) = 0;
end

audiowrite('10Clean.wav',y,fs);

       