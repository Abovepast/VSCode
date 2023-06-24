clc,clear,prob = optimproblem;
x = optimvar('x',6,'Type','integer','LowerBound',0);
prob.Objective = sum(x);
con = optimconstr(6);
a = [60,70,60,50,20,30];
con(1) = x(1)+x(6)>=60;
for i = 1:5
    con(i+1) = x(i)+x(i+1)>=a(i+1);
end

prob.Constraints.con = con;
[sol,fval,flag] = solve(prob)
sol.x







clc,clear
prob=optimproblem('ObjectiveSense','max');
x=optimvar('x',2,3,'LowerBound',0);
a = [600,800]';
b = [600;750;625];
c = [4,12,16;-5,3,7];
prob.Objective=sum(sum(c.*x));
con=[a<=sum(x,2);(sum(x))'<=b
    0.5*sum(x(1,:))<=x(1,1)
    0.25*sum(x(1,:))<=x(1,2)
    x(1,3)<=0.1*sum(x(1,:))
    x(2,1)<=0.4*sum(x(2,:))
    x(2,2)<=0.4*sum(x(2,:))];
prob.Constraints.con = con;
[sol,fval] = solve(prob);sol.x
fval=vpa(fval)  %计算总利润
sproduct = vpa(sum(sol.x,2))   %计算两种糖的生产量