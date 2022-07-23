

a = 1;
b = -5000.002;
c = 10;
% este bloque se trabajo con la primera ecuasion (3.12)

x1 = (-b + sqrt(b ^ 2 - 4 * a * c)) / (2 * a);
x2 = (-b - sqrt(b ^ 2 - 4 * a * c)) / (2 * a);
% este bloque se trabajo con la segunda ecuasion (3.13)
x3 = (-2 * c) / (b + sqrt(b ^ 2 - 4 * a * c));
x4 = (-2 * c) / (b - sqrt(b ^ 2 - 4 * a * c));

er1 = ((x1 - x3) / x1) * 100
er2 = ((x2 - x4) / x2) * 100
%los errores relativos porcentuales entre (x1-x3) y (x2-x4)
fprintf('er1 = \n',er1);
fprintf('er2 = \n',er2)
