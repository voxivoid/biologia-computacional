fileID = fopen('q1_output.txt','r');

formatSpec = '%d %f %f';
sizeA = [3 Inf];

A = fscanf(fileID,formatSpec,sizeA);
fclose(fileID);

A = A';

x = A(:,1);
y1 = A(:,2);
y2 = A(:,3);

figure; hold on
a1 = plot(x,y1); M1 = '% of mismatching sites/Hamming distance';
a2 = plot(x,y2); M2 = 'Jukes-Cantor model                     ';
legend([a1; a2], [M1; M2]);

title('Sequence Identity Plot')
xlabel('# generations')
ylabel('y')