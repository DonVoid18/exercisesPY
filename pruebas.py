function bairstow(fx,r,s,imax,es)

syms x % declaro variables simbolicas

coef = sym2poly(fx);
xra = roots(coef)
n = length(coef);
u = length(coef);
x = length(coef);
xr1 = [];
xr2 = [];
do = 0;
g=0;
iter = 0;
 while(do==0)
        for i=1:1:n
            if(i==1) 
              b(i) = coef(i);%permite calcular primer division sintetica
            elseif(i==2)
              b(i) = coef(i)+r*b(i-1);
            else  
              b(i) = coef(i)+r*b(i-1)+s*b(i-2);
            end     
        end
         for j=1:1:n-1
            if(j==1) 
              c(j) = b(j);
            elseif(j==2)
              c(j) = b(j) + r*c(j-1);     
            else        
              c(j) = b(j) + r*c(j-1) + s*c(j-2);
            end
         end
         b=fliplr(b)
         c=fliplr(c)
         det=(c(2))^2-c(1)*c(3);
         dr = (c(3)*b(1)-c(2)*b(2))/det;
         ds = (c(1)*b(2)-c(2)*b(1))/det;
         r = r + dr;
         s = s + ds;
         
         if(r ~= 0 && s ~= 0)
            ear = abs(dr/r) * 100;
            eas = abs(ds/s) * 100;
            fprintf('\ti= %d\tr= %2.4f\ts= %2.4f\tear= %2.3f\teas= %2.3f\n', iter,r,s,ear,eas);
        else 
            disp("El error es indeterminado");
         end
        
        if ((ear < es) && (eas<es)|| (iter >= imax))
          iter = 0; 
            b(1:2)=[]
            b=fliplr(b)
            coef=b;
            n = length(coef)
            x1 = ((r)+sqrt((r)^2+4*(s)))/2
            x2 = ((r)-sqrt(((r)^2+4*(s))))/2
            disp(r);
            disp(s);
   
            break;
           % b(1:2)=[]
            %b=fliplr(b)
            %n = length(b);
            if (n==3)
            x3 = (-coef(2)+((coef(2))^2-4*coef(1)*coef(3))^(1/2))/2*coef(1)
            x4 = (-coef(2)-((coef(2))^2-4*coef(1)*coef(3))^(1/2))/2*coef(1)
            break;
            end
            if (n==2)
                  x1 = -coef(2)/coef(1)
                break;
            end
        end
       
   % end
 % if ((ear < es) || (eas < es)|| (iter >= imax))
    %   break;
   
  %end
 end

end

