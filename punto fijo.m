format long;
% metodo del punto fijo
x = 5;
eInicial = 0.00001;
i = 1;
disp('it    xi    g(x)');
while true
    
    %b = xr;
    b = 2*sin(sqrt(x));
    e = abs((b - x)/b);
    
    x = b;
    i = i +1;
    
    if e <= eInicial
        disp('Ra�z aproximada:');
        disp(b);
        break;
    end
end

