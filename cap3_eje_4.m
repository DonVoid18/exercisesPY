

vd = double(pi ^ 4 / 90);
sum = 0;
n = 10000;

for i=1:n
sum = sum + 1 / i ^ 4;

end 

 vr=100* abs((vd-sum)/vd);
fprintf('suma\n');
 disp(sum)
fprintf('muestra el error relativo porcentual verdadero\n');
 disp(vr)
 
