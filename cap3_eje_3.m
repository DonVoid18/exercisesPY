function xmin = getmin
x = 1;

while(1)
 if x <= 0, break, end
 
 xmin = x;
 x = x / 2;

end
