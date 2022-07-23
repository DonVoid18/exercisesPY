
x=0.3*pi;
es=0.5e-08;
cosi=1;
j=1;
fprintf("j=%2.0f cos(x)=%0.10f\n",j,cosi)
fact = 1;
while(1)
    j=j+1;
    i=2*j-2;
    fact= fact*i*(i-1);
    cosn=cosi+((-1)^(j+1))*((x)^i)/fact;
    ea = abs((cosn-cosi)/cosn);
    fprintf("j=%2.0f cos(x)=%0.10f ea=%0.1e\n",j,cosn,ea);
    if ea<es,break,end
    cosi=cosn;
end